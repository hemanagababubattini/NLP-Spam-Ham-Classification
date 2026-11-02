# SMS Spam-Ham Classification Using Machine Learning

## Project Overview
This project focuses on classifying SMS messages as **Spam** or **Ham (Not Spam)** using Machine Learning techniques and Natural Language Processing (NLP).

The model analyzes the text message and predicts whether it is a spam message or a legitimate message.

## Objectives
- Clean and preprocess raw SMS text data.
- Perform Exploratory Data Analysis (EDA).
- Convert text into numerical features using TF-IDF.
- Train and evaluate Machine Learning models.
- Save the trained model for future predictions.
- Deploy the model using a Gradio web interface.

## Dataset
- Dataset: SMS Spam Collection Dataset
- Original records: 5,572
- Records after removing duplicates: 5,169
- Classes: Ham and Spam

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- TF-IDF
- Gradio
- Jupyter Notebook

## Project Workflow
1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis
4. Text Preprocessing
   - Lowercase Conversion
   - Punctuation Removal
   - Tokenization
   - Stopword Removal
   - Stemming
5. Feature Extraction using TF-IDF
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Saving using Pickle
10. Deployment using Gradio

## Machine Learning Models
Two classification algorithms were trained and compared:

| Model | Accuracy |
|---|---:|
| Multinomial Naive Bayes | 97.68% |
| Random Forest Classifier | 98.16% |

**Best Model:** Random Forest Classifier

The Random Forest model achieved 98.16% accuracy and a 0.92 F1-score for the Spam class on the test dataset.

## Project Structure
```text
NLP_SPAM_HAM_PROJECT/
│
├── dataset/
│   └── spam.csv
│
├── notebooks/
│   └── spam_ham_classification.ipynb
│
├── models/
│   ├── spam_ham_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the Repository
```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder
```bash
cd NLP_SPAM_HAM_PROJECT
```

### 3. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn gradio jupyter
```

### 4. Run the Application
```bash
python app.py
```

Open the local Gradio URL displayed in the terminal.

Enter an SMS message to predict whether it is Spam or Ham.

## Sample Predictions

| SMS Message | Prediction |
|---|---|
| Congratulations! You won a free prize. Claim now | SPAM |
| Hey, are you coming to college today? | HAM |
| URGENT! You have won 1000 pounds. Call now | SPAM |

## Conclusion
This project demonstrates how Natural Language Processing and Machine Learning can be used to identify spam messages. The trained Random Forest model achieved 98.16% test accuracy and was successfully integrated into a Gradio application for interactive predictions.

## Future Enhancements
- Improve spam detection using advanced NLP techniques.
- Experiment with deep learning models.
- Test the model with more real-world SMS messages.
- Deploy the application online.

---
**Project:** SMS Spam-Ham Classification  
**Domain:** Natural Language Processing (NLP) | Machine Learning