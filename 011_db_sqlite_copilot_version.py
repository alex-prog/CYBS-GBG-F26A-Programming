"""
011 - SQLite Database: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the SQLite Database exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Connect to SQLite databases
- Create tables with SQL
- Insert, select, update, and delete data (CRUD operations)
- Use parameterized queries to prevent SQL injection
- Work with cursors and connections
- Apply database concepts to cybersecurity logging

"""

import sqlite3
from datetime import datetime


# ============================================================================
# PART 1: Connecting to SQLite Database
# ============================================================================
# SQLite is a file-based database (no server required)
# If the database file doesn't exist, it will be created

print("=== PART 1: Database Connection ===\n")

# Connect to database (creates 'security.db' if it doesn't exist)
conn = sqlite3.connect('security.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

print(f"Cursor object: {cursor}")
print(f"Connection object: {conn}")
print("Connected to security.db successfully!")

print()


# ============================================================================
# PART 2: Creating Tables
# ============================================================================
# SQL CREATE TABLE statement defines table structure
# Use IF NOT EXISTS to avoid errors if table already exists

print("=== PART 2: Creating Tables ===\n")

# Create security events table
create_table_query = '''
CREATE TABLE IF NOT EXISTS security_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    event_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    source_ip TEXT,
    description TEXT
)
'''

cursor.execute(create_table_query)
print("Table 'security_events' created successfully!")

# Create users table
create_users_query = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    email TEXT,
    role TEXT,
    created_at TEXT
)
'''

cursor.execute(create_users_query)
print("Table 'users' created successfully!")

# Commit changes to save them
conn.commit()

print()


# ============================================================================
# PART 3: Inserting Data (CREATE in CRUD)
# ============================================================================
# Use parameterized queries (?) to prevent SQL injection
# NEVER use string formatting with user input!

print("=== PART 3: Inserting Data ===\n")

# Insert single record
insert_event_query = '''
INSERT INTO security_events (timestamp, event_type, severity, source_ip, description)
VALUES (?, ?, ?, ?, ?)
'''

event_data = (
    '2026-03-25 10:30:00',
    'login_attempt',
    'medium',
    '192.168.1.100',
    'Failed login attempt for user admin'
)

cursor.execute(insert_event_query, event_data)
print("Inserted security event")

# Insert multiple records
insert_user_query = '''
INSERT INTO users (user_id, username, email, role, created_at)
VALUES (?, ?, ?, ?, ?)
'''

users_data = [
    (1, 'alice', 'alice@company.com', 'admin', '2026-01-15'),
    (2, 'bob', 'bob@company.com', 'analyst', '2026-02-20'),
    (3, 'charlie', 'charlie@company.com', 'user', '2026-03-10'),
]

cursor.executemany(insert_user_query, users_data)
print(f"Inserted {cursor.rowcount} users")

# IMPORTANT: Commit to save changes
conn.commit()

print()


# ============================================================================
# PART 4: Selecting Data (READ in CRUD)
# ============================================================================
# SELECT retrieves data from tables
# Use fetchall(), fetchone(), or fetchmany() to get results

print("=== PART 4: Selecting Data ===\n")

# Select all users
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()

print("All users:")
for user in all_users:
    print(f"  ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Role: {user[3]}")

print()

# Select specific columns with WHERE clause
cursor.execute('SELECT username, role FROM users WHERE role = ?', ('admin',))
admins = cursor.fetchall()

print("Admin users:")
for admin in admins:
    print(f"  {admin[0]} - {admin[1]}")

print()

# Select with ORDER BY and LIMIT
cursor.execute('SELECT username, email FROM users ORDER BY username LIMIT 2')
first_two = cursor.fetchall()

print("First 2 users (alphabetically):")
for user in first_two:
    print(f"  {user[0]}: {user[1]}")

print()


# ============================================================================
# PART 5: fetchone() vs fetchall()
# ============================================================================
# Different methods for retrieving query results

print("=== PART 5: Fetch Methods ===\n")

# fetchone() - returns single row (or None if no results)
cursor.execute('SELECT * FROM users WHERE user_id = ?', (2,))
single_user = cursor.fetchone()

if single_user:
    print(f"User ID 2: {single_user[1]} ({single_user[2]})")
else:
    print("User not found")

print()

# fetchall() - returns all rows as list of tuples
cursor.execute('SELECT username FROM users')
all_usernames = cursor.fetchall()

print("All usernames:")
for username_tuple in all_usernames:
    print(f"  - {username_tuple[0]}")

print()


# ============================================================================
# PART 6: Updating Data (UPDATE in CRUD)
# ============================================================================
# UPDATE modifies existing records

print("=== PART 6: Updating Data ===\n")

# Update a user's role
update_query = 'UPDATE users SET role = ? WHERE username = ?'
cursor.execute(update_query, ('senior_analyst', 'bob'))

print(f"Updated {cursor.rowcount} record(s)")

# Verify the change
cursor.execute('SELECT username, role FROM users WHERE username = ?', ('bob',))
updated_user = cursor.fetchone()
print(f"Bob's new role: {updated_user[1]}")

conn.commit()

print()


# ============================================================================
# PART 7: Deleting Data (DELETE in CRUD)
# ============================================================================
# DELETE removes records from table

print("=== PART 7: Deleting Data ===\n")

# Check data before deletion
cursor.execute('SELECT * FROM users WHERE user_id = ?', (3,))
user_before = cursor.fetchone()
print(f"Before deletion: User {user_before[1]} exists")

# Delete a user
delete_query = 'DELETE FROM users WHERE user_id = ?'
cursor.execute(delete_query, (3,))

print(f"Deleted {cursor.rowcount} record(s)")

# Verify deletion
cursor.execute('SELECT * FROM users WHERE user_id = ?', (3,))
user_after = cursor.fetchone()

if user_after is None:
    print("User successfully deleted")

conn.commit()

print()


# ============================================================================
# PART 8: Security Logging Example
# ============================================================================
# Real-world application: Log security events to database

print("=== PART 8: Security Event Logging ===\n")

def log_security_event(event_type, severity, source_ip, description):
    """
    Log a security event to the database.
    
    Args:
        event_type: Type of event (login_attempt, file_access, etc.)
        severity: Severity level (low, medium, high, critical)
        source_ip: IP address of the source
        description: Event description
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    query = '''
    INSERT INTO security_events (timestamp, event_type, severity, source_ip, description)
    VALUES (?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (timestamp, event_type, severity, source_ip, description))
    conn.commit()
    
    print(f"[{timestamp}] Logged {severity.upper()} event: {event_type}")


