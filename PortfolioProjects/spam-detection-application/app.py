from flask import Flask, request, render_template # for sending/getting data and 
from model import predict_message # spam detection function
from database import create_table, insert_result  # import database functions 

app = Flask(__name__)

# Create table when app starts 

create_table()

@app.route("/", methods=["GET", "POST"])  # Handles requests in homepage
def index():
    result = None  # Initialize result as None
    selected_model = "naive_bayes"  # Default model

    if request.method == "POST":  # Use POST to send data to the server
        user_input = request.form.get("message")  # Get user input from html file
        selected_model = request.form.get("model")  # Get selected model from html
        save_to_database = request.form.get("SaveToDatabase") # Get option to save data from html file 
        if user_input:  # Make sure input is not empty
            result = predict_message(user_input, selected_model)  # Get prediction with chosen model
            if save_to_database: #If user want to save message to database 
                insert_result(user_input, result, selected_model) # Send results to database if check box has been ticked 
        else:
            result = "No message entered!"  # send message if input is empty
    
    return render_template("index.html", result=result, selected_model=selected_model)  # Pass index.html, result and  selected model through function to make web page dynamic 

if __name__ == "__main__":  # Runs only when this file is executed directly
    app.run(debug=True)  # Enable debug mode



"""
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        message = request.form["message"]
        selected_model = request.form["model"]
        
        # Call function from model.py
        result = predict_spam(message, selected_model)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)"
"""



"""@app.route("/", methods=["GET", "POST"]) #handles requests in homepage 
def index():
    result = None # Initialise result as None 
    if request.method == "POST": # Use POST to send data to the server 
        user_input = request.form.get("message") # Use '.get()' to avoid erros
        if user_input: #Make sure input is not empty
            result = predict_spam(user_input) # Get prediction
            insert_result(user_input, result)
        else:
            result = "No message entered!" # Handle empty input
    return render_template("index.html", result=result) # Render html templete with result

if __name__ == "__main__": # Runs only when this file is executed directly
    app.run(debug=True) # Enable debug mode ""
"""