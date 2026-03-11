# Secure & Anonymous Public Reporting System

A web-based platform that allows users to report cyber incidents anonymously.  
Administrators can securely review and manage submitted reports.

## Features
- Anonymous cyber incident reporting
- Admin login and dashboard
- Evidence upload support
- Role-based access control
- Secure backend using Flask
- MySQL database integration

## Technologies Used
- Python (Flask)
- HTML
- CSS
- JavaScript
- MySQL
- Git & GitHub

## Project Structure

secure-anonymous-reporting-system
│
└── backend
    ├── app.py
    ├── templates
    │   ├── index.html
    │   ├── report.html
    │   ├── admin_login.html
    │   ├── admin_dashboard.html
    │   └── admin_view_report.html
    │
    ├── static
    │   ├── style.css
    │   └── script.js
    │
    └── uploads

## How to Run the Project

1. Install Python (3.11 or above)

2. Install required libraries

pip install flask  
pip install mysql-connector-python

3. Run the Flask server

python app.py

4. Open browser

http://127.0.0.1:5000

## Admin Login Credentials

Username: admin  
Password: admin123