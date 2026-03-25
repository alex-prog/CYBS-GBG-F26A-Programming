"""
011 - MySQL Database: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the MySQL Database exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Connect to MySQL databases
- Execute SQL queries on MySQL server
- Understand differences between SQLite and MySQL
- Work with remote database connections
- Apply MySQL in multi-user environments
- Handle connection errors and authentication

"""

# Required package: mysql-connector-python
# Install with: pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error


# ============================================================================
# PART 1: MySQL vs SQLite
# ============================================================================
"""
Key Differences:

SQLite:
- File-based (no server)
- Single-user/embedded
- Great for: local storage, mobile apps, testing
- No user management
- Limited concurrent writes

MySQL:
- Client-server architecture
- Multi-user support
- Great for: web applications, production systems
- User authentication & permissions
- High concurrency
- ACID compliance
- Better for large datasets

When to use MySQL:
- Web applications with multiple users
- Centralized data storage
- When you need user access control
- Production environments
- High-traffic applications
"""

print("=== PART 1: MySQL Overview ===\n")
print("MySQL is a client-server database system")
print("Requires: MySQL server running + credentials for connection")
print()


# ============================================================================
# PART 2: Connection Configuration
# ============================================================================
# MySQL requires server host, username, password, and database name

print("=== PART 2: MySQL Connection Setup ===\n")

# Connection parameters (fill these with your database info)
# These would typically come from environment variables or config files
DB_CONFIG = {
    'host': 'localhost',        # or IP address of MySQL server
    'user': 'your_username',    # MySQL username
    'password': 'your_password',# MySQL password
    'database': 'your_database' # Database name
}

# In production, NEVER hardcode credentials!
# Use environment variables or secure config:
# import os
# DB_CONFIG = {
#     'host': os.getenv('DB_HOST'),
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASSWORD'),
#     'database': os.getenv('DB_NAME')
# }

print("Connection configuration:")
print(f"  Host: {DB_CONFIG['host']}")
print(f"  User: {DB_CONFIG['user']}")
print(f"  Database: {DB_CONFIG['database']}")
print()


# ============================================================================
# PART 3: Connecting to MySQL
# ============================================================================
# Use try/except to handle connection errors gracefully

print("=== PART 3: Establishing Connection ===\n")

def create_connection(config):
    """
    Create a connection to MySQL database.
    
    Args:
        config: Dictionary with connection parameters
    
    Returns:
        Connection object if successful, None otherwise
    """
    try:
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
            
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            database_name = cursor.fetchone()
            print(f"Connected to database: {database_name[0]}")
            
            return connection
            
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Example connection (will fail without real credentials)
# conn = create_connection(DB_CONFIG)

print()


# ============================================================================
# PART 4: Basic Query Example
# ============================================================================
# Once connected, queries work similar to SQLite

print("=== PART 4: Executing Queries ===\n")

def query_students(connection):
    """
    Query students table and display results.
    """
    try:
        cursor = connection.cursor()
        
        # Execute SELECT query
        cursor.execute("SELECT * FROM students")
        
        # Fetch all results
        data = cursor.fetchall()
        
        if not data:
            print("Table is empty!")
        else:
            print(f"Found {len(data)} student(s):")
            for row in data:
                print(f"  {row}")
        
        cursor.close()
        
    except Error as e:
        print(f"Error querying database: {e}")

# Example usage (requires active connection):
# if conn and conn.is_connected():
#     query_students(conn)

print()


# ============================================================================
# PART 5: Creating Tables in MySQL
# ============================================================================
# Similar to SQLite but with MySQL-specific features

print("=== PART 5: Creating Tables ===\n")

