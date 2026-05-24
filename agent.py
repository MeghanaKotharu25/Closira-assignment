import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class ClosiraAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        
        # Load SOP
        with open('sop.json', 'r') as f:
            self.sop = json.load(f)
            
        # Load System Prompt
        with open('system_prompt.txt', 'r') as f:
            self.system_prompt = f.read()
        
        self.state = "FAQ" 
        self.qual_questions = [
            "Which treatment are you interested in (Botox, Fillers, or Consultation)?",
            "Do you have any known allergies or medical conditions we should know about?",
            "What is your preferred date and time for an appointment?"
        ]
        self.qual_index = 0
        self.qual_data = {}
        self.history = [{"role": "system", "content": self.system_prompt}]

    def process_message(self, user_input):
        # 1. Global Escalation Check (Safety First)
        if self.is_escalation(user_input):
            self.state = "ESCALATED"
            return "I apologize, but I must escalate this to our management team for you. A representative will contact you shortly."

        if self.state == "ESCALATED":
            return "This conversation has been escalated to a human agent. Please hold."

        # 2. State-Based Logic
        if self.state == "SUMMARY":
            return "Thank you! I have passed your details to our booking team. They will contact you shortly."

        self.history.append({"role": "user", "content": user_input})

        if self.state == "FAQ":
            if "book" in user_input.lower() or "schedule" in user_input.lower():
                self.state = "QUALIFICATION"
                return f"I can help you with that! {self.qual_questions[0]}"
            return self.get_llm_response()

        elif self.state == "QUALIFICATION":
            self.qual_data[self.qual_questions[self.qual_index]] = user_input
            self.qual_index += 1
            if self.qual_index < len(self.qual_questions):
                return f"Noted. {self.qual_questions[self.qual_index]}"
            else:
                self.state = "SUMMARY"
                return self.generate_summary()

    def is_escalation(self, text):
        return any(t in text.lower() for t in self.sop['escalation_triggers'])

    def get_llm_response(self):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/your-username/closira-assignment",
            "X-Title": "ClosiraAgent",
            "Content-Type": "application/json"
        }
        payload = {"model": "meta-llama/llama-3.1-8b-instruct", "messages": self.history}

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            msg = response.json()['choices'][0]['message']['content']
            self.history.append({"role": "assistant", "content": msg})
            return msg
        except Exception as e:
            return "I apologize, I am experiencing technical difficulties. Please call our clinic directly."

    def generate_summary(self):
        return f"Conversation complete. Summary:\nIntent: Booking\nDetails collected: {json.dumps(self.qual_data)}\nRecommended Action: Pass to scheduling team."