# Log some events
log_security_event('login_attempt', 'high', '10.0.0.5', 'Multiple failed login attempts')
log_security_event('file_access', 'medium', '192.168.1.50', 'Unauthorized file access attempt')
log_security_event('malware_detected', 'critical', '172.16.0.10', 'Trojan.GenericKD detected')

print()

# Query recent high-severity events
cursor.execute('''
    SELECT timestamp, event_type, source_ip, description
    FROM security_events
    WHERE severity IN ('high', 'critical')
    ORDER BY timestamp DESC
''')

critical_events = cursor.fetchall()

print(f"Found {len(critical_events)} high-severity events:")
for event in critical_events:
    print(f"  [{event[0]}] {event[1]} from {event[2]}")
    print(f"    {event[3]}")

print()


# ============================================================================
# PART 9: Aggregate Functions (COUNT, AVG, SUM, etc.)
# ============================================================================
# SQL aggregate functions perform calculations on data

print("=== PART 9: Aggregate Functions ===\n")

# Count total events
cursor.execute('SELECT COUNT(*) FROM security_events')
total_events = cursor.fetchone()[0]
print(f"Total security events: {total_events}")

# Count events by severity
cursor.execute('''
    SELECT severity, COUNT(*) as count
    FROM security_events
    GROUP BY severity
    ORDER BY count DESC
''')

