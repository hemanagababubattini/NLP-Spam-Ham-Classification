import gradio as gr
import pickle

with open("models/spam_ham_model.pkl", "rb") as file:
    model = pickle.load(file)


with open("models/tfidf_vectorizer.pkl", "rb") as file:
    tfidf = pickle.load(file)


def predict_message(message):

    if not message.strip():
        return "Please enter a message!"

    message_vector = tfidf.transform([message])

    prediction = model.predict(message_vector)[0]

    if prediction == 1:
        return "🚨 SPAM MESSAGE"
    else:
        return "✅ HAM MESSAGE"


demo = gr.Interface(
    fn=predict_message,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter your SMS message here..."
    ),
    outputs=gr.Textbox(label="Prediction"),
    title="SMS Spam-Ham Classifier",
    description="Enter a message to identify whether it is Spam or Ham."
)

demo.launch()