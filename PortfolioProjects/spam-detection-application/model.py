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
    
    try:
        proba = model.predict_proba(text_vector)[0][1] 
        spam_score = round(proba * 100, 2)
    except:
        spam_score = "N/A"


    
    
    if prediction == 1: #If the prediction is spam then send the message below 
        label = "This is Spam! Delete Email at ONCE!"
    else:# if the prediction is ham send the message below 
        label =  "This is Ham! Keep the email! (Could be important!)"

    return label, spam_score  # Return label and spam score as a tuple

def predict_bulk_messages(messages, model_name="naive_bayes"):
    if model_name not in models:
        return ["Invalid model selected!"] * len(messages)  # Return error message for each message if model is not valid

    vectorizer, model = models[model_name]  # Get selected model and vectorizer
    messages_vector = vectorizer.transform(messages)  # Convert all messages to numerical format
    predictions = model.predict(messages_vector)  # Make predictions for all messages


    try:
        probabilities = model.predict_proba(messages_vector)[:, 1]  # Get probabilities for spam class
        threat_scores = [round(score * 100, 2 ) for score in probabilities]  # Convert probabilities to threat scores
    except:
        threat_scores = ["N/A"] * len(messages)

    # Convert numeric predctions to human-readable format

    readable = []
    for pred, score in zip(predictions, threat_scores):
        if pred == 1:
            label = "This is Spam! Delete Email at ONCE!"
        else:
            label = "This is Ham! Keep the email! (Could be important!)"
        readable.append((label, score))

    return readable  # Return list of predictions for each message

def custom_spam_filter(text):
    spam_keywords = [
        "free", "winner", "claim", "urgent", "money", "guarantee", "prize",
        "click here", "buy now", "act now", "limited time", "congratulations"
    ]

    score = 0
    for keyword in spam_keywords:
        if keyword in text.lower():
            score += 20

    if score >= 60:
        return "This is Spam! (Custom Filter)" , score
    elif score >= 30:
        return "This is potentially Spam! (Custom Filter)", score
    else:
        return "This is Ham! (Custom Filter)", score
    
    




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
