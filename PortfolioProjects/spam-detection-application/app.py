from flask import Flask, request, render_template, send_file # for sending/getting data and 
from model import predict_message, predict_bulk_messages # spam detection function
from database import create_table, insert_result  # import database functions 
import uuid # for generating unique IDs
import pandas as pd  # for handling CSV files

app = Flask(__name__)

# Create table when app starts 

create_table()

@app.route("/", methods=["GET", "POST"])  # Handles requests in homepage
def index():
    result = None  # Initialize result as None
    selected_model = "naive_bayes"  # Default model

    if request.method == "POST":  # Use POST to send data to the server
        user_input = request.form.get("message")  # Get user input from html file
        uploaded_file = request.files.get("file")
        selected_model = request.form.get("model")  # Get selected model from html
        save_to_database = request.form.get("SaveToDatabase") # Get option to save data from html file 
        
        if not user_input and uploaded_file and uploaded_file.filename.endswith(".txt"):
            # If a file is uploaded, read its content
            user_input = uploaded_file.read().decode("utf-8")
        
        if user_input:  # Make sure input is not empty
            result = predict_message(user_input, selected_model)  # Get prediction with chosen model
            if save_to_database:  # If user want to save message to database
                insert_result(user_input, result, selected_model)  # Send results to database if check box has been ticked
        else:
            result = "No message entered!"  # send message if input is empty
    
    return render_template("index.html", result=result, selected_model=selected_model)  # Pass index.html, result and  selected model through function to make web page dynamic 

@app.route("/bulk_predict", methods=["POST"])  
def bulk_predict():
    file = request.files.get("csv_file")  # Get the uploaded file
    selected_model = request.form.get("bulk_model")

    if not file or not file.filename.endswith(".csv"):
        return "Please upload a valid CSV file."
    
    try:
        df = pd.read_csv(file)  
        if "message" not in df.columns:
            return "CSV file must contain a 'message' column."
        
        predictions = predict_bulk_messages(df["message"], selected_model)  # Get predictions for all messages
        df["prediction"] = predictions  # Add predictions to DataFrame

        output_file = f"static/bulk_results_{uuid.uuid4()}.csv"  # Create a unique output file name
        df.to_csv(output_file, index=False)  # Save DataFrame to CSV

        return send_file(output_file, as_attachment=True)  # Send the file for download
    
    except Exception as e:
        return f"Error processing file: {str(e)}"


    

    

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