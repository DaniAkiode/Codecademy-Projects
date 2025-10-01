from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os 
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)

# initialise DB if it does not exist 

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS jobs (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              company TEXT NOT NULL,
              position TEXT NOT NULL,
              email TEXT NOT NULL,
              date_applied TEXT NOT NULL,
              status TEXT DEFAULT 'Pending'
              )""")
    conn.commit()
    conn.close()

def send_email(company, position, recipient_email):
    sender_email = os.getenv("EMAIL_USER")
    sender_pass = os.getenv("EMAIL_PASS")

    subject = f"Application for {position} at {company}"
    body = f"""
    Dear {company} Team,

    I wanted to follow up and let you know that I have submitted my application for the {position} role at your company.

    I look forward to hearing from you.

    Best regards,
    [Your Name]

    """

    # create message 

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email send successfully")
    except Exception as e:
        print("Error sending email", e)


@app.route("/")
def index():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM jobs")
    jobs = c.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

@app.route("/add", methods=["GET", "POST"])
def add_job():
    if request.method == "POST":
        company = request.form["company"]
        position = request.form["position"]
        email = request.form["email"]
        date_applied = datetime.now().strftime("%Y-%m-%d")

        # Save job in BD

        conn = sqlite3.connect("jobs.db")
        c = conn.cursor()
        c.execute("INSERT INTO jobs (company, position, email, date_applied) VALUES (?, ?, ?, ?)", (company, position, email, date_applied))
        conn.commit()
        conn.close()

        # Send follow-up email 
        send_email(company, position, email)

        return redirect("/")
    return render_template("add_job.html")

@app.route("/update/<int:job_id>", methods=["GET", "POST"])
def update_job(job_id):
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()

    if request.method == "POST":
        
        company = request.form['company']
        position = request.form['position']
        status = request.form['status']
        
        c.execute("UPDATE jobs SET company = ?, position = ?, status = ? WHERE id = ?", (company, position, status, job_id))
        conn.commit()
        conn.close()
        return redirect("/")
    
    # Fetch job for form 
    c.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
    job = c.fetchone()
    conn.close()
    return render_template("update_job.html", job=job)

@app.route("/delete/<int:job_id>", methods=["POST"])
def delete_job(job_id):
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("DELETE FROM jobs WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

