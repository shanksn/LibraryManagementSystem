# config.py - Python Logic Explanation

**File**: `config.py`
**Purpose**: Centralized configuration file for database credentials

---

## Overview

This file stores database connection settings in one place. All other Python files import these settings, demonstrating the CBSE principle of **modular programming** and **code reusability**.

---

## File Contents

```python
# Database Configuration File
# This file stores MySQL connection settings

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',  # Your MySQL password
    'database': 'library_management_system'
}
```

---

## What is a Dictionary?

```python
db_config = {...}
```

**Dictionary**: A Python data structure that stores key-value pairs

**Format**:
```python
{
    'key1': 'value1',
    'key2': 'value2'
}
```

**Accessing Values**:
```python
host_name = db_config['host']  # Returns 'localhost'
user_name = db_config['user']  # Returns 'root'
```

---

## Configuration Parameters

### 1. host
```python
'host': 'localhost'
```
- **Purpose**: MySQL server address
- **'localhost'**: Server running on same computer
- **Alternatives**: IP address (e.g., '192.168.1.100') for remote servers

### 2. user
```python
'user': 'root'
```
- **Purpose**: MySQL username
- **'root'**: Default MySQL administrator account
- **Production**: Should use specific user with limited permissions

### 3. password
```python
'password': 'invasion'
```
- **Purpose**: MySQL user password
- **Important**: This is your actual MySQL password
- **Security**: File should be in .gitignore (not pushed to GitHub)

### 4. database
```python
'database': 'library_management_system'
```
- **Purpose**: Name of the database to connect to
- Must match database created in setup_database.py

---

## Why Centralized Configuration?

### Problem Without config.py

**Bad Practice**: Hardcoding credentials in every file

```python
# login.py
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='invasion',
    database='library_management_system'
)

# admin.py
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='invasion',
    database='library_management_system'
)

# member.py
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='invasion',
    database='library_management_system'
)
```

**Problems**:
1. **Repetition**: Same code in 7+ files
2. **Maintenance**: Change password = update 7+ files
3. **Error-prone**: Easy to miss one file
4. **Version Control**: Password exposed in every file

---

### Solution With config.py

**Good Practice**: Import from one place

```python
# config.py
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',
    'database': 'library_management_system'
}

# login.py
from config import db_config
conn = mysql.connector.connect(**db_config)

# admin.py
from config import db_config
conn = mysql.connector.connect(**db_config)

# member.py
from config import db_config
conn = mysql.connector.connect(**db_config)
```

**Benefits**:
1. **Single Source of Truth**: One place to update
2. **Easy Maintenance**: Change once, applies everywhere
3. **Less Error-prone**: Can't forget to update
4. **Gitignore Compatible**: Only one file to exclude

---

## Dictionary Unpacking (`**`)

### What is `**db_config`?

```python
conn = mysql.connector.connect(**db_config)
```

The `**` operator **unpacks** the dictionary into keyword arguments.

### Example:

```python
# With dictionary unpacking
db_config = {'host': 'localhost', 'user': 'root', 'password': 'invasion', 'database': 'library_management_system'}
conn = mysql.connector.connect(**db_config)

# Equivalent to:
conn = mysql.connector.connect(host='localhost', user='root', password='invasion', database='library_management_system')
```

### How It Works:

**Step 1**: Dictionary
```python
db_config = {'host': 'localhost', 'user': 'root'}
```

**Step 2**: Unpack with `**`
```python
**db_config
```

**Step 3**: Becomes keyword arguments
```python
host='localhost', user='root'
```

---

## Usage in Project Files

### 1. login.py
```python
from config import db_config

def login():
    conn = mysql.connector.connect(**db_config)
    # ... rest of code
```

### 2. admin.py
```python
from config import db_config

def get_conn():
    return mysql.connector.connect(**db_config)
```

### 3. member.py
```python
from config import db_config

def get_conn():
    return mysql.connector.connect(**db_config)
```

### 4. add_member.py
```python
from config import db_config

def save():
    conn = mysql.connector.connect(**db_config)
    # ... rest of code
```

### 5. add_book.py
```python
from config import db_config

def save():
    conn = mysql.connector.connect(**db_config)
    # ... rest of code
```

---

## Git Workflow

### .gitignore File
```
# Local configuration
config.py
```

### config_template.py (For GitHub)
```python
# Database Configuration Template
# Copy this file to config.py and update with your MySQL credentials

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password_here',  # YOUR MYSQL PASSWORD
    'database': 'library_management_system'
}
```

