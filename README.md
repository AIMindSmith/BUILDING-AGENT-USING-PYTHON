# My First AI Agent 🤖

This project is a step-by-step journey to build AI agents from scratch using Python. We start with the basics and progressively build more complex and intelligent agents.

## Project Evolution

### ✅ Step 1: Simple Rule-Based Greeter Agent (The Foundation)

Our first agent, `Greeter_bot.py`, was a simple "Greeter Bot" operating on a **Perceive-Think-Act** loop.

-   **Perceive**: It checked the system's current hour.
-   **Think**: It used a set of `if-elif-else` rules to decide on a greeting (e.g., "Good morning").
-   **Act**: It printed the chosen greeting to the console.

This foundational step taught us the core architecture of an autonomous agent.

---

### ✅ Step 2: LLM-Powered Chat Agent (The Brain Upgrade)

In this major upgrade, we replaced the rigid, rule-based "brain" with a powerful **Large Language Model (LLM)** using the Google Gemini API. The agent evolved from a simple bot into a true conversational AI.

#### Key Enhancements:
-   **Conversational Intelligence**: The agent can now understand and respond to a wide range of user inputs, not just the time of day.
-   **LLM Integration**: The `think` function now calls the Gemini API to generate dynamic, human-like responses.
-   **Secure API Key Handling**: We use a `.env` file to store the secret API key, which is kept out of version control thanks to `.gitignore`.

#### How to Run this Version:
1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Set up your environment:**
    -   Create a `.env` file.
    -   Add your API key to it: `GEMINI_API_KEY="YOUR_API_KEY_HERE"`
3.  **Run the agent:**
    ```bash
    python main.py
    ```

You can now have a full conversation with the agent in your terminal!

