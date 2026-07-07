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

### phone_object_practice
An exercise used to practice classes, objects, and methods for the first time

How It Works

It has a module name pop_module which contain the class and the methods used by the objects to call and perform the functions of the method and the class

How To Run

python phone_object_practice.py

Topics Covered
- Classes
- Objects
- Functions

### Employee_information
An exercise used to practice class variables and instance variables

How To Run 

python employee_information.py

Topics Covered
- Classes
- Objects
- Functions
- Format specifiers

### Bank Account System
This is a project built like a real bank account, which contains withdraw, deposit, the ability to check balance and also get account info printed.

How It Works
- It contians a general bank account, savings account, and a student account
- Student account has a withrawal limit of $100
- Savings account can get an interest
- Currency is in USD

How To Run

python bank_account_system.py

Topics Covered
- Classes
- Objects
- inheritance
- Encapsulation
- Access modifiers
- Error Handling

### Payment Processing System

This is a payment processing system built using Object-Oriented Programming principles. It allows users to create different payment methods, add them to a transaction, process payments, and generate receipts.

How It Works

Contains multiple payment types:

  - Credit Card Payment
  - PayPal Payment
  - Crypto Payment
  - Bank Transfer
- Uses an abstract base class to enforce a common payment interface
- Each payment type implements its own processing and receipt generation logic
- Sensitive information such as card numbers and bank account numbers are masked
- Multiple payments can be grouped into a single transaction
- Transactions can be combined together using operator overloading
- Total transaction amount is calculated automatically

Features

- Add payments through a command-line interface
- View all payments in a transaction
- Process all payments at once
- Generate receipts for every payment
- Calculate total transaction value
- Count payments using - len()
- Combine transactions using the - + operator

How To Run


python payment_system.py

Topics Covered

- Classes
- Objects
- Abstract Classes
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation
- Method Overriding
- Operator Overloading
- Special Methods
- Type Hints
- Collections
- Command Line Interfaces (CLI)
- Data Masking
- Object Aggregation

### Bank Account Simulator CLI

This is a console-based banking system built with Python using Object-Oriented Programming (OOP) principles. The application simulates basic banking operations such as creating accounts, making deposits, withdrawing funds, transferring money between accounts, and viewing account information.

How It Works

- Supports both Checking Accounts and Savings Accounts
- Users can create multiple accounts through a menu-driven interface
- Funds can be deposited into and withdrawn from accounts
- Money can be transferred between accounts
- Savings accounts can calculate both **simple interest** and **compound interest**
- Interest projections can be viewed for different time periods
- The bank can generate a report showing total assets across all accounts
- Currency is represented in USD ($)

Features

- Open new accounts
- Deposit funds
- Withdraw funds
- Transfer money between accounts
- View account details
- View all accounts
- Interest projection for savings accounts
- Bank-wide asset reports

How To Run


python bank_account_simulator_cli.py

Topics Covered

- Classes and Objects
- Inheritance
- Encapsulation
- Method Overriding
- Properties (@property)
- Exception Handling
- Composition
- Polymorphism
- Object-Oriented Programming (OOP)

Example Concepts Demonstrated

- A Bank object manages multiple accounts
- A SavingsAccount inherits from the base Account class
- Account balances are protected using encapsulation
- Transactions are validated using error handling
- Different account types share common behavior while implementing specialized functionality

Future Improvements

- Transaction history
- Account deletion
- Data persistence using JSON files
- Custom savings account interest rates
- Unit testing
- Account authentication and security features


### Personal Journal CLI

This is a console-based journal application built with Python. The program allows users to write journal entries, read previously saved entries, count the total number of entries, and clear the journal through a simple menu-driven command-line interface.

How It Works

- Journal entries are stored in a text file named 'journal.txt'
- Users can create new journal entries through the console
- Each entry is automatically numbered
- Existing journal entries can be viewed at any time
- The application keeps track of the total number of entries
- Users can clear all journal entries with a confirmation prompt
- File operations are handled using Python's built-in file handling features

Features

- Write journal entries
- Read all journal entries
- Count total entries
- Clear journal contents
- Automatic entry numbering
- File persistence using a text file
- Error handling for missing files
- Menu-driven interface

How To Run


python personal_journal_cli.py


Topics Covered

- File Handling
- Reading Files
- Writing Files
- Appending Data to Files
- Exception Handling
- Functions
- Loops
- Conditional Statements
- User Input
- Command-Line Applications