def create_security_table(connection):
    """
    Create a security events table in MySQL.
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS security_events (
        event_id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME NOT NULL,
        event_type VARCHAR(50) NOT NULL,
        severity ENUM('low', 'medium', 'high', 'critical') NOT NULL,
        source_ip VARCHAR(45),
        user_account VARCHAR(100),
        description TEXT,
        INDEX idx_timestamp (timestamp),
        INDEX idx_severity (severity)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'security_events' created successfully")
        cursor.close()
        
    except Error as e:
        print(f"Error creating table: {e}")

# MySQL-specific features used above:
# - AUTO_INCREMENT instead of AUTOINCREMENT
# - VARCHAR(n) for variable-length strings
# - ENUM for predefined values
# - INDEX for faster queries
# - ENGINE=InnoDB for transactions
# - CHARSET=utf8mb4 for full Unicode support

print()


# ============================================================================
# PART 6: Inserting Data with Parameterized Queries
# ============================================================================
# ALWAYS use parameterized queries to prevent SQL injection

print("=== PART 6: Inserting Data ===\n")

def log_security_event(connection, event_type, severity, source_ip, user, description):
    """
    Insert a security event into the database.
    """
    insert_query = """
    INSERT INTO security_events (timestamp, event_type, severity, source_ip, user_account, description)
    VALUES (NOW(), %s, %s, %s, %s, %s)
    """
    
    # MySQL uses %s placeholders (not ? like SQLite)
    data = (event_type, severity, source_ip, user, description)
    
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        
        print(f"Logged event: {event_type} (Severity: {severity})")
        print(f"  Event ID: {cursor.lastrowid}")
        
        cursor.close()
        return cursor.lastrowid
        
    except Error as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
        return None

# Example usage:
# if conn and conn.is_connected():
#     log_security_event(
#         conn,
#         'login_failure',
#         'medium',
#         '192.168.1.100',
#         'alice',
#         'Failed login attempt - incorrect password'
#     )

print()


# ============================================================================
# PART 7: Querying with Filters
# ============================================================================
# Use WHERE clauses to filter results

print("=== PART 7: Filtering Queries ===\n")

def get_high_severity_events(connection, limit=10):
    """
    Retrieve recent high-severity security events.
    """
    query = """
    SELECT event_id, timestamp, event_type, source_ip, user_account, description
    FROM security_events
    WHERE severity IN ('high', 'critical')
    ORDER BY timestamp DESC
    LIMIT %s
    """
    
    try:
        cursor = connection.cursor()
        cursor.execute(query, (limit,))
        
        results = cursor.fetchall()
        
        print(f"High-severity events (last {limit}):")
        for row in results:
            event_id, timestamp, event_type, source_ip, user, desc = row
            print(f"  [{timestamp}] {event_type} from {source_ip}")
            print(f"    User: {user}, Description: {desc}")
        
        cursor.close()
        return results
        
    except Error as e:
        print(f"Error querying events: {e}")
        return []

print()


# ============================================================================
# PART 8: Connection Pooling
# ============================================================================
# For production: use connection pooling for better performance

print("=== PART 8: Connection Pooling ===\n")

def create_connection_pool(config, pool_name="mypool", pool_size=5):
    """
    Create a connection pool for efficient database access.
    """
    try:
        from mysql.connector import pooling
        
        connection_pool = pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )
        
        print(f"Connection pool '{pool_name}' created with {pool_size} connections")
        return connection_pool
        
    except Error as e:
        print(f"Error creating connection pool: {e}")
        return None

# Get connection from pool
# pool = create_connection_pool(DB_CONFIG)
# connection = pool.get_connection()
# # Use connection...
# connection.close()  # Returns connection to pool

print()


# ============================================================================
# PART 9: Error Handling and Cleanup
# ============================================================================
# Proper resource management is critical

print("=== PART 9: Proper Connection Handling ===\n")

def execute_query_safely(config, query, params=None):
    """
    Execute a query with proper error handling and cleanup.
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        # Execute query
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        # Fetch results
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
            return results
        else:
            connection.commit()
            return cursor.rowcount
            
    except Error as e:
        print(f"Database error: {e}")
        if connection:
            connection.rollback()
        return None
        
    finally:
        # Always close resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

print()


# ============================================================================
# PART 10: Complete Working Example
# ============================================================================
# Full example with connection, query, and cleanup

print("=== PART 10: Complete Example ===\n")

def main():
    """
    Complete example of MySQL database operations.
    """
    # Configuration (replace with your actual credentials)
    config = {
        'host': 'localhost',
        'user': 'security_user',
        'password': 'secure_password',
        'database': 'security_db'
    }
    
    connection = None
    
    try:
        # Connect
        print("Connecting to MySQL...")
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            print("Connected successfully!")
            
            cursor = connection.cursor()
            
            # Example: Query database version
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"MySQL version: {version[0]}")
            
            # Example: Count records
            cursor.execute("SELECT COUNT(*) FROM students")
            count = cursor.fetchone()
            print(f"Total students: {count[0]}")
            
            cursor.close()
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")

# Uncomment to run (requires valid MySQL credentials):
# main()

print()
print("=== Module Complete ===")
print()
print("NOTE: This file demonstrates MySQL concepts.")
print("To run these examples, you need:")
print("  1. MySQL server installed and running")
print("  2. A database created")
print("  3. Valid credentials (username/password)")
print("  4. mysql-connector-python package installed")


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Create Database Connection Function
Create a reusable connection function with error handling.

# def get_db_connection():
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='your_user',
#             password='your_password',
#             database='your_database',
#             autocommit=False  # Manual transaction control
#         )
#         return conn
#     except Error as e:
#         print(f"Connection failed: {e}")
#         return None
# 
# conn = get_db_connection()
# if conn:
#     print("Connected!")
#     conn.close()


Exercise 2: Create Users Table
Create a table for storing user account information.

