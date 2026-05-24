# Prompt Design & Strategy

## 1. System Prompt
The system prompt is maintained in `system_prompt.txt` to ensure modularity. It defines the AI as the Lead Receptionist for Bloom Aesthetics Clinic, grounding its behavior in the provided SOP.

## 2. Hallucination Prevention
- **Strict Grounding:** The system prompt explicitly mandates the use of the SOP JSON. 
- **Constraint Injection:** We explicitly instruct the model: "If the answer is not in the SOP, do not make it up." 
- **API Guardrails:** By utilizing a System Prompt that prohibits general knowledge responses, we minimize the LLM's tendency to guess.

## 3. Confidence-based Escalation
We implement a two-tier escalation strategy:
1. **Keyword/Heuristic Layer:** The `is_escalation` method in `agent.py` performs a pre-processing check for high-risk triggers (complaints, medical advice, underage queries). This ensures safety regardless of the AI's "confidence" score.
2. **LLM Reasoning:** The System Prompt empowers the LLM to identify when it lacks the information required, instructing it to trigger an escalation or suggest a consultation.

## 4. Tone and Persona
- **Persona:** Professional, empathetic Lead Receptionist.
- **Constraints:** The model is restricted to a maximum of 3 sentences for standard responses to maintain efficiency. The tone is kept clinical and formal to match the business context of an aesthetics clinic.