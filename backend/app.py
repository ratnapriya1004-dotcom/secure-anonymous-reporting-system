from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # session security

# ---------------- MYSQL CONFIG ----------------
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ratna@2005',
    'database': 'secure_reporting'
}

# ---------------- FILE UPLOAD CONFIG ----------------
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- ADMIN LOGIN (HASHED PASSWORD) ----------------
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM admin WHERE username=%s", (username,))
        admin = cursor.fetchone()

        cursor.close()
        conn.close()

        if admin and check_password_hash(admin['password'], password):
            session['user_role'] = 'admin'
            session['username'] = username
            return redirect(url_for('admin_dashboard'))

        return render_template('admin_login.html', error="Invalid username or password")

    return render_template('admin_login.html')

# ---------------- ADMIN DASHBOARD ----------------
@app.route('/admin/dashboard')
def admin_dashboard():
    if 'user_role' not in session or session['user_role'] != 'admin':
        return redirect(url_for('admin_login'))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reports ORDER BY submitted_at DESC")
    reports = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('admin_dashboard.html', reports=reports)

# ---------------- VIEW SINGLE REPORT ----------------
@app.route('/admin/report/<int:report_id>')
def view_report(report_id):
    if 'user_role' not in session or session['user_role'] != 'admin':
        return redirect(url_for('admin_login'))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reports WHERE id=%s", (report_id,))
    report = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('admin_view_report.html', report=report)

# ---------------- UPDATE REPORT STATUS ----------------
@app.route('/admin/report/update/<int:report_id>')
def update_report_status(report_id):
    if 'user_role' not in session or session['user_role'] != 'admin':
        return redirect(url_for('admin_login'))

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE reports SET status='Resolved' WHERE id=%s",
        (report_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('admin_dashboard'))

# ---------------- ADMIN LOGOUT ----------------
@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))

# ---------------- REPORT SUBMISSION (ANONYMOUS) ----------------
@app.route('/report', methods=['GET', 'POST'])
def submit_report():
    if request.method == 'POST':
        report_type = request.form['report_type']
        description = request.form['description']

        file = request.files.get('evidence')
        filename = None

        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO reports (report_type, description, evidence_file, status)
            VALUES (%s, %s, %s, 'Pending')
            """,
            (report_type, description, filename)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('submit_report', success='1'))

    success = request.args.get('success')
    return render_template('report.html', success=success)

# ---------------- SERVE UPLOADED FILES ----------------
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
