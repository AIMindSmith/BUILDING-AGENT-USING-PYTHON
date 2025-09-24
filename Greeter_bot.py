"""
what is greeter bot?
Before we going first we understanfd what is agent and how to build it?
agent maily build a three point
i) Percieve
ii)Think
iii)Act

these three thing mainly build different type of agent

Greeter bot
It will perceive the current time from the computer (its environment),
 think based on predefined rules (if it's morning, afternoon, or evening), 
 and act by printing the correct greeting. 

let's build it 

"""
# main.py
import datetime
import time

def perceive_environment():
    """
    Senses the current state of the environment.
    For our simple agent, this is just the current hour of the day.
    """
    current_hour = datetime.datetime.now().hour
    print(f"DEBUG: Perceived hour: {current_hour}")
    return {"current_hour": current_hour}

def think_and_decide_action(state):
    """
    The agent's "brain." It decides what action to take based on the state.
    This is a simple rule-based logic.
    """
    hour = state.get("current_hour")

    if hour is None:
        return "say_error_message"
    
    if 5 <= hour < 12:
        return "say_good_morning"
    elif 12 <= hour < 17:
        return "say_good_afternoon"
    elif 17 <= hour < 22:
        return "say_good_evening"
    elif 22<= hour <=5:
        return "say_good_night"
    else:
        return "sometjing_went_wrong"
def act(action):
    """
    The agent performs the action, affecting the environment (in this case, printing to the console).
    """
    if action == "say_good_morning":
        print("☀️ Good morning!")
    elif action == "say_good_afternoon":
        print("🌤️ Good afternoon!")
    elif action == "say_good_evening":
        print("🌙 Good evening!")
    elif action == "say_good_night":
        print("😴 Good night!")
    elif action == "say_error_message":
        print("❌ Sorry, I couldn't determine the time.")
    else:
        print("🤔 I'm not sure what to do.")

def agent_loop():
    """
    The main loop that drives the agent's behavior.
    """
    print("Agent started. Press Ctrl+C to stop.")
    try:
        while True:
            # 1. Perceive the environment
            current_state = perceive_environment()
            
            # 2. Think and decide on an action
            action_to_perform = think_and_decide_action(current_state)
            
            # 3. Act upon the decision
            print(f"DEBUG: Decided action: {action_to_perform}")
            act(action_to_perform)
            
            # Wait for a while before the next cycle
            print("-" * 20)
            time.sleep(5) # The agent "wakes up" every 5 seconds
            
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")

if __name__ == "__main__":
    agent_loop()








