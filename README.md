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

1. **secure-anonymous-reporting-system**
2. **backend**
3. `app.py` – Main Flask application file
4. **templates**
5. `index.html` – Home page
6. `report.html` – Report submission page
7. `admin_login.html` – Admin login page
8. `admin_dashboard.html` – Admin dashboard
9. `admin_view_report.html` – Page to view submitted reports
10. **static**
11. `style.css` – Styling for the website
12. `script.js` – JavaScript functionality
13. **uploads** – Folder used to store uploaded evidence files

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