### Setup Instructions (README.md)
```markdown
## Setup

1. Copy config_template.py to config.py:
   ```
   cp config_template.py config.py
   ```

2. Edit config.py with your MySQL password

3. Run setup_database.py
```

---

## CBSE Class XII Concepts Demonstrated

1. **Modular Programming**: Separating configuration from logic
2. **Dictionaries**: Key-value data structure
3. **Import Statement**: Using modules
4. **DRY Principle**: Don't Repeat Yourself
5. **Code Reusability**: One config used by all files
6. **Dictionary Unpacking**: `**` operator
7. **Best Practices**: Security and maintainability

---

## Security Considerations

### Current Implementation (Educational)
```python
'password': 'invasion'  # Plain text password
```
- ⚠️ Password visible in file
- ⚠️ File must be gitignored
- ✅ Acceptable for CBSE project

### Production Best Practices

#### 1. Environment Variables
```python
import os

db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'library_management_system')
}
```

**Set environment variables**:
```bash
export DB_PASSWORD="invasion"
```

#### 2. Config File with Encryption
```python
import keyring

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': keyring.get_password('library_app', 'mysql'),
    'database': 'library_management_system'
}
```

#### 3. Separate Credentials File
```python
# credentials.json (gitignored)
{
    "mysql": {
        "host": "localhost",
        "user": "root",
        "password": "invasion"
    }
}

# config.py
import json
with open('credentials.json') as f:
    creds = json.load(f)

db_config = {
    'host': creds['mysql']['host'],
    'user': creds['mysql']['user'],
    'password': creds['mysql']['password'],
    'database': 'library_management_system'
}
```

---

## Troubleshooting

### Error: "No module named 'config'"

**Cause**: config.py not in same directory

**Solution**:
1. Ensure config.py is in same folder as other Python files
2. Check file name is exactly `config.py` (not config.py.txt)

### Error: "Access denied for user 'root'@'localhost'"

**Cause**: Wrong password in config.py

**Solution**:
```python
'password': 'your_actual_mysql_password'
```

### Error: "Unknown database 'library_management_system'"

**Cause**: Database not created

**Solution**:
1. Run setup_database.py first
2. Or create database manually:
   ```sql
   CREATE DATABASE library_management_system;
   ```

---

## Testing Configuration

### Test Script (test_config.py)
```python
from config import db_config
import mysql.connector

try:
    conn = mysql.connector.connect(**db_config)
    print("✓ Successfully connected to MySQL")
    print(f"  Host: {db_config['host']}")
    print(f"  User: {db_config['user']}")
    print(f"  Database: {db_config['database']}")
    conn.close()
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

**Expected Output**:
```
✓ Successfully connected to MySQL
  Host: localhost
  User: root
  Database: library_management_system
```

---

## Alternative Configuration Styles

### 1. Separate Variables
```python
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'invasion'
DB_NAME = 'library_management_system'

# Usage:
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
```

### 2. Class-based Config
```python
class Config:
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'invasion'
    DB_NAME = 'library_management_system'

# Usage:
conn = mysql.connector.connect(
    host=Config.DB_HOST,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME
)
```

### 3. Current (Dictionary) - Best for CBSE
```python
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'invasion',
    'database': 'library_management_system'
}

# Usage:
conn = mysql.connector.connect(**db_config)
```

**Why Dictionary is Best**:
- Simple to understand
- Easy to unpack with `**`
- Demonstrates Python dictionaries
- CBSE-friendly syntax

---

## File Structure

```
library_app/
├── config.py               ← Database credentials (gitignored)
├── config_template.py      ← Template for GitHub
├── login.py               ← Imports config
├── admin.py               ← Imports config
├── member.py              ← Imports config
├── add_member.py          ← Imports config
├── add_book.py            ← Imports config
├── setup_database.py
├── .gitignore             ← Contains: config.py
└── README.md              ← Setup instructions
```

---

## Summary

**config.py** is a simple but powerful example of good software engineering:

✅ **Modular**: Separates configuration from logic
✅ **Maintainable**: Change once, applies everywhere
✅ **Reusable**: Used by all application files
✅ **Secure**: Can be gitignored easily
✅ **CBSE-Compliant**: Demonstrates import and dictionary concepts

**Key Concept**: This file demonstrates that good programming isn't just about writing code that works, but writing code that is easy to maintain and modify.
