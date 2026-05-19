# 🐍 My Python Mini Toolkit

> My first Python portfolio project — built as part of my learning journey at Life Choices YouthCode programme.

---

## 📌 Project Description

My Python Mini Toolkit is a simple, menu-based program that runs in the terminal. When you run it, I present you with a menu where you can choose from three mini tools I built. Each tool is interactive and takes your input directly. I built this project to show the Python concepts I have been learning during the YouthCode programme at Life Choices Academy.

---

## 🛠️ Features

| # | Tool | What it does |
|---|------|-------------|
| 1 | **Grade Calculator** | I ask for your score and tell you your letter grade (A–F) |
| 2 | **Number Guessing Game** | I pick a secret number between 1 and 100 — you have 5 attempts to guess it |
| 3 | **Budget Tracker** | I ask for your budget and how much you spent, then tell you what is left |

---

## 🧠 Python Concepts I Used

- **Variables & data types** — I used integers, floats, and strings throughout the project
- **User input & output** — I used `input()` and `print()` with f-strings to interact with the user
- **Type casting** — I used `int()` and `float()` to convert what the user types into usable numbers
- **Arithmetic operators** — I used subtraction to calculate the remaining budget
- **Comparison operators** — I used `==`, `<`, `>`, and `>=` for grade checks and game hints
- **Conditionals** — I used `if`, `elif`, and `else` to handle different outcomes in each tool
- **Loops** — I used a `for` loop with `range()` to manage the guessing attempts, and `break` to stop the loop early when the user wins
- **Functions** — I gave each tool its own function to keep my code organised
- **Modules** — I used the built-in `random` module and created my own custom module (`helpers.py`) which I import into `main.py`

---

## 📁 Project Structure

```
python-mini-toolkit/
├── main.py        # My main program — shows the menu and runs each tool
├── helpers.py     # My custom module — holds all three tool functions
└── README.md      # My project documentation (you are here)
```

---

## ▶️ How to Run My Project

### Requirements
- Python 3.x installed ([download here](https://www.python.org/downloads/))
- No extra libraries needed — I only used built-in modules

### Steps

1. Clone or download my repository:
   ```bash
   git clone https://github.com/adam-jattiem/python-mini-toolkit.git
   ```

2. Navigate into the project folder:
   ```bash
   cd python-mini-toolkit
   ```

3. Run the program:
   ```bash
   python main.py
   ```

4. Choose a tool from the menu (1–3) or press 4 to exit.

---

## 🧩 Challenges I Faced

- **Splitting my code across two files** — I had to learn how to import my own functions from `helpers.py` into `main.py` using `from helpers import ...`. Once I understood it, it made my code much cleaner and easier to read.
- **Managing the guessing game loop** — I had to figure out how to track remaining guesses inside a `for` loop and stop it early with `break` when the user guesses correctly. It took me a few tries to get the logic right.
- **Working with different data types** — I had to think carefully about when to use `int()` versus `float()`, especially in the budget tracker where the user might enter amounts with cents.

---

## 💡 What I Learned

- How to organise my project across multiple files using a custom module
- How to use `for` loops with `range()` to repeat actions a set number of times
- How `if/elif/else` chains let me handle many different conditions in one block
- How `break` lets me exit a loop early when a condition is met
- How to use the `random` module to generate numbers my program does not know in advance

---

## 🔮 What I Would Improve Next

- Add a `while` loop to the main menu so the user can keep using tools without restarting the program
- Let the user enter multiple expenses in the Budget Tracker instead of just one
- Add input validation so my program does not crash if someone types letters instead of numbers
- Add more tools such as a To-Do List or a Study Planner
- Save results to a text file so they are not lost when the program closes

---

## 👤 About Me

**Adam Jattiem**  
Life Choices Academy — YouthCode Programme  
