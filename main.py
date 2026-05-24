from agent import ClosiraAgent

def main():
    agent = ClosiraAgent()
    print("--- Closira AI Agent Started ---")
    
    while True:
        user_input = input("\nCustomer: ")
        if user_input.lower() == 'exit':
            break
        
        response = agent.process_message(user_input)
        print(f"\nAgent: {response}")

if __name__ == "__main__":
    main()