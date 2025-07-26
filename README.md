# 💰 Expense Tracker CLI

A simple command-line application to track and manage your daily expenses.  
Built using Python with a focus on logic building, CLI interaction, and filesystem handling.

---

## 🚀 Features

- Add new expenses with description and amount
- Update or delete existing expenses by ID
- View all expenses in a formatted list
- View total expenses
- View monthly expense summaries (filtered by month)
- Data stored locally in a JSON file

---

## 🛠️ How to Use

### ▶️ Run from terminal:

```bash
python tracker.py <command> [options]
````

---

## 📋 Available Commands

### ➕ Add a New Expense

```bash
python tracker.py add --description "Lunch" --amount 20
```

### 📝 Update an Expense

```bash
python tracker.py update --id 2 --description "Snacks" --amount 15
```

### ❌ Delete an Expense

```bash
python tracker.py delete --id 2
```

### 📄 List All Expenses

```bash
python tracker.py list
```

### 📊 Total Summary of All Expenses

```bash
python tracker.py summary
```

### 📅 Summary for a Specific Month

```bash
python tracker.py summary --month 8
```

---

## 🧠 Internals

* Expenses are saved in a file called `expenses.json`
* Each record includes:

  * `id`: unique number
  * `date`: auto-generated in `YYYY-MM-DD` format
  * `description`: what the money was spent on
  * `amount`: how much was spent

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required

---

## ✅ Example Output

```bash
$ python tracker.py list

ID   Date         Description     Amount
1    2025-07-27    Lunch           $20.00
2    2025-07-27    Snacks          $15.00
```

---

## 🧑‍💻 Author

Azmeer Hassan Ammad
Beginner Python Developer 

```

---