# def create_users_table(connection):
#     create_table_sql = '''
#     CREATE TABLE IF NOT EXISTS users (
#         user_id INT AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(50) UNIQUE NOT NULL,
#         email VARCHAR(100) NOT NULL,
#         role ENUM('admin', 'analyst', 'user') DEFAULT 'user',
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#         last_login DATETIME,
#         active BOOLEAN DEFAULT TRUE
#     ) ENGINE=InnoDB;
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#         connection.commit()
#         print("Users table created")
#         cursor.close()
#     except Error as e:
#         print(f"Error: {e}")
# 
# conn = get_db_connection()
# if conn:
#     create_users_table(conn)
#     conn.close()


Exercise 3: Insert Multiple Users
Use executemany() to insert multiple records efficiently.

# def add_users(connection, users_list):
#     insert_sql = '''
#     INSERT INTO users (username, email, role)
#     VALUES (%s, %s, %s)
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.executemany(insert_sql, users_list)
#         connection.commit()
#         print(f"Inserted {cursor.rowcount} users")
#         cursor.close()
#     except Error as e:
#         print(f"Error: {e}")
#         connection.rollback()
# 
# users = [
#     ('alice', 'alice@company.com', 'admin'),
#     ('bob', 'bob@company.com', 'analyst'),
#     ('charlie', 'charlie@company.com', 'user')
# ]
# 
# conn = get_db_connection()
# if conn:
#     add_users(conn, users)
#     conn.close()


Exercise 4: Query with JOIN
Join two tables to get related data.

# def get_user_events(connection, username):
#     query = '''
#     SELECT u.username, e.timestamp, e.event_type, e.severity
#     FROM users u
#     JOIN security_events e ON u.username = e.user_account
#     WHERE u.username = %s
#     ORDER BY e.timestamp DESC
#     LIMIT 20
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query, (username,))
#         
#         results = cursor.fetchall()
#         print(f"Events for user {username}:")
#         for row in results:
#             print(f"  [{row[1]}] {row[2]} - {row[3]}")
#         
#         cursor.close()
#         return results
#     except Error as e:
#         print(f"Error: {e}")
#         return []
# 
# conn = get_db_connection()
# if conn:
#     get_user_events(conn, 'alice')
#     conn.close()


Exercise 5: Update User Last Login
Update a user's last login timestamp.

# def update_last_login(connection, username):
#     update_sql = '''
#     UPDATE users
#     SET last_login = NOW()
#     WHERE username = %s
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.execute(update_sql, (username,))
#         connection.commit()
#         
#         if cursor.rowcount > 0:
#             print(f"Updated last login for {username}")
#         else:
#             print(f"User {username} not found")
#         
#         cursor.close()
#     except Error as e:
#         print(f"Error: {e}")
#         connection.rollback()
# 
# conn = get_db_connection()
# if conn:
#     update_last_login(conn, 'alice')
#     conn.close()


Exercise 6: Aggregate Statistics
Get statistics about security events.

# def get_event_statistics(connection):
#     query = '''
#     SELECT 
#         severity,
#         COUNT(*) as count,
#         DATE(timestamp) as date
#     FROM security_events
#     WHERE timestamp >= DATE_SUB(NOW(), INTERVAL 7 DAY)
#     GROUP BY severity, DATE(timestamp)
#     ORDER BY date DESC, severity
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         
#         results = cursor.fetchall()
#         print("Event statistics (last 7 days):")
#         for severity, count, date in results:
#             print(f"  {date}: {severity} - {count} events")
#         
#         cursor.close()
#         return results
#     except Error as e:
#         print(f"Error: {e}")
#         return []
# 
# conn = get_db_connection()
# if conn:
#     get_event_statistics(conn)
#     conn.close()


Challenge 1: Incident Management System
Build a complete incident tracking system with MySQL.

