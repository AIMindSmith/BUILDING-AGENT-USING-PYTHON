# main.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure_llm():
    """
    Configures the generative AI model with the API key.
    """
    load_dotenv() # Load environment variables from .env file
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    return model

def perceive_environment():
    """
    Senses the environment by getting input from the user.
    """
    user_input = input("You: ")
    return {"user_input": user_input}

def think_and_decide_action(state, model):
    """
    The agent's "brain." It uses the LLM to generate a response.
    """
    user_input = state.get("user_input")

    if not user_input:
        return "Sorry, I didn't get any input. Could you please repeat?"
        
    try:
        # The core of the new "think" process: calling the LLM
      prompt = f"You are a helpful and slightly funny assistant named Jarvis. Please answer the following question: {user_input}"
      response = model.generate_content(prompt) 
      return response.text
    except Exception as e:
        print(f"DEBUG: An error occurred: {e}")
        return "Sorry, I'm having trouble thinking right now."

def act(response_text):
    """
    The agent performs the action: printing the LLM's response.
    """
    print(f"Agent: {response_text}")

def agent_loop(model):
    """
    The main loop for the chat agent.
    """
    print("🤖 AI Agent is now online! (Type 'quit' to exit)")
    try:
        while True:
            # 1. Perceive user input
            current_state = perceive_environment()
            
            # Check for exit condition
            if current_state.get("user_input", "").lower() == "quit":
                print("Agent shutting down. Goodbye!")
                break
            
            # 2. Think using the LLM
            response = think_and_decide_action(current_state, model)
            
            # 3. Act by printing the response
            act(response)
            
            print("-" * 20)
            
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")

if __name__ == "__main__":
    try:
        llm_model = configure_llm()
        agent_loop(llm_model)
    except ValueError as e:
        print(e)