Example Concepts Demonstrated

- Reading data from a text file using open()
- Writing and appending journal entries to a file
- Handling missing files with try and except
- Counting entries by iterating through file contents
- Creating a menu-driven CLI application
- Managing application flow using loops and functions
- Confirming destructive actions before deleting data

Future Improvements

- Add timestamps to journal entries
- Search journal entries by keyword
- Edit existing entries
- Delete individual entries
- Export journal entries to other file formats
- Password-protected journals
- Categorize entries with tags
- Store entries using JSON or a database
- Unit testing
- Enhanced user interface

### Student Grade Tracker CLI

This is a console-based student grade management application built with Python. The program allows users to store, manage, search, and delete student academic records while automatically saving data to a CSV file for persistence.

How It Works

- Student records are stored in a CSV file named 'grades.csv'
- Users can add student information through a menu-driven interface
- Each student record contains scores for Mathematics, English, and Science
- Student data is automatically saved after additions and deletions
- Users can search for specific students by name
- Student records can be removed from the system
- The application calculates and displays each student's average score
- Data remains available between program sessions through CSV storage

Features

- Add student records
- View all student records
- Search for a student by name
- Delete student records
- Automatic average score calculation
- Persistent data storage using CSV files
- Automatic file loading on startup
- Menu-driven command-line interface
- Error handling for missing files

How To Run


python student_grade_tracker.py


Topics Covered

- File Handling
- CSV File Processing
- Reading and Writing CSV Files
- Dictionaries
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling
- Data Persistence
- User Input Validation
- Command-Line Applications

Example Concepts Demonstrated

- Loading structured data from a CSV file using 'csv.DictReader'
- Saving data using 'csv.DictWriter'
- Storing student information as dictionaries
- Managing collections of records with lists
- Calculating student averages from subject scores
- Searching through datasets using iteration
- Deleting records from a collection
- Persisting application data between program executions
- Handling missing files with exception handling

CSV Structure

The application stores data in the following format:

| Name  | Math | English | Science |
| ----- | ---- | ------- | ------- |
| Jenny | 85   | 92      | 88      |
| David | 78   | 81      | 90      |

Future Improvements

- Edit existing student records
- Calculate class-wide statistics
- Display highest and lowest scores
- Generate student report cards
- Sort students by average score
- Export reports to PDF
- Add grade classifications (A, B, C, etc.)
- Input validation for score ranges
- Support additional subjects
- Unit testing
- Graphical User Interface (GUI)
- Student ranking system


### Expense Report System CLI

This is a console-based personal finance management system built with Python. The application allows users to track income and expenses, manage category-based budgets, analyze spending habits, generate financial reports, and monitor savings performance through a menu-driven command-line interface.

The system stores transaction data in CSV format and budget settings in JSON format, providing persistent storage between sessions while maintaining data integrity through validation and error handling.

How It Works

* Income and expense transactions are recorded and stored in a CSV file
* Budget limits are managed separately using a JSON configuration file
* Transactions are categorized to enable spending analysis and budget tracking
* The system automatically calculates balances, expenses, income, and savings rates
* Users can review complete transaction histories
* Spending can be analyzed by category and compared against budget limits
* Monthly spending trends can be compared to identify financial patterns
* Reports can be exported based on categories or date ranges
* Duplicate transaction detection helps maintain data accuracy
* Financial data persists between program sessions

Features

* Add income and expense transactions
* View complete transaction history
* Track total income, expenses, and balance
* Create and manage category-based budgets
* Monitor budget overruns
* Analyze spending by category
* Calculate savings rate automatically
* Compare spending across months
* Calculate average daily spending
* Detect duplicate transactions
* Export filtered financial reports
* Store transaction data using CSV files
* Store budget settings using JSON files
* Data validation and error handling
* Menu-driven command-line interface

Financial Categories

The application supports budgeting and expense tracking for the following categories:

* Housing
* Utilities
* Transportation
* Food
* Health
* Personal Care
* Lifestyle
* Leisure

How To Run


python expense_system.py


# Data Storage


Transactions File

All transactions are stored in:


transactions.csv


Example structure:

| Transaction Type | Category | Amount  | Description | Date       |
| ---------------- | -------- | ------- | ----------- | ---------- |
| income           | salary   | 2500.00 | paycheck    | 2026-01-01 |
| expenses         | food     | 25.50   | lunch       | 2026-01-02 |

Budget File

Budget limits are stored in:


budget.json