# class IncidentManager:
#     def __init__(self, config):
#         self.config = config
#     
#     def create_tables(self):
#         connection = mysql.connector.connect(**self.config)
#         cursor = connection.cursor()
#         
#         # Incidents table
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS incidents (
#                 incident_id INT AUTO_INCREMENT PRIMARY KEY,
#                 title VARCHAR(200) NOT NULL,
#                 severity ENUM('low', 'medium', 'high', 'critical'),
#                 status ENUM('open', 'investigating', 'resolved', 'closed') DEFAULT 'open',
#                 assigned_to VARCHAR(50),
#                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                 updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#                 description TEXT
#             ) ENGINE=InnoDB
#         ''')
#         
#         connection.commit()
#         cursor.close()
#         connection.close()
#     
#     def create_incident(self, title, severity, description):
#         connection = mysql.connector.connect(**self.config)
#         cursor = connection.cursor()
#         
#         cursor.execute('''
#             INSERT INTO incidents (title, severity, description)
#             VALUES (%s, %s, %s)
#         ''', (title, severity, description))
#         
#         connection.commit()
#         incident_id = cursor.lastrowid
#         
#         cursor.close()
#         connection.close()
#         
#         return incident_id
#     
#     def get_open_incidents(self):
#         connection = mysql.connector.connect(**self.config)
#         cursor = connection.cursor(dictionary=True)
#         
#         cursor.execute('''
#             SELECT * FROM incidents
#             WHERE status IN ('open', 'investigating')
#             ORDER BY severity DESC, created_at DESC
#         ''')
#         
#         incidents = cursor.fetchall()
#         
#         cursor.close()
#         connection.close()
#         
#         return incidents
# 
# # Usage
# config = {'host': 'localhost', 'user': 'user', 'password': 'pass', 'database': 'db'}
# manager = IncidentManager(config)
# manager.create_tables()
# incident_id = manager.create_incident('Unauthorized Access', 'high', 'Suspicious login detected')


Challenge 2: Database Backup and Export
Create a utility to export security events to CSV.

# def export_events_to_csv(connection, output_file, days=7):
#     import csv
#     from datetime import datetime, timedelta
#     
#     cutoff_date = datetime.now() - timedelta(days=days)
#     
#     query = '''
#     SELECT event_id, timestamp, event_type, severity, source_ip, user_account, description
#     FROM security_events
#     WHERE timestamp >= %s
#     ORDER BY timestamp DESC
#     '''
#     
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query, (cutoff_date,))
#         
#         results = cursor.fetchall()
#         
#         with open(output_file, 'w', newline='', encoding='utf-8') as f:
#             writer = csv.writer(f)
#             
#             # Write header
#             writer.writerow(['Event ID', 'Timestamp', 'Type', 'Severity', 'Source IP', 'User', 'Description'])
#             
#             # Write data
#             writer.writerows(results)
#         
#         print(f"Exported {len(results)} events to {output_file}")
#         cursor.close()
#         
#     except Error as e:
#         print(f"Export failed: {e}")
# 
# conn = get_db_connection()
# if conn:
#     export_events_to_csv(conn, 'security_events_export.csv', days=30)
#     conn.close()

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. MySQL Connection:
   - mysql.connector.connect(host, user, password, database)
   - Check connection: connection.is_connected()
   - Always close: connection.close()
   - Use try/except for error handling

2. MySQL vs SQLite Syntax Differences:
   - Placeholders: %s (MySQL) vs ? (SQLite)
   - Auto-increment: AUTO_INCREMENT vs AUTOINCREMENT
   - Data types: VARCHAR(n), ENUM, DATETIME vs TEXT
   - Engines: ENGINE=InnoDB
   - Functions: NOW(), CURRENT_TIMESTAMP

3. Data Types in MySQL:
   - INT, BIGINT - integers
   - VARCHAR(n) - variable-length strings (max n chars)
   - TEXT - large text
   - DATETIME, TIMESTAMP - dates and times
   - ENUM - predefined values
   - BOOLEAN - true/false
   - DECIMAL(m,d) - precise decimals

4. Parameterized Queries (CRITICAL):
   - Use %s placeholders: cursor.execute(query, (param1, param2))
   - NEVER: f"SELECT * FROM users WHERE name='{name}'"  # SQL INJECTION!
   - ALWAYS: cursor.execute("SELECT * FROM users WHERE name=%s", (name,))

5. Connection Management:
   - Single connection: Good for scripts
   - Connection pooling: Better for applications
   - Context managers: Use 'with' when available
   - Always close cursors and connections
   - Handle errors with try/except/finally

6. Transactions:
   - connection.commit() - save changes
   - connection.rollback() - undo changes
   - autocommit=True - auto-save (not recommended)
   - Use transactions for multiple related operations

7. Performance Tips:
   - Use connection pooling for web apps
   - Create indexes on frequently queried columns
   - Use LIMIT to restrict large result sets
   - Use executemany() for bulk inserts
   - Close cursors after use

8. Security Best Practices:
   - NEVER hardcode credentials in code
   - Use environment variables or config files
   - Restrict database user permissions
   - Use parameterized queries (prevent SQL injection)
   - Enable SSL for remote connections
   - Regularly update MySQL server
   - Monitor failed connection attempts

9. Cursor Types:
   - Default cursor: returns tuples
   - cursor(dictionary=True): returns dictionaries
   - cursor(buffered=True): fetches all results immediately

10. Common MySQL Functions:
    - NOW() - current datetime
    - DATE() - extract date
    - COUNT(*) - count rows
    - SUM(), AVG(), MIN(), MAX() - aggregates
    - CONCAT() - concatenate strings
    - DATE_SUB() - date arithmetic

Remember: MySQL is production-ready for multi-user, high-traffic applications.
Always use parameterized queries and secure your database credentials!
"""
