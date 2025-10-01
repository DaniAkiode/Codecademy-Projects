from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime 

app = Flask(__name__)

# initialise DB if it does not exist 

def init_db():
    conn = sqlite3.connect("jobs.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS jobs (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              company TEXT NOT NULL,
              position TEXT NOT NULL,
              date_applied TEXT NOT NULL,
              status TEXT DEFAULT 'Pending'
              )""")
    conn.commit()
    conn.close()

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
        date_applied = datetime.now().strftime("%Y-%m-%d")

        conn = sqlite3.connect("jobs.db")
        c = conn.cursor()
        c.execute("INSERT INTO jobs (company, position, date_applied) VALUES (?, ?, ?)", (company, position, date_applied))
        conn.commit()
        conn.close()

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

