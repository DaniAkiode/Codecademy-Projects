import joblib
#Load vectorizers
cv = joblib.load("models/cv5.pkl")
tfidf = joblib.load("models/tfidf3.pkl")

# Load multiple models along with respected vectorizers 
models = {
    "naive_bayes": (cv, joblib.load("models/nb_spam_model5.pkl")),
    "logic_regression": (cv, joblib.load("models/lr_spam_model5.pkl")),
    "KNeighborsClassifier": (tfidf, joblib.load("models/knn_spam_model3.pkl"))
}

def predict_message(text, model_name="naive_bayes"):  # declare predict_ function for predicting the message 
    if model_name not in models: 
        return "Invalid model selected!" #Display the message if the models are not in the list 
    vectorizer, model = models[model_name]  # Get selected model, assigns "vectorizer" and "model" to the selected model along with the vectorzier being used   
    text_vector = vectorizer.transform([text])  # Convert text to numerical format for the program to understand the text 
    prediction = model.predict(text_vector)  # Make a prediction    
    if prediction == 1: #If the prediction is spam then send the message below 
        return "This is Spam! Delete Email at ONCE!"
    else:# if the prediction is ham send the message below 
        return "This is Ham! Keep the email! (Could be important!)"

def predict_bulk_messages(messages, model_name="naive_bayes"):
    if model_name not in models:
        return ["Invalid model selected!"] * len(messages)  # Return error message for each message if model is not valid

    vectorizer, model = models[model_name]  # Get selected model and vectorizer
    messages_vector = vectorizer.transform(messages)  # Convert all messages to numerical format
    predictions = model.predict(messages_vector)  # Make predictions for all messages


    # Convert numeric predctions to human-readable format

    readable = []
    for pred in predictions:
        if pred == 1:
            readable.append("This is Spam! Delete Email at ONCE!")
        else:
            readable.append("This is Ham! Keep the email! (Could be important!)")

    return readable  # Return list of predictions for each message



"""model = joblib.load("NBSpamDetector3.pkl") # Load model

vectorizer = joblib.load("cv3.pkl") # Load vectoriser 

def predict_spam(text): #Define spam preditcting function

    text_vector = vectorizer.transform([text]) # convert text to numerical format
    prediction = model.predict(text_vector) # Make a prediction 
    if prediction == 1:
        return "This is Spam! Delete Email at ONCE!" # Return string, displayed in the HTML 
    else:
        return "This is Ham! Keep the email! (Could be important!) "  # Return string, displayed in the HTML 

"""
