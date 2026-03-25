"""
011 - HTTP Requests: GitHub Copilot's Version
CYBS-GBG-F26A Programming Course - Spring 2026

This is my enhanced version of the HTTP Requests exercise.
The original instructor file remains unchanged.

Learning Objectives:
- Install and use the requests library
- Make GET and POST requests
- Handle HTTP status codes and responses
- Send authentication credentials
- Work with sessions and cookies
- Apply HTTP requests in cybersecurity scenarios

"""

import requests
from requests.auth import HTTPBasicAuth


# ============================================================================
# PART 1: Installing the Requests Library
# ============================================================================
# The requests library must be installed first
# Installation commands:
#   pip install requests
#   pip3 install requests
#   python -m pip install requests

print("=== PART 1: Basic GET Request ===\n")

# GET request - retrieve data from a server
response = requests.get("https://httpbin.org/get")

# Check HTTP status code
print(f"Status Code: {response.status_code}")  # 200 = success

# Common status codes:
# 200 - OK
# 301/302 - Redirect
# 401 - Unauthorized
# 403 - Forbidden
# 404 - Not Found
# 500 - Internal Server Error

if response.status_code == 200:
    print("Request successful!")
else:
    print(f"Request failed with status {response.status_code}")

print()


# ============================================================================
# PART 2: Inspecting Response Content
# ============================================================================
# The response object contains headers, content, and metadata

print("=== PART 2: Response Content ===\n")

response = requests.get("https://httpbin.org/get")

# Response text (as string)
print("Response text (first 200 chars):")
print(response.text[:200])
print()

# Response JSON (if content is JSON)
print("Response as JSON:")
json_data = response.json()
print(f"URL accessed: {json_data['url']}")
print(f"User-Agent: {json_data['headers']['User-Agent']}")
print()

# Response headers
print("Response headers:")
print(f"Content-Type: {response.headers['Content-Type']}")
print(f"Server: {response.headers.get('Server', 'Unknown')}")
print()


# ============================================================================
# PART 3: POST Requests (Sending Data)
# ============================================================================
# POST requests send data to the server (form submissions, API calls)

print("=== PART 3: POST Request ===\n")

# Send form data
payload = {
    'username': 'alice',
    'password': 'strongpassword',
    'action': 'login'
}

response = requests.post("https://httpbin.org/post", data=payload)

print(f"Status Code: {response.status_code}")
print()

# Inspect what was sent
json_response = response.json()
print("Data sent to server:")
print(f"  Username: {json_response['form']['username']}")
print(f"  Action: {json_response['form']['action']}")
print()


# ============================================================================
# PART 4: HTTP Authentication
# ============================================================================
# Many APIs require authentication (Basic Auth, API keys, Bearer tokens)

print("=== PART 4: HTTP Authentication ===\n")

# Basic Authentication (username + password)
# Note: This example will fail auth, but shows the pattern
response = requests.get(
    'https://httpbin.org/basic-auth/user/passwd',
    auth=HTTPBasicAuth('user', 'passwd')
)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print("Authentication successful!")
    print(f"Response: {response.json()}")
else:
    print("Authentication failed!")

print()


# ============================================================================
# PART 5: Sessions and Cookies
# ============================================================================
# Sessions persist data (cookies, auth) across multiple requests

print("=== PART 5: Sessions and Cookies ===\n")

# Create a session object
session = requests.Session()

# First request - server sets a cookie
response = session.get('https://httpbin.org/cookies/set/session_id/abc123')
print(f"Cookie set - Status: {response.status_code}")

# Second request - cookie is automatically sent
response = session.get('https://httpbin.org/cookies')
print(f"Cookies in session: {response.json()['cookies']}")

print()


# ============================================================================
# PART 6: Custom Headers (API Keys, User-Agent)
# ============================================================================
# Headers provide metadata about the request

print("=== PART 6: Custom Headers ===\n")

# Custom headers (common for APIs)
headers = {
    'User-Agent': 'CyberSecurity-Tool/1.0',
    'Authorization': 'Bearer fake-api-key-12345',
    'Content-Type': 'application/json'
}

