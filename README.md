git # CLI Projects — Python Fundamentals

A collection of CLI projects built while learning Python fundamentals.

## Projects

### Unit Converter
Converts between km/m, celsius/fahrenheit, USD/NGN, kg/lbs
- Topics covered: Variables, data types, conditionals, Arithmetic operation
- Run: python unit_converter.py

### Calculator
- Uses: +. -, *, /, //, **, √
- Topics covered : Variables, Data types, conditionals, Arithmetic operation
- Used import math module
- Run: python calculator.py

### Solving quadratic equation
- Solves quadratic equations using the quadratic formula
- Topics covered : Variables, Data types, Arithmetic operation
- Used import math module
- Run: python solving_quadratic_equation.py

### Loan Evaluator
- Ask user for loan amount and amount payed, which is used to calculate the balance and percentage which is used in printing the output.
- Topics covered Variables, Data types, conditionals , conditional expression, Arithmetic operation.
- Run: python loan_evaluator.py

### Shopping Cart Program
- Asks user for item preffered to purchase and price, which is used to calculate the total price.
- Topics covered: Variables, data types, conditionals, arithmetic operations, while loops, lists, string methods.
- Run: python shopping_cart.py

### CLI Arithmetic Drill Trainer

A command-line math quiz game built in Python.
Choose your difficulty, answer 10 random math questions, 
and get a performance report at the end.

 Features
- Three difficulty levels: Easy, Medium, Hard
- Random questions using addition, subtraction, multiplication and division
- Tracks correct and wrong answers per session
- Times each question and calculates average response time
- Shows wrong answers with correct solutions at end of session

 How To Run
python arithmetic_drill.py

 How It Works
1. Choose difficulty (easy / medium / hard)
2. Answer 10 randomly generated math questions
3. See your score, accuracy and average response time
4. Review questions you got wrong

 Difficulty Levels
| Level | Number Range |
|-------|-------------|
| Easy | 1 - 10 |
| Medium | 1 - 100 |
| Hard | 1 - 1000 |

 Topics Covered
- Control flow (if/elif/else)
- Loops (for loop)
- Random module
- Time module
- Input validation

 Project Status:
Built during Python fundamentals learning phase.
Refactor planned after learning functions.

### Personal Profile Card Generator

A command-line Python program that generates a formatted 
profile card using functions.

  Features
- Displays full name with optional title
- Shows age, country and hobbies
- Lists skills with proficiency levels

 How To Run
python profile_card.py

 Example Output
===== PROFILE CARD =====
Name: Dr. Elizabeth Smith
------------------------
Age: 17 | Country: France
Hobbies: cooking, music, reading
------------------------
Skills:
  - Python: Beginner
  - Github: Beginner
  - Vscode: Beginner
===============================

Topics covered
- Functions
- lists
- String methods
- Conditionals

  ### Arithmetic Drill Trainer CLI v2
  Refactored using functions after completing functions topic.

### Personal Finance Tracker CLI

A command-line budget management tool built in Python.  
Set spending limits per category, log income and expenses,  
and get a full financial breakdown with savings rate tracking.


  Features

- Set custom budget limits across 8 spending categories
- Log income and expense transactions with descriptions
- View running balance (income, expenses, net)
- Full transaction history with type, category, and amount
- Spending breakdown by category with percentage of total expenses
- Over-budget alerts per category
- Savings rate calculation as a percentage of income


 How To Run

python finance_tracker.py

  How It Works

1. Set your budget limits for each category at startup
2. Choose an action from the menu (add transaction, view balance, etc.)
3. Log income or expense transactions with category and description
4. View your balance, history, or full breakdown at any time
5. Exit when done — session data is not persisted between runs



 Menu Options

| Option | Action |
|--------|--------|
| 1 | Add a transaction |
| 2 | Show balance |
| 3 | Show transaction history |
| 4 | Show spending breakdown |
| 5 | Quit |



 Budget Categories

| Category | Description |
|----------|-------------|
| Housing | Rent, mortgage |
| Utilities | Electric, water, internet |
| Transportation | Fuel, transit, car payments |
| Food | Groceries, dining |
| Health | Medical, pharmacy |
| Personal Care | Hygiene, grooming |
| Lifestyle | Clothing, subscriptions |
| Leisure | Entertainment, hobbies |



  Topics Covered

- Functions and modular code structure
- Dictionaries and lists
- Loops and conditionals
- Input validation and type casting
- Basic financial logic (balance, savings rate, category totals)



  Known Limitations

- Data is not saved — all transactions are lost when the program exits
- No input validation on transaction type or category name (typos will break logic)
- Budget categories are fixed at startup and cannot be edited mid-session

### Student Course Manager
   This is an exercise containing three university department, each with a list of enrolled students.
  
  Task Covered
- Find students enrolled in ALL three departments simultaneously
- Find students enrolled in computer science OR medicine but not both
- Find students enrolled in computer science but NOT in engineering
- Find students enrolled in at least one department (all unique students)
- Find students enrolled in exactly one department only (not in any overlap)
- Check if medicine and engineering share any students — print True or False
- Add "Blessing" to computer science, remove "Bob" from medicine
- Find all students NOT in computer science from the full student population

Topics Covered
- Sets
- Conditional expression

How To Run
python student_course_manager.py


### Student Performance Analyzer CLI

A command-line student performance analysis tool built in Python.

Input student grades across multiple subjects and get a full performance breakdown including rankings, weighted GPA, and subject-level insights.

Features
- Stores multiple students with multiple subject grades
- Computes per-student average, median, highest, lowest score and pass/fail status
- Ranks students on a leaderboard with a visual bar chart
- Calculates weighted GPA with subject-specific credit points
- Identifies students failing 2 or more subjects using sets
- Shows class average per subject
- Flags subjects where the majority of students are failing

How To Run

python student_performance_analyzer.py


How It Works
1. Choose an option from the menu
2. View students failing 2+ subjects
3. View subject averages and flagged subjects
4. View the full ranked leaderboard with stats

Menu Options
| Option | Description |
|--------|-------------|
| 1 | Show failing students |
| 2 | Show subject averages and flagged subjects |
| 3 | Show ranked leaderboard |
| 4 | Quit |

Topics Covered
- Data structures (dicts, lists, sets)
- Functions and modular design
- Sorting with lambda
- String formatting and f-strings
- Manual mean, median and weighted GPA calculation

Project Status:
Built during Python fundamentals learning phase as a data structures capstone project.