severity_stats = cursor.fetchall()
print("\nEvents by severity:")
for severity, count in severity_stats:
    print(f"  {severity}: {count}")

print()


# ============================================================================
# PART 10: Closing the Connection
# ============================================================================
# Always close the connection when done

print("=== PART 10: Cleanup ===\n")

# Close cursor and connection
cursor.close()
conn.close()

print("Database connection closed successfully!")
print()
print("=== Module Complete ===")


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Create Inventory Table
Create a table for tracking IT assets (computers, servers, etc.).

# conn = sqlite3.connect('inventory.db')
# cursor = conn.cursor()
# 
# create_table = '''
# CREATE TABLE IF NOT EXISTS assets (
#     asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     hostname TEXT NOT NULL,
#     ip_address TEXT,
#     asset_type TEXT,
#     os TEXT,
#     last_scan TEXT
# )
# '''
# 
# cursor.execute(create_table)
# conn.commit()
# print("Assets table created")
# 
# conn.close()


Exercise 2: Insert and Query Assets
Add assets to your inventory and query them.

# conn = sqlite3.connect('inventory.db')
# cursor = conn.cursor()
# 
# # Insert assets
# assets = [
#     ('WEB-SERVER-01', '192.168.1.10', 'server', 'Ubuntu 22.04', '2026-03-25'),
#     ('DB-SERVER-01', '192.168.1.20', 'server', 'CentOS 8', '2026-03-25'),
#     ('WORKSTATION-01', '192.168.1.100', 'workstation', 'Windows 11', '2026-03-24'),
# ]
# 
# cursor.executemany('''
#     INSERT INTO assets (hostname, ip_address, asset_type, os, last_scan)
#     VALUES (?, ?, ?, ?, ?)
# ''', assets)
# 
# conn.commit()
# 
# # Query servers only
# cursor.execute("SELECT hostname, ip_address FROM assets WHERE asset_type = 'server'")
# servers = cursor.fetchall()
# 
# print("Servers:")
# for server in servers:
#     print(f"  {server[0]}: {server[1]}")
# 
# conn.close()


Exercise 3: Update Asset Information
Update an asset's last scan time.

# conn = sqlite3.connect('inventory.db')
# cursor = conn.cursor()
# 
# # Update last scan time
# new_scan_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 
# cursor.execute('''
#     UPDATE assets
#     SET last_scan = ?
#     WHERE hostname = ?
# ''', (new_scan_time, 'WEB-SERVER-01'))
# 
# print(f"Updated {cursor.rowcount} asset(s)")
# conn.commit()
# conn.close()


Exercise 4: Search with LIKE
Find assets with specific patterns in their hostname.

# conn = sqlite3.connect('inventory.db')
# cursor = conn.cursor()
# 
# # Find all servers (hostname contains 'SERVER')
# cursor.execute('''
#     SELECT hostname, asset_type
#     FROM assets
#     WHERE hostname LIKE ?
# ''', ('%SERVER%',))
# 
# results = cursor.fetchall()
# print(f"Found {len(results)} servers:")
# for hostname, asset_type in results:
#     print(f"  {hostname} ({asset_type})")
# 
# conn.close()


Exercise 5: Delete Old Records
Remove events older than a certain date.

# conn = sqlite3.connect('security.db')
# cursor = conn.cursor()
# 
# cutoff_date = '2026-03-01'
# 
# cursor.execute('''
#     DELETE FROM security_events
#     WHERE timestamp < ?
# ''', (cutoff_date,))
# 
# print(f"Deleted {cursor.rowcount} old event(s)")
# conn.commit()
# conn.close()


Exercise 6: Transaction Support
Use transactions to ensure data integrity.