response = requests.get('https://httpbin.org/headers', headers=headers)

print(f"Status Code: {response.status_code}")
print("Headers sent:")
sent_headers = response.json()['headers']
print(f"  User-Agent: {sent_headers['User-Agent']}")
print(f"  Authorization: {sent_headers['Authorization']}")

print()


# ============================================================================
# PART 7: Error Handling and Timeouts
# ============================================================================
# Always handle network errors gracefully

print("=== PART 7: Error Handling ===\n")

try:
    # Set timeout to prevent hanging (seconds)
    response = requests.get('https://httpbin.org/delay/1', timeout=5)
    print(f"Request completed: {response.status_code}")
    
except requests.exceptions.Timeout:
    print("Error: Request timed out!")
    
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to server!")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

print()


# ============================================================================
# PART 8: Cybersecurity Use Case - Threat Intelligence API
# ============================================================================
# Real-world example: Query a threat intelligence service

print("=== PART 8: Threat Intelligence Query ===\n")

def check_ip_reputation(ip_address):
    """
    Check IP reputation using a mock API.
    
    In production, use real services like:
    - AbuseIPDB
    - VirusTotal
    - IPVoid
    """
    # Mock API endpoint (httpbin for demonstration)
    api_url = f"https://httpbin.org/get?ip={ip_address}"
    
    headers = {
        'User-Agent': 'ThreatIntel-Scanner/1.0',
        'X-API-Key': 'your-api-key-here'
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"IP {ip_address} checked successfully")
            print(f"  Query URL: {data['url']}")
            return True
        else:
            print(f"API error: Status {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

# Test IP reputation check
check_ip_reputation('192.168.1.100')

print()
print("=== Module Complete ===")


# ============================================================================
# EXERCISES
# ============================================================================
"""
Practice what you've learned!

Exercise 1: Weather API Request
Use a public API to get weather data. Try https://wttr.in/London?format=j1

# response = requests.get('https://wttr.in/London?format=j1')
# if response.status_code == 200:
#     weather = response.json()
#     current = weather['current_condition'][0]
#     print(f"Temperature: {current['temp_C']}°C")
#     print(f"Description: {current['weatherDesc'][0]['value']}")
# else:
#     print(f"Failed to get weather: {response.status_code}")


Exercise 2: Download File
Download a file from the internet and save it locally.

# def download_file(url, filename):
#     try:
#         response = requests.get(url, timeout=30)
#         
#         if response.status_code == 200:
#             with open(filename, 'wb') as f:
#                 f.write(response.content)
#             print(f"Downloaded {filename} successfully")
#             return True
#         else:
#             print(f"Download failed: {response.status_code}")
#             return False
#             
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return False
# 
# # Test with a small file
# download_file('https://httpbin.org/image/png', 'test_image.png')


Exercise 3: JSON API POST Request
Send JSON data to an API endpoint.

# import json
# 
# def submit_incident_report(incident_data):
#     api_url = 'https://httpbin.org/post'
#     
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer api-key-123'
#     }
#     
#     try:
#         response = requests.post(
#             api_url,
#             json=incident_data,  # Automatically converts to JSON
#             headers=headers,
#             timeout=10
#         )
#         
#         if response.status_code == 200:
#             print("Incident report submitted successfully")
#             print(f"Response: {response.json()['data']}")
#             return True
#         else:
#             print(f"Submission failed: {response.status_code}")
#             return False
#             
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return False
# 
# # Test
# incident = {
#     'incident_id': 'INC-2026-001',
#     'severity': 'high',
#     'description': 'Suspicious login attempts detected'
# }
# submit_incident_report(incident)


Exercise 4: Check Multiple URLs
Check the status of multiple URLs and report which are up or down.

# def check_urls(url_list):
#     results = {}
#     
#     for url in url_list:
#         try:
#             response = requests.get(url, timeout=5)
#             results[url] = {
#                 'status': response.status_code,
#                 'available': response.status_code == 200
#             }
#         except requests.exceptions.RequestException as e:
#             results[url] = {
#                 'status': 'error',
#                 'available': False,
#                 'error': str(e)
#             }
#     
#     return results
# 
# # Test
# urls = [
#     'https://httpbin.org',
#     'https://example.com',
#     'https://this-site-does-not-exist-12345.com'
# ]
# 
# results = check_urls(urls)
# for url, info in results.items():
#     status = "UP" if info['available'] else "DOWN"
#     print(f"{url}: {status} (Status: {info['status']})")


Exercise 5: Rate Limiting
Implement rate limiting when making multiple API requests.

# import time
# 
# def rate_limited_requests(urls, requests_per_second=2):
#     '''
#     Make requests with rate limiting to avoid overwhelming the server.
#     '''
#     delay = 1.0 / requests_per_second
#     results = []
#     
#     for i, url in enumerate(urls):
#         try:
#             print(f"Request {i+1}/{len(urls)}: {url}")
#             response = requests.get(url, timeout=5)
#             results.append({
#                 'url': url,
#                 'status': response.status_code,
#                 'success': True
#             })
#             
#             # Wait before next request (except for last one)
#             if i < len(urls) - 1:
#                 time.sleep(delay)
#                 
#         except requests.exceptions.RequestException as e:
#             results.append({
#                 'url': url,
#                 'error': str(e),
#                 'success': False
#             })
#     
#     return results
# 
# # Test with 5 requests, max 2 per second
# urls = [f'https://httpbin.org/delay/0' for _ in range(5)]
# results = rate_limited_requests(urls, requests_per_second=2)
# print(f"Completed {len([r for r in results if r['success']])} successful requests")


Exercise 6: Parse HTML Response
Fetch HTML and extract specific information (requires BeautifulSoup).

# # First install: pip install beautifulsoup4
# from bs4 import BeautifulSoup
# 
# def extract_links(url):
#     try:
#         response = requests.get(url, timeout=10)
#         
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             
#             # Find all links
#             links = []
#             for link in soup.find_all('a'):
#                 href = link.get('href')
#                 text = link.get_text(strip=True)
#                 if href:
#                     links.append({'url': href, 'text': text})
#             
#             return links
#         else:
#             print(f"Failed: {response.status_code}")
#             return []
#             
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return []
# 
# # Test
# links = extract_links('https://example.com')
# print(f"Found {len(links)} links")
# for link in links[:5]:  # Show first 5
#     print(f"  {link['text']}: {link['url']}")


Challenge 1: IoC Checker with Multiple Services
Create a tool that checks IP addresses against multiple threat intelligence APIs.

# class ThreatIntelChecker:
#     def __init__(self):
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'ThreatIntel-Tool/1.0'
#         })
#     
#     def check_ip_abuseipdb(self, ip, api_key):
#         '''Check IP against AbuseIPDB (mock example)'''
#         url = f'https://api.abuseipdb.com/api/v2/check'
#         headers = {'Key': api_key}
#         params = {'ipAddress': ip}
#         
#         try:
#             response = self.session.get(url, headers=headers, params=params, timeout=10)
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 return {'error': f'Status {response.status_code}'}
#         except requests.exceptions.RequestException as e:
#             return {'error': str(e)}
#     
#     def check_ip_virustotal(self, ip, api_key):
#         '''Check IP against VirusTotal (mock example)'''
#         url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
#         headers = {'x-apikey': api_key}
#         
#         try:
#             response = self.session.get(url, headers=headers, timeout=10)
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 return {'error': f'Status {response.status_code}'}
#         except requests.exceptions.RequestException as e:
#             return {'error': str(e)}
#     
#     def check_ip_all_services(self, ip, api_keys):
#         '''Check IP against all available services'''
#         results = {}
#         
#         if 'abuseipdb' in api_keys:
#             print(f"Checking {ip} on AbuseIPDB...")
#             results['abuseipdb'] = self.check_ip_abuseipdb(ip, api_keys['abuseipdb'])
#         
#         if 'virustotal' in api_keys:
#             print(f"Checking {ip} on VirusTotal...")
#             results['virustotal'] = self.check_ip_virustotal(ip, api_keys['virustotal'])
#         
#         return results
# 
# # Usage
# checker = ThreatIntelChecker()
# api_keys = {
#     'abuseipdb': 'your-api-key-here',
#     'virustotal': 'your-api-key-here'
# }
# results = checker.check_ip_all_services('8.8.8.8', api_keys)


Challenge 2: Web Scraper with Error Recovery
Build a resilient web scraper that retries failed requests.

# def fetch_with_retry(url, max_retries=3, backoff=2):
#     '''
#     Fetch URL with exponential backoff retry logic.
#     
#     Args:
#         url: URL to fetch
#         max_retries: Maximum number of retry attempts
#         backoff: Backoff multiplier (seconds between retries)
#     '''
#     for attempt in range(max_retries):
#         try:
#             print(f"Attempt {attempt + 1}/{max_retries}: {url}")
#             response = requests.get(url, timeout=10)
#             
#             if response.status_code == 200:
#                 print(f"Success on attempt {attempt + 1}")
#                 return response
#             elif response.status_code == 429:  # Too Many Requests
#                 retry_after = int(response.headers.get('Retry-After', backoff * (attempt + 1)))
#                 print(f"Rate limited. Waiting {retry_after}s before retry...")
#                 time.sleep(retry_after)
#             else:
#                 print(f"HTTP {response.status_code}, retrying...")
#                 time.sleep(backoff * (attempt + 1))
#                 
#         except requests.exceptions.Timeout:
#             print(f"Timeout on attempt {attempt + 1}")
#             if attempt < max_retries - 1:
#                 time.sleep(backoff * (attempt + 1))
#         except requests.exceptions.RequestException as e:
#             print(f"Error: {e}")
#             if attempt < max_retries - 1:
#                 time.sleep(backoff * (attempt + 1))
#     
#     print(f"Failed after {max_retries} attempts")
#     return None
# 
# # Test
# response = fetch_with_retry('https://httpbin.org/status/200,429,500')
# if response:
#     print(f"Final status: {response.status_code}")

"""


# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
1. Requests Library Basics:
   - requests.get(url) - retrieve data
   - requests.post(url, data=...) - send data
   - response.status_code - HTTP status (200=success, 404=not found, etc.)
   - response.text - response as string
   - response.json() - parse JSON response
   - response.headers - HTTP headers

2. Authentication Methods:
   - Basic Auth: auth=HTTPBasicAuth('user', 'pass')
   - API Keys: headers={'Authorization': 'Bearer api-key'}
   - Custom Headers: headers={'X-API-Key': 'key'}
   - Sessions: persist cookies and auth across requests

3. Best Practices:
   - Always set timeout to prevent hanging
   - Use try/except for error handling
   - Check status_code before processing response
   - Use sessions for multiple requests to same server
   - Implement rate limiting to be respectful
   - Close sessions when done (or use 'with' statement)

4. Common HTTP Status Codes:
   - 2xx Success: 200 OK, 201 Created, 204 No Content
   - 3xx Redirect: 301 Moved, 302 Found, 304 Not Modified
   - 4xx Client Error: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
   - 5xx Server Error: 500 Internal Error, 502 Bad Gateway, 503 Service Unavailable

5. Cybersecurity Applications:
   - Threat intelligence API queries
   - IoC (Indicator of Compromise) lookups
   - Vulnerability scanning
   - Log collection from remote systems
   - Automated security reporting
   - SIEM integration via REST APIs

6. Error Handling:
   - requests.exceptions.Timeout - request timed out
   - requests.exceptions.ConnectionError - connection failed
   - requests.exceptions.HTTPError - HTTP error occurred
   - requests.exceptions.RequestException - catch-all exception

7. Advanced Features:
   - Proxies: requests.get(url, proxies={'http': 'proxy.com:8080'})
   - SSL Verification: requests.get(url, verify=False) # Not recommended
   - File uploads: files={'file': open('file.txt', 'rb')}
   - Streaming: response = requests.get(url, stream=True)

Remember: Always validate and sanitize data received from external APIs!
The requests library is essential for modern cybersecurity automation.
"""
