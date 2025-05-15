# ✅ Codveda Internship - Level 2 Task 1: To-Do List CLI App


This is a command-line Python application that allows users to manage a to-do list. Users can add tasks, view them, mark them as completed, and delete them. All tasks are saved in a JSON file so they persist between runs.

---

## 🧠 Features

- ➕ Add tasks
- 📋 View all tasks with completion status
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Save/load tasks from `tasks.json`
- ⚠️ Error handling (invalid task numbers, input, etc.)

---
## 📋 Sample Menu Output
📝 To-Do List Menu
1. Add Task
2. View Tasks
3. Mark as Done
4. Delete Task
5. Exit

## 📄 Sample Usage
Enter your choice (1-5): 1
Enter task: Complete Codveda Task 1
✅ Task added.

Enter your choice (1-5): 2
1. Complete Codveda Task 1 [❌]

Enter your choice (1-5): 3
Enter task number to mark as done: 1
🎉 Task marked as completed.

Enter your choice (1-5): 2
1. Complete Codveda Task 1 [✅]

## 🗃️ File Structure
todo_cli.py       # Main application
tasks.json        # Stores the to-do list between sessions

## 🛠️ Requirements
Python 3.x
No external libraries required (json and os are built-in)

## 📌 Notes
You can reset your to-do list by deleting or clearing the tasks.json file.
This is a CLI-only application for demonstration purposes.

## 🔗 Author
This project is part of my internship tasks at Codveda Technology.
#CodvedaJourney #CodvedaExperience #FutureWithCodveda

---

## ✅ Level 2 - Task 2: Web Scraper

This Python script scrapes data (e.g., article titles) from a website and saves the results into a CSV file using `requests`, `BeautifulSoup`, and `csv`.

---

### 🧠 Features

- Scrapes article titles from a target website
- Saves the results into `scraped_data.csv`
- Uses basic HTML parsing with BeautifulSoup
- Handles failed web requests

---

## Make sure requests and beautifulsoup4 are installed:

pip install requests beautifulsoup4

## 📁 Output File Example
scraped_data.csv

| Title                          |
|--------------------------------|
| OpenAI launches new model...  |
| Python 3.12 released...        |
| ...                            |

## 🛠️ Customization
You can change the url and tag selectors inside the script to scrape data from other pages (e.g., product listings, news headlines, blog posts).

## 📌 Notes
Web scraping must comply with website terms of service.
Not all websites allow scraping — always test responsibly.

---

## ✅ Level 2 - Task 3: API Integration (Cryptocurrency Price Checker)

This Python script fetches the current price of any cryptocurrency (e.g., Bitcoin, Ethereum, Dogecoin) in **Indian Rupees (INR)** using the **CoinGecko API**.

---

### 🧠 Features

- Accepts user input for the cryptocurrency name
- Fetches live price from CoinGecko's public API
- Displays price in INR (₹)
- Handles invalid coin names and network/API errors

---
## Example:

Enter cryptocurrency (e.g., bitcoin, ethereum): bitcoin
💰 Current price of Bitcoin: ₹5672341

## ⚙️ Dependencies
pip install requests

## 📌 Notes
No API key required (CoinGecko is public & free)

Supported coins: bitcoin, ethereum, dogecoin, litecoin, etc.

Output is fetched in real-time using the endpoint:
https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr

## 🔗 Author
This project is part of my internship tasks at Codveda Technology.
#CodvedaJourney #CodvedaExperience #FutureWithCodveda

### 💻 How to Run

```bash
python crypto_price.py

python web_scraper.py

python todo_cli.py

