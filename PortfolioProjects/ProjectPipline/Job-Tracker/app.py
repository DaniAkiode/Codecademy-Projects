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

if __name__ == "__main__":
    init_db()
    app.run(debug=True)


    