Example structure:


{
  "housing": 1000,
  "food": 400,
  "transportation": 200,
  "utilities": 150
}

Topics Covered

* File Handling
* CSV Processing
* JSON Serialization
* Dictionaries
* Lists
* Functions
* Exception Handling
* Data Validation
* Financial Calculations
* Date and Time Handling
* Data Persistence
* Report Generation
* Budget Management
* Statistical Analysis
* Command-Line Applications

Example Concepts Demonstrated

* Reading and writing structured CSV data using 'csv.DictReader' and 'csv.DictWriter'
* Persisting application settings using JSON
* Implementing robust error handling for corrupted or missing files
* Validating user input before processing financial data
* Calculating balances from income and expense records
* Computing savings rates and spending percentages
* Aggregating financial data by category and month
* Detecting duplicate records using composite keys
* Generating custom reports based on filters
* Working with dates using Python's 'datetime' module
* Managing application state across multiple program executions

# Financial Analytics Included

Balance Tracking

The system automatically calculates:

* Total Income
* Total Expenses
* Current Balance

Spending Breakdown

Users can view:

* Category spending totals
* Percentage of total expenses by category
* Budget overages by category

Savings Rate Analysis

The application calculates:


(Total Income - Total Expenses) / Total Income × 100

to determine the user's savings rate.

Monthly Spending Comparison

The system compares spending between the two most recent months and reports:

* Spending increases
* Spending decreases
* Percentage change

Average Daily Spending

The application calculates average spending per day based on recorded expense activity.

Report Exporting

Users can generate detailed text reports filtered by:

* Category
* Date Range

Generated reports include:

* Transaction details
* Income totals
* Expense totals
* Date information
* Category summaries


Reports are automatically timestamped to prevent accidental overwrites.

Error Handling

The application includes protection against:

* Missing transaction files
* Missing budget files
* Corrupted JSON data
* Invalid CSV records
* Invalid transaction amounts
* Invalid date formats
* Empty datasets
* Division-by-zero calculations
* Failed file operations

Future Improvements

* Transaction editing functionality
* Transaction deletion functionality
* Recurring income and expense tracking
* Financial goal tracking
* Savings target projections
* Budget recommendation engine
* Data visualization with charts and graphs
* Monthly and yearly financial summaries
* Multi-user support
* Currency selection
* Import and export to Excel
* SQLite database integration
* Unit testing
* Graphical User Interface (GUI)
* Authentication and account security

Learning Outcomes

This project demonstrates how to build a real-world finance application using Python while applying concepts such as file persistence, data validation, financial calculations, reporting systems, exception handling, and modular program design.

It serves as an excellent intermediate-level Python project that bridges the gap between basic CRUD applications and more advanced data-driven software systems.


### Weather API Retry Simulator CLI

This is a console-based weather service simulator built with Python. The application simulates interactions with an external weather API while demonstrating robust error handling, retry mechanisms, logging, and session analytics.

The program randomly generates successful responses and various types of failures to mimic real-world API behavior, allowing users to explore how resilient applications handle unreliable external services.

How It Works

- Users enter the name of a city to request weather information
- The application simulates an API call using randomized outcomes
- Requests may succeed or fail with different types of errors
- Network-related failures are automatically retried
- Data-related failures terminate the request immediately
- All errors are recorded in a log file for debugging purposes
- Session statistics are collected throughout program execution
- A final report summarizes system performance and reliability metrics

Features

- Simulated weather API requests
- Randomized success and failure responses
- Automatic retry mechanism
- Error categorization
- Exception handling
- Error logging to file
- Session performance tracking
- Success rate calculations
- Retry statistics
- Failure analysis
- Interactive command-line interface

Error Types Simulated

The application simulates several common API failure scenarios:

- Connection errors
- Timeout errors
- Invalid data errors
- Missing data errors
- Successful API responses

Retry Strategy

The application implements a retry policy for temporary failures:

- Connection errors are retried automatically
- Timeout errors are retried automatically
- A maximum of three attempts is allowed
- Invalid data errors immediately terminate processing
- Missing field errors immediately terminate processing

How To Run


python weather_retry_simulator.py


Example Successful Response


----------Weather Forecast-----------

City : London

Temperature : 24

Condition : Windy

Humidity : 0.2

Example Failed Response


Attempt 1 failed. Retrying...

Attempt 2 failed. Retrying...

There is an error with the server.

Unable to get weather details


Session Analytics

