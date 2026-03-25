import json 
import csv

print('hello')


# incident = {
#     'incident_id': 'INC-2024-042',
#     'date': '2024-09-16',
#     'type': 'data_breach',
#     'affected_systems': ['web-server-01', 'database-02'],
#     'status': 'investigating'
# }
 
# with open('incident_report.json', 'w') as file:
#     json.dump(incident, file, indent=4)

# with open('alert.json', 'r') as file:
#     d = json.load(file)
#     print(f'Alert {d['alert_id']}: {d['severity'].upper()} severity {d['alert_type']} from {d['source_ip']}')


# security_events = [
#     ['timestamp', 'event_type', 'severity', 'description'],
#     ['2025-09-16 10:30:00', 'login_failure', 'medium', 'Failed login attempt'],
#     ['2025-09-16 10:35:12', 'malware_detected', 'high', 'Trojan found in email'],
#     ['2025-09-16 10:40:33', 'unauthorized_access', 'critical', 'Root access attempted']
# ]

# with open('security_report.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(security_events)

# with open('grades.csv', 'r') as f:
#     cr = csv.reader(f)
#     h = next(cr)
#     a = next(cr)
#     print(h)
#     for e in cr:
#         id, name, exam, grade = e
#         print(id, name, exam, grade)

# with open('threat_intel.json', 'r') as f:
#     d = json.load(f)

#     filtered_ioc = []

#     for i in d['indicators']:
#         if i['confidence'] > 80 and i['severity'] == 'high':
#             filtered_ioc.append([i['ioc_value'], 
#                                  i['ioc_type'], 
#                                  i['severity'], 
#                                  i['confidence'], 
#                                  i['last_seen']])

#     print(filtered_ioc)
