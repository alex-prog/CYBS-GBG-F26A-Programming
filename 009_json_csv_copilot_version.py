"""
009 - JSON and CSV Files: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the JSON and CSV Files exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Work with JSON files (reading and writing)
- Work with CSV files (reading and writing)
- Parse and filter cybersecurity data
- Convert between data formats
- Use Python's json and csv modules effectively

"""

import json 
import csv

# ============================================================================
# PART 1: Writing JSON Files
# ============================================================================
# JSON (JavaScript Object Notation) is a popular data format
# Python dictionaries map naturally to JSON objects

print("=== PART 1: Writing JSON Files ===\n")

incident = {
    'incident_id': 'INC-2024-042',
    'date': '2024-09-16',
    'type': 'data_breach',
    'affected_systems': ['web-server-01', 'database-02'],
    'status': 'investigating'
}

# json.dump() writes Python objects to a file as JSON
# indent=4 makes the output human-readable
with open('incident_report.json', 'w') as file:
    json.dump(incident, file, indent=4)

print(f"Created incident report: {incident['incident_id']}")
print(f"Type: {incident['type']}, Status: {incident['status']}")
print()


# ============================================================================
# PART 2: Reading JSON Files
# ============================================================================
# json.load() reads JSON from a file and converts it to Python objects

print("=== PART 2: Reading JSON Files ===\n")

with open('alert.json', 'r') as file:
    d = json.load(file)
    print(f"Alert {d['alert_id']}: {d['severity'].upper()} severity {d['alert_type']} from {d['source_ip']}")

print()


# ============================================================================
# PART 3: Writing CSV Files
# ============================================================================
# CSV (Comma-Separated Values) is great for tabular data
# Each row is a list, and we can write multiple rows at once

print("=== PART 3: Writing CSV Files ===\n")

security_events = [
    ['timestamp', 'event_type', 'severity', 'description'],
    ['2025-09-16 10:30:00', 'login_failure', 'medium', 'Failed login attempt'],
    ['2025-09-16 10:35:12', 'malware_detected', 'high', 'Trojan found in email'],
    ['2025-09-16 10:40:33', 'unauthorized_access', 'critical', 'Root access attempted']
]