At the end of execution, the application generates a session report containing:

- Total API calls
- Successful requests
- Success rate percentage
- Average retry count
- Most common failure type
- Failure breakdown statistics

Example:


--------- Session Report ---------

Total API Calls: 25

Successful Requests: 10

Success Rate: 40.00%

Average Retries Before Success: 1.30

Most Common Failure Type: ConnectionError

Failure Breakdown:

ConnectionError: 8

TimeoutError: 4

ValueError: 2


Logging

All errors are automatically written to:


error.log


Example log entry:


2026-06-26 18:45:12 - ERROR - Attempt 2 - ConnectionError:
Could not connect to the weather service


Topics Covered

- Exception Handling
- Custom Retry Logic
- Error Recovery
- Logging
- Random Simulation
- Dictionaries
- Lists
- Functions
- Global State Management
- Statistical Analysis
- Command-Line Applications
- API Simulation
- Defensive Programming

Example Concepts Demonstrated

- Simulating external API behavior using random outcomes
- Handling multiple exception types
- Implementing retry mechanisms for transient failures
- Logging application errors using Python's logging module
- Tracking application performance metrics
- Calculating success rates and averages
- Categorizing and aggregating failures
- Using dictionaries for statistical analysis
- Building resilient systems that recover from temporary failures
- Separating recoverable and unrecoverable errors

Software Engineering Concepts Demonstrated

This project demonstrates several patterns commonly used in production systems:

- Retry Pattern
- Fail Fast Principle
- Error Classification
- Fault Tolerance
- Logging and Monitoring
- Reliability Metrics
- Performance Analytics
- Defensive Programming

Future Improvements

- Exponential backoff retry strategy
- Configurable retry limits
- Real weather API integration
- Response caching
- Circuit breaker pattern implementation
- Custom exception classes
- Multi-city batch requests
- Report export functionality
- Graphical performance dashboards
- Unit testing
- Asynchronous API requests
- API response time tracking

Learning Outcomes

This project demonstrates how to build resilient software systems that can tolerate failures when communicating with external services. It introduces concepts commonly used in backend engineering, cloud systems, and API development, including retry strategies, error logging, fault tolerance, and performance monitoring.

It serves as an excellent intermediate Python project for understanding how real-world applications handle unreliable external dependencies.



### Course Statistics API Client

This is a Python-based API client application that retrieves and processes course statistics data from the University of Helsinki's mock statistics API. The program demonstrates how to consume REST APIs, parse JSON responses, filter data, and perform statistical calculations.

The application provides two main functionalities: retrieving a list of active courses and generating statistical summaries for individual courses.

How It Works

* The application connects to the University of Helsinki mock statistics API
* Course data is retrieved using HTTP requests
* JSON responses are parsed into Python data structures
* Only active courses are returned when retrieving all courses
* Course statistics are aggregated across multiple weeks
* Various metrics, such as total exercises and average hours per student, are calculated
* SSL certificate verification is handled using the `certifi` package

Features

* Retrieve all active courses
* Filter inactive courses automatically
* Calculate total exercises for each course
* Retrieve detailed statistics for a specific course
* Calculate total study hours
* Calculate total completed exercises
* Determine the maximum number of enrolled students
* Calculate average study hours per student
* Calculate average exercises completed per student
* Process and analyze JSON API responses

How To Run


python course_statistics_api.py


Example Output

Retrieving Active Courses



[
    ('Full Stack Open 2019', 'ofs2019', 2019, 165),
    ('Docker 2019', 'docker2019', 2019, 36)
]


Retrieving Course Statistics


{
    'weeks': 8,
    'students': 220,
    'hours': 6730,
    'hours_average': 30,
    'exercises': 15230,
    'exercises_average': 69
}


Topics Covered

* REST APIs
* HTTP Requests
* JSON Processing
* Data Aggregation
* Statistical Calculations
* List Comprehensions
* Dictionaries
* Tuples
* Functions
* String Formatting
* SSL Certificate Verification
* External Libraries

Example Concepts Demonstrated

* Making HTTP requests using 'urllib.request'
* Parsing JSON responses using Python's 'json' module
* Working with external APIs
* Filtering data based on specific conditions
* Performing aggregate calculations on datasets
* Using generator expressions
* Computing averages and totals
* Finding maximum values in collections
* Structuring data using tuples and dictionaries
* Handling secure HTTPS connections using 'certifi'

API Endpoints Used

Retrieve All Courses

