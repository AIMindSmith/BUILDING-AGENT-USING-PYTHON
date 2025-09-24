# My First AI Agent 🤖

This project is a step-by-step guide to building AI agents from scratch using Python. We start with the basics and progressively build more complex and intelligent agents.

## Step 1: Simple Rule-Based Greeter Agent

This is the foundational step. The agent, `main.py`, is a simple "Greeter Bot" that operates on a **Perceive-Think-Act** loop.

### How it Works
1.  **Perceive**: The agent checks the system's current hour.
2.  **Think**: It uses a set of `if-elif-else` rules to decide the appropriate greeting (e.g., "Good morning," "Good afternoon").
3.  **Act**: It prints the chosen greeting to the console.

The agent runs in a continuous loop, re-evaluating the time every 5 seconds.

### How to Run
```bash
python main.py
