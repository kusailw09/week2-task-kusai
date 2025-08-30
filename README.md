#week2-task-kusai

# README.md....instructions and all

This repo contains 5 tasks.



 1) File-Based To-Do List Manager  
Approach: Extended Week 1 To-Do List, now saves tasks in a JSON file. On restart, tasks are reloaded.  
Run: python todo_list.py`  
Example: Add "Study" → saved → reopen → Study still there.  
Challenge: File read/write handling.



2) Currency Converter  
Approach: Fetches real-time exchange rates using an API. Converts user input amount from one currency to another.  
Run: python currency_converter.py`  
Example: 100 USD → 8300 INR (example rate).  
Challenge: API key & network issues.



3) Simple Quiz Application  
Approach:Quiz questions stored in JSON file. Program displays them, takes answers, and calculates final score.  
Run: python quiz_application.py`  
Example: Q: 2+2 → Ans: 4 → Score = +1.  
Challenge: JSON data parsing.



4) News Headlines Fetcher  
Approach: Uses NewsAPI to fetch 5 latest headlines, with category filter (e.g., sports, tech).  
Run: python news_fetcher.py` (needs API key)  
Example: Category: Sports → shows 5 headlines.  
Challenge: API setup & error handling.



5) Basic Expense Tracker with File Storage  
Approach: Extended Week 1 Budget Tracker. Saves income/expenses in CSV file and shows totals.  
Run: python expense_tracker.py`  
Example: Income 500, Expense 200 → Balance = 300.  
Challenge: Updating and reading CSV.