# csv.writer() creates a writer object
# newline='' prevents extra blank lines on Windows
with open('security_report.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(security_events)  # Write all rows at once

print(f"Wrote {len(security_events) - 1} security events to CSV")
print()


# ============================================================================
# PART 4: Reading CSV Files
# ============================================================================
# csv.reader() reads CSV files line by line
# next() gets the next row (useful for getting the header)

print("=== PART 4: Reading CSV Files ===\n")

with open('grades.csv', 'r') as f:
    cr = csv.reader(f)
    h = next(cr)  # Read header row
    print(f"Headers: {h}")
    print()
    
    # Read and display remaining rows
    for e in cr:
        id, name, exam, grade = e  # Unpack the row
        print(f"Student {id}: {name} - Exam: {exam}, Grade: {grade}")

print()


# ============================================================================
# PART 5: JSON Data Filtering and Analysis
# ============================================================================
# Real-world scenario: Filter threat intelligence data
# Select only high-confidence, high-severity indicators

print("=== PART 5: Threat Intelligence Filtering ===\n")

with open('threat_intel.json', 'r') as f:
    d = json.load(f)

    # Filter for high-confidence and high-severity indicators
    filtered_ioc = []

    for i in d['indicators']:
        if i['confidence'] > 80 and i['severity'] == 'high':
            filtered_ioc.append([
                i['ioc_value'], 
                i['ioc_type'], 
                i['severity'], 
                i['confidence'], 
                i['last_seen']
            ])

    print(f"Found {len(filtered_ioc)} high-priority indicators:")
    print()
    
    for ioc in filtered_ioc:
        print(f"  {ioc[1].upper()}: {ioc[0]}")
        print(f"    Severity: {ioc[2]}, Confidence: {ioc[3]}%, Last seen: {ioc[4]}")
        print()


# ============================================================================
# BONUS: Converting JSON to CSV
# ============================================================================
# Practical application: Export filtered threat data to CSV format

print("=== BONUS: Exporting Filtered Data to CSV ===\n")

if filtered_ioc:
    # Define CSV headers
    headers = ['ioc_value', 'ioc_type', 'severity', 'confidence', 'last_seen']
    
    with open('filtered_threats.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)  # Write header
        csv_writer.writerows(filtered_ioc)  # Write data
    
    print(f"Exported {len(filtered_ioc)} threats to filtered_threats.csv")
    print("This CSV can now be imported into SIEM systems or shared with the team")

print()
print("=== Module Complete ===")


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Read and Parse JSON Alert
Read an alert from a JSON file and display it in a formatted way.

# with open('alert.json', 'r') as f:
#     alert = json.load(f)
#     
#     print("===== SECURITY ALERT =====")
#     print(f"Alert ID: {alert['alert_id']}")
#     print(f"Type: {alert['alert_type']}")
#     print(f"Severity: {alert['severity'].upper()}")
#     print(f"Source IP: {alert['source_ip']}")
#     print(f"Description: {alert['description']}")
#     print(f"Status: {alert['status']}")


Exercise 2: Create User Profile JSON
Create a function that saves user profile data to JSON.

# def save_user_profile(username, email, role, department):
#     user_profile = {
#         'username': username,
#         'email': email,
#         'role': role,
#         'department': department,
#         'created_at': '2026-03-25'
#     }
#     
#     with open(f'{username}_profile.json', 'w') as f:
#         json.dump(user_profile, f, indent=4)
#     
#     print(f"Profile created for {username}")
# 
# save_user_profile('jdoe', 'jdoe@company.com', 'analyst', 'security')


Exercise 3: CSV to Dictionary
Read a CSV file and convert it to a list of dictionaries.

# def csv_to_dict(filename):
#     result = []
#     
#     with open(filename, 'r') as f:
#         reader = csv.DictReader(f)  # Uses first row as keys
#         for row in reader:
#             result.append(row)
#     
#     return result
# 
# grades = csv_to_dict('grades.csv')
# for student in grades:
#     print(f"{student['name']}: {student['grade']}")


Exercise 4: Write Security Logs to CSV
Create a function that logs security events to a CSV file.

# def log_security_event(timestamp, event_type, user, ip_address, status):
#     event = [timestamp, event_type, user, ip_address, status]
#     
#     # Append to existing file or create new one with header
#     try:
#         with open('security_logs.csv', 'r') as f:
#             pass  # File exists
#         append_header = False
#     except FileNotFoundError:
#         append_header = True
#     
#     with open('security_logs.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         
#         if append_header:
#             writer.writerow(['timestamp', 'event_type', 'user', 'ip_address', 'status'])
#         
#         writer.writerow(event)
#     
#     print(f"Logged: {event_type} event for {user}")
# 
# log_security_event('2026-03-25 10:30:00', 'login', 'alice', '192.168.1.100', 'success')
# log_security_event('2026-03-25 10:31:15', 'file_access', 'alice', '192.168.1.100', 'success')


Exercise 5: Filter CSV Data
Read a CSV and filter rows based on criteria.

# def filter_high_severity_events(csv_file):
#     high_severity = []
#     
#     with open(csv_file, 'r') as f:
#         reader = csv.DictReader(f)
#         
#         for row in reader:
#             if row['severity'] in ['high', 'critical']:
#                 high_severity.append(row)
#     
#     return high_severity
# 
# events = filter_high_severity_events('security_report.csv')
# print(f"Found {len(events)} high-severity events:")
# for event in events:
#     print(f"  {event['timestamp']}: {event['event_type']}")


Exercise 6: JSON to CSV Converter
Create a general function to convert JSON array to CSV.

# def json_to_csv(json_file, csv_file):
#     # Read JSON
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#     
#     # Assuming data is a list of dictionaries
#     if not data:
#         print("No data to convert")
#         return
#     
#     # Get headers from first dictionary
#     headers = list(data[0].keys())
#     
#     # Write to CSV
#     with open(csv_file, 'w', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(data)
#     
#     print(f"Converted {len(data)} records from {json_file} to {csv_file}")


Challenge 1: Cybersecurity Dashboard Data
Create a comprehensive incident report system that:
- Reads incidents from JSON
- Filters by severity and date
- Exports summary to CSV
- Generates statistics

# def generate_incident_report(json_file, csv_output):
#     # Read incidents
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#         incidents = data.get('incidents', [])
#     
#     # Filter and analyze
#     critical_incidents = []
#     severity_counts = {}
#     type_counts = {}
#     
#     for incident in incidents:
#         severity = incident['severity']
#         inc_type = incident['type']
#         
#         # Count by severity and type
#         severity_counts[severity] = severity_counts.get(severity, 0) + 1
#         type_counts[inc_type] = type_counts.get(inc_type, 0) + 1
#         
#         # Filter critical
#         if severity == 'critical':
#             critical_incidents.append([
#                 incident['incident_id'],
#                 incident['date'],
#                 incident['type'],
#                 incident['status']
#             ])
#     
#     # Write to CSV
#     with open(csv_output, 'w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(['Incident ID', 'Date', 'Type', 'Status'])
#         writer.writerows(critical_incidents)
#     
#     # Print statistics
#     print(f"Total incidents: {len(incidents)}")
#     print(f"\nBy severity:")
#     for sev, count in severity_counts.items():
#         print(f"  {sev}: {count}")
#     print(f"\nBy type:")
#     for typ, count in type_counts.items():
#         print(f"  {typ}: {count}")
#     print(f"\nCritical incidents exported to {csv_output}")
# 
# generate_incident_report('all_incidents.json', 'critical_incidents.csv')


Challenge 2: IoC (Indicator of Compromise) Manager
Build a system to manage threat intelligence IoCs:
- Load IoCs from JSON
- Add new IoCs
- Search by type or value
- Export filtered results to CSV

# class IoCManager:
#     def __init__(self, json_file):
#         self.json_file = json_file
#         self.iocs = self.load_iocs()
#     
#     def load_iocs(self):
#         try:
#             with open(self.json_file, 'r') as f:
#                 data = json.load(f)
#                 return data.get('indicators', [])
#         except FileNotFoundError:
#             return []
#     
#     def add_ioc(self, ioc_value, ioc_type, severity, confidence):
#         new_ioc = {
#             'ioc_value': ioc_value,
#             'ioc_type': ioc_type,
#             'severity': severity,
#             'confidence': confidence,
#             'last_seen': '2026-03-25'
#         }
#         self.iocs.append(new_ioc)
#         print(f"Added IoC: {ioc_value}")
#     
#     def search_by_type(self, ioc_type):
#         return [ioc for ioc in self.iocs if ioc['ioc_type'] == ioc_type]
#     
#     def search_by_severity(self, severity):
#         return [ioc for ioc in self.iocs if ioc['severity'] == severity]
#     
#     def export_to_csv(self, filename, filter_func=None):
#         iocs_to_export = self.iocs if not filter_func else filter_func()
#         
#         if not iocs_to_export:
#             print("No IoCs to export")
#             return
#         
#         headers = ['ioc_value', 'ioc_type', 'severity', 'confidence', 'last_seen']
#         
#         with open(filename, 'w', newline='') as f:
#             writer = csv.DictWriter(f, fieldnames=headers)
#             writer.writeheader()
#             writer.writerows(iocs_to_export)
#         
#         print(f"Exported {len(iocs_to_export)} IoCs to {filename}")
#     
#     def save(self):
#         with open(self.json_file, 'w') as f:
#             json.dump({'indicators': self.iocs}, f, indent=4)
#         print(f"Saved {len(self.iocs)} IoCs to {self.json_file}")
# 
# # Usage:
# manager = IoCManager('threat_intel.json')
# manager.add_ioc('malicious-domain.com', 'domain', 'high', 95)
# 
# high_severity = manager.search_by_severity('high')
# print(f"Found {len(high_severity)} high-severity IoCs")
# 
# manager.export_to_csv('high_severity_iocs.csv', lambda: high_severity)
# manager.save()

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. JSON Operations:
   - json.load(file): Read JSON from file into Python objects
   - json.dump(data, file): Write Python objects to file as JSON
   - indent parameter makes JSON human-readable
   - JSON maps: dict↔object, list↔array, str↔string, int/float↔number

2. CSV Operations:
   - csv.reader(file): Read CSV rows as lists
   - csv.writer(file): Write lists as CSV rows
   - csv.DictReader(file): Read CSV as dictionaries (uses header row as keys)
   - csv.DictWriter(file): Write dictionaries as CSV (specify fieldnames)
   - Always use newline='' on Windows to prevent extra blank lines

3. File Operations with Context Managers:
   - Always use 'with' statement for automatic file closing
   - 'r' mode for reading, 'w' for writing (overwrites), 'a' for appending
   - with open(file, 'r') as f: ensures file is closed even if errors occur

4. Data Filtering and Processing:
   - Use loops and conditionals to filter data
   - Build filtered results in lists
   - Apply multiple filter criteria with 'and'/'or' logic
   - Extract specific fields from dictionaries

5. Real-World Cybersecurity Applications:
   - Security events: Use CSV for structured log data
   - Alerts and incidents: JSON for complex nested data
   - Threat intelligence: JSON for IoCs with metadata
   - Reports: Convert JSON to CSV for SIEM/spreadsheet tools
   - Automation: Read configs from JSON, log results to CSV

6. Best Practices:
   - Validate data before processing (check keys exist, handle missing values)
   - Use descriptive variable names (ioc, incident, alert vs d, i, a)
   - Add error handling for missing files or malformed data
   - Use indent=4 for JSON files that humans will read
   - Use DictReader/DictWriter for more readable CSV code

Remember: JSON for complex/nested data, CSV for simple tabular data!
"""
