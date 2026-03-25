# CYBS-GBG-F26A Programming Course

Welcome to your first programming course! 

## 📚 About This Course

This is where you'll find all the code examples from our programming classes. Each file contains examples and exercises to help you learn Python programming step by step.

- **Course**: Programming 1st Semester
- **Team**: CYBS-GBG-F26A
- **Language**: Python 3.8+
- **Instructor**: Alex 
- **Semester**: Spring 2026 (Forår 2026 - F26)

## 🚀 Getting Started

### What You Need
- Python 3.8 or newer installed on your computer
- A text editor (I recommend VS Code)

### Required Packages
Some exercises require additional Python packages. Install them using pip:

```bash
# For HTTP requests (011_req files)
pip install requests

# For MySQL database (011_db_mysql files)
pip install mysql-connector-python

# For HTML parsing (optional exercises)
pip install beautifulsoup4
```

To install all at once:
```bash
pip install requests mysql-connector-python beautifulsoup4
```

### How to Use These Files
1. **Download** or **clone** this repository to your computer
2. **Open** the Python files in your text editor
3. **Read** the code and comments carefully
4. **Run** the programs to see how they work
5. **Try** the exercises at the end of each file

### Running Python Programs
To run any `.py` file:
1. Open your terminal or command prompt
2. Navigate to the folder with the file
3. Type: `python filename.py` (replace `filename.py` with the actual file name)
4. Press Enter

Example:
```
python 001_first.py
```

### Understanding File Versions
Each topic has two versions:

- **Original Files** (e.g., `001_hello_world.py`): The instructor's condensed version used in class
- **Copilot Versions** (e.g., `001_hello_world_copilot_version.py`): Extended AI-generated versions with:
  - Detailed explanations and comments
  - Multiple examples for each concept
  - Practice exercises at the end
  - Challenge problems for advanced learners
  - Key takeaways and best practices

Both versions teach the same concepts - the copilot versions just provide more depth and practice opportunities!

## 📁 Course Files

Each file follows this naming pattern: `XXX_topic_name.py`

| File | Topic | What You'll Learn |
|------|-------|-------------------|
| [`001_hello_world.py`](001_hello_world.py) | Hello World | Your first Python program |
| [`001_hello_world_copilot_version.py`](001_hello_world_copilot_version.py) | Hello World (AI generated) | Extended version with detailed explanations and exercises |
| [`002_Variables_and_Datatypes_Primitives.py`](002_Variables_and_Datatypes_Primitives.py) | Variables & Data Types | Primitives and basic string operations |
| [`002_Variables_and_Datatypes_Primitives_copilot_version.py`](002_Variables_and_Datatypes_Primitives_copilot_version.py) | Variables & Data Types (AI generated) | Complete guide with examples and exercises |
| [`003_bool_list_tuple.py`](003_bool_list_tuple.py) | Booleans, Lists & Tuples | Boolean logic and sequence data types |
| [`003_bool_list_tuple_copilot_version.py`](003_bool_list_tuple_copilot_version.py) | Booleans, Lists & Tuples (AI generated) | Complete guide with examples and exercises |
| [`004_dict_set.py`](004_dict_set.py) | Dictionaries & Sets | Key-value pairs and unique collections |
| [`004_dict_set_copilot_version.py`](004_dict_set_copilot_version.py) | Dictionaries & Sets (AI generated) | Complete guide with examples and exercises |
| [`006_control_flows.py`](006_control_flows.py) | Control Flows | If statements, loops, and iteration |
| [`006_control_flows_copilot_version.py`](006_control_flows_copilot_version.py) | Control Flows (AI generated) | Complete guide with examples and exercises |
| [`007_func_exceptions.py`](007_func_exceptions.py) | Functions & Exceptions | Defining functions and error handling |
| [`007_func_exceptions_copilot_version.py`](007_func_exceptions_copilot_version.py) | Functions & Exceptions (AI generated) | Complete guide with examples and exercises |
| [`008_files.py`](008_files.py) | File Operations | Reading and writing files |
| [`008_files_copilot_version.py`](008_files_copilot_version.py) | File Operations (AI generated) | Complete guide with examples and exercises |
| [`009_json_csv.py`](009_json_csv.py) | JSON & CSV Files | Working with JSON and CSV data formats |
| [`009_json_csv_copilot_version.py`](009_json_csv_copilot_version.py) | JSON & CSV Files (AI generated) | Complete guide with examples and exercises |
| [`010_input_validation.py`](010_input_validation.py) | Input Validation | Validating and sanitizing user input |
| [`010_input_validation_copilot_version.py`](010_input_validation_copilot_version.py) | Input Validation (AI generated) | Complete guide with regex, security, and exercises |
| **011 - External Data & APIs** | | **Three-part module:** |
| [`011_req.py`](011_req.py) | └─ HTTP Requests | Making HTTP requests with the requests library |
| [`011_req_copilot_version.py`](011_req_copilot_version.py) | └─ HTTP Requests (AI generated) | Complete guide with API examples and exercises |
| [`011_db_sqlite.py`](011_db_sqlite.py) | └─ SQLite Database | Working with SQLite databases |
| [`011_db_sqlite_copilot_version.py`](011_db_sqlite_copilot_version.py) | └─ SQLite Database (AI generated) | Complete CRUD guide with security logging examples |
| [`011_db_mysql.py`](011_db_mysql.py) | └─ MySQL Database | Connecting to MySQL databases |
| [`011_db_mysql_copilot_version.py`](011_db_mysql_copilot_version.py) | └─ MySQL Database (AI generated) | Complete guide with connection pooling and exercises |


*More files will be added as we progress through the course!*

### Supporting Data Files
The repository also includes sample data files used in exercises:
- `alert.json`, `threat_intel.json`, `incident_report.json` - JSON examples
- `grades.csv`, `security_report.csv` - CSV examples  
- `my_file.txt`, `test.txt`, `numbers.txt` - Text file examples

## 💡 How to Learn Effectively

1. **Read First** - Always read through the code before running it
2. **Predict** - Try to guess what the code will do before running it
3. **Experiment** - Change things and see what happens
4. **Practice** - Complete the exercises in each file
5. **Ask Questions** - Don't hesitate to ask during class!

## 🆘 Getting Help

- **In Class**: Raise your hand and ask questions
- **Online**: Check the official Python documentation at [python.org](https://docs.python.org/3/)
- **ITSLearning**: Check course announcements and materials

## 📝 Tips for Success

- **Practice regularly** - Programming is learned by doing
- **Start small** - Don't try to write complex programs immediately
- **Read error messages** - They often tell you exactly what's wrong
- **Use meaningful names** - Choose variable names that describe what they store
- **Comment your code** - Explain what your code does in plain English

## 🎯 Learning Objectives

By the end of this course, you will be able to:
- Write basic Python programs
- Use variables and data types
- Get input from users and validate it
- Make decisions with if/else statements
- Repeat actions with loops
- Organize code with functions
- Handle errors gracefully with try/except
- Work with files (reading, writing, JSON, CSV)
- Use regular expressions for pattern matching
- Make HTTP requests to APIs
- Work with databases (SQLite and MySQL)
- Apply programming to cybersecurity scenarios

---

**Happy coding! Remember: every expert programmer started exactly where you are now.**