# conn = sqlite3.connect('security.db')
# cursor = conn.cursor()
# 
# try:
#     # Start transaction (implicit)
#     cursor.execute('''
#         INSERT INTO users (user_id, username, email, role, created_at)
#         VALUES (?, ?, ?, ?, ?)
#     ''', (10, 'dave', 'dave@company.com', 'user', '2026-03-25'))
#     
#     cursor.execute('''
#         INSERT INTO security_events (timestamp, event_type, severity, source_ip, description)
#         VALUES (?, ?, ?, ?, ?)
#     ''', ('2026-03-25 15:00:00', 'account_created', 'low', '192.168.1.1', 'New user account created: dave'))
#     
#     # Commit both changes together
#     conn.commit()
#     print("Transaction successful")
#     
# except sqlite3.Error as e:
#     # Rollback if any error occurs
#     conn.rollback()
#     print(f"Transaction failed: {e}")
# 
# conn.close()


Challenge 1: Security Audit Log System
Build a complete audit logging system with queries.

# class SecurityAuditLog:
#     def __init__(self, db_name='audit.db'):
#         self.conn = sqlite3.connect(db_name)
#         self.cursor = self.conn.cursor()
#         self._create_tables()
#     
#     def _create_tables(self):
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS audit_log (
#                 log_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 timestamp TEXT NOT NULL,
#                 user TEXT NOT NULL,
#                 action TEXT NOT NULL,
#                 resource TEXT,
#                 result TEXT,
#                 ip_address TEXT
#             )
#         ''')
#         self.conn.commit()
#     
#     def log_action(self, user, action, resource, result, ip_address):
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         self.cursor.execute('''
#             INSERT INTO audit_log (timestamp, user, action, resource, result, ip_address)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (timestamp, user, action, resource, result, ip_address))
#         self.conn.commit()
#     
#     def get_user_activity(self, username):
#         self.cursor.execute('''
#             SELECT timestamp, action, resource, result
#             FROM audit_log
#             WHERE user = ?
#             ORDER BY timestamp DESC
#         ''', (username,))
#         return self.cursor.fetchall()
#     
#     def get_failed_actions(self, limit=10):
#         self.cursor.execute('''
#             SELECT timestamp, user, action, resource, ip_address
#             FROM audit_log
#             WHERE result = 'failed'
#             ORDER BY timestamp DESC
#             LIMIT ?
#         ''', (limit,))
#         return self.cursor.fetchall()
#     
#     def close(self):
#         self.conn.close()
# 
# # Usage
# audit = SecurityAuditLog()
# audit.log_action('alice', 'login', 'web_portal', 'success', '192.168.1.100')
# audit.log_action('bob', 'file_access', '/etc/passwd', 'failed', '192.168.1.50')
# 
# failed = audit.get_failed_actions()
# print(f"Recent failed actions: {len(failed)}")
# 
# audit.close()


Challenge 2: Vulnerability Database
Create a database to track vulnerabilities and affected systems.

# conn = sqlite3.connect('vulndb.db')
# cursor = conn.cursor()
# 
# # Create vulnerabilities table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS vulnerabilities (
#         cve_id TEXT PRIMARY KEY,
#         title TEXT NOT NULL,
#         severity TEXT NOT NULL,
#         cvss_score REAL,
#         published_date TEXT,
#         description TEXT
#     )
# ''')
# 
# # Create affected systems table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS affected_systems (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         cve_id TEXT NOT NULL,
#         hostname TEXT NOT NULL,
#         status TEXT,
#         patched_date TEXT,
#         FOREIGN KEY (cve_id) REFERENCES vulnerabilities (cve_id)
#     )
# ''')
# 
# # Insert vulnerabilities
# vulns = [
#     ('CVE-2024-1234', 'Remote Code Execution in WebApp', 'critical', 9.8, '2024-01-15', 'RCE vulnerability'),
#     ('CVE-2024-5678', 'SQL Injection in API', 'high', 7.5, '2024-02-20', 'SQLi in REST API'),
# ]
# 
# cursor.executemany('''
#     INSERT OR IGNORE INTO vulnerabilities (cve_id, title, severity, cvss_score, published_date, description)
#     VALUES (?, ?, ?, ?, ?, ?)
# ''', vulns)
# 
# # Track affected systems
# affected = [
#     ('CVE-2024-1234', 'WEB-01', 'patched', '2024-01-20'),
#     ('CVE-2024-1234', 'WEB-02', 'vulnerable', None),
#     ('CVE-2024-5678', 'API-SERVER', 'vulnerable', None),
# ]
# 
# cursor.executemany('''
#     INSERT INTO affected_systems (cve_id, hostname, status, patched_date)
#     VALUES (?, ?, ?, ?)
# ''', affected)
# 
# conn.commit()
# 
# # Query unpatched critical vulnerabilities
# cursor.execute('''
#     SELECT v.cve_id, v.title, v.cvss_score, a.hostname
#     FROM vulnerabilities v
#     JOIN affected_systems a ON v.cve_id = a.cve_id
#     WHERE v.severity = 'critical' AND a.status = 'vulnerable'
# ''')
# 
# unpatched = cursor.fetchall()
# print(f"Unpatched critical vulnerabilities: {len(unpatched)}")
# for cve, title, score, host in unpatched:
#     print(f"  {cve} (CVSS {score}): {host}")
# 
# conn.close()

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. SQLite Basics:
   - sqlite3.connect(db_name) - create/open database
   - conn.cursor() - create cursor for executing SQL
   - conn.commit() - save changes to database
   - conn.close() - close connection when done
   - No server required - just a file

2. CRUD Operations:
   - CREATE: INSERT INTO table VALUES (?, ?, ?)
   - READ: SELECT column FROM table WHERE condition
   - UPDATE: UPDATE table SET column = ? WHERE condition
   - DELETE: DELETE FROM table WHERE condition

3. Parameterized Queries (CRITICAL for security):
   - ALWAYS use ? placeholders: cursor.execute(query, (param1, param2))
   - NEVER use string formatting: f"...{user_input}..."  # SQL INJECTION RISK!
   - executemany() for inserting multiple records

4. Fetching Results:
   - fetchone() - get single row (returns tuple or None)
   - fetchall() - get all rows (returns list of tuples)
   - fetchmany(n) - get n rows
   - Cursor is iterator - can loop directly: for row in cursor

5. SQLite Data Types:
   - INTEGER - whole numbers
   - REAL - floating point
   - TEXT - strings
   - BLOB - binary data
   - NULL - null value
   - PRIMARY KEY - unique identifier
   - AUTOINCREMENT - auto-generate IDs

6. Common SQL Clauses:
   - WHERE - filter rows
   - ORDER BY - sort results
   - LIMIT - restrict number of results
   - GROUP BY - aggregate data
   - JOIN - combine tables
   - LIKE - pattern matching (% = wildcard)

7. Aggregate Functions:
   - COUNT(*) - count rows
   - SUM(column) - total
   - AVG(column) - average
   - MIN(column) - minimum
   - MAX(column) - maximum

8. Best Practices:
   - Use parameterized queries (prevent SQL injection)
   - Always commit after INSERT/UPDATE/DELETE
   - Close connections when done
   - Use transactions for multiple related changes
   - Create indexes for frequently queried columns
   - Use AUTOINCREMENT for primary keys
   - Normalize data (avoid duplication)

9. Cybersecurity Applications:
   - Security event logging and SIEM
   - User access auditing
   - Vulnerability tracking
   - Incident  management
   - Asset inventory
   - Threat intelligence storage

Remember: SQLite is perfect for local storage, logging, and lightweight applications.
For multi-user systems, consider PostgreSQL or MySQL instead.
ALWAYS use parameterized queries to prevent SQL injection attacks!
"""