https://studies.cs.helsinki.fi/stats-mock/api/courses


Returns information about all available courses, including whether they are currently active.

Retrieve Course Statistics


https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats


Returns weekly statistics for a specific course.


Statistical Metrics Calculated

For each course, the application calculates:

* Number of weeks
* Maximum number of enrolled students
* Total study hours
* Average study hours per student
* Total completed exercises
* Average exercises completed per student

Learning Outcomes

This project demonstrates how to interact with REST APIs using Python while applying concepts such as JSON parsing, data filtering, aggregation, and statistical analysis. It provides practical experience with external data sources and illustrates how Python can be used to transform raw API responses into meaningful information.

It serves as an excellent introductory project for learning API consumption, data processing, and basic analytics in Python.


### String Manipulation Utilities

This is a small Python utility module that demonstrates common string manipulation techniques. The program provides functions for changing character case, splitting strings into equal parts, and removing special characters from text.

How It Works

* The application accepts a string as input
* Character cases can be swapped from uppercase to lowercase and vice versa
* Strings can be split into two halves
* Special characters and punctuation can be removed while preserving letters, numbers, and spaces

Features

* Change the case of characters
* Split strings into two parts
* Remove special characters
* Preserve alphanumeric characters and spaces

### How To Run



python string_utilities.py


Topics Covered

* Strings
* String Methods
* String Slicing
* Loops
* Conditional Statements
* Lists
* Functions

Example Concepts Demonstrated

* Using Python's 'swapcase()' method
* Splitting strings with slicing operations
* Iterating through characters in a string
* Validating characters with 'isalpha()' and 'isdigit()'
* Building and joining lists of characters
* Processing and cleaning text data

Example Output


MEAn
('I feel so', ' happy today')
This is a test lets see how it goes11


Learning Outcomes


This project demonstrates fundamental string processing techniques in Python and provides practical experience with text manipulation, character validation, and string operations.


### File System Analyzer CLI

This is a console-based file system analysis tool built with Python. The application scans a user-specified folder, analyzes its files, groups them by extension, identifies old and duplicate files, and exports a detailed CSV report.

The project demonstrates how Python's standard library can be used to automate file system inspection and generate useful reports without relying on external packages.

### How It Works

* The user provides a folder path as a command-line argument
* The application scans all files in the specified folder
* Files are grouped according to their extensions
* The total size of each file type is calculated
* Files older than 30 days are identified
* Duplicate files are detected based on filename and file size
* A summary report is displayed in the terminal
* A detailed CSV report is generated inside the scanned folder

### Features

* Analyze files in any folder
* Group files by extension
* Calculate total storage used by each file type
* Detect files older than 30 days
* Identify duplicate files
* Display a formatted console report
* Export analysis results to a CSV file
* Human-readable file size formatting
* Command-line interface using arguments
* File system validation and error handling

### How To Run

```bash
python file_system_analyzer.py <folder_path>
```

Example:

```bash
python file_system_analyzer.py Documents
```

### Report Sections

The generated report contains three sections:

* **Extension Summary** – File extensions, file counts, and total storage used
* **Old Files** – Files older than 30 days, including last modified date and age
* **Duplicate Files** – Duplicate filenames, file sizes, and their locations

The report is saved as:

```text
file_system_report.csv
```

### Topics Covered

* Modules and Libraries
* Command-Line Arguments
* File System Operations
* CSV File Handling
* Date and Time
* Dictionaries
* Lists
* Functions
* Error Handling
* Data Aggregation
* Report Generation

### Standard Library Modules Used

* `argparse` – Parse command-line arguments
* `pathlib` – Navigate and inspect the file system
* `collections.defaultdict` – Group duplicate files efficiently
* `datetime` – Calculate file ages
* `csv` – Export analysis reports
* `sys` – Handle program termination and errors

### Example Concepts Demonstrated

* Parsing command-line arguments with `argparse`
* Traversing directories using `pathlib`
* Grouping data with dictionaries and `defaultdict`
* Reading file metadata
* Calculating file ages from timestamps
* Formatting file sizes into human-readable units
* Detecting duplicate files using composite keys
* Generating structured CSV reports
* Validating user input and file paths
* Building a complete command-line utility

### Learning Outcomes

This project demonstrates how to combine multiple Python standard library modules to build a practical file management application. It provides experience with command-line programming, file system navigation, data aggregation, report generation, and working with file metadata while reinforcing modular program design and problem-solving skills.





  




