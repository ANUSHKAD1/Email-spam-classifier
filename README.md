# 📧 Email Spam Classifier using Machine Learning

## 📌 Project Overview

The Email Spam Classifier is a Machine Learning web application that detects whether an email or message is **SPAM** or **NOT SPAM**.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to analyze email text and classify it accurately.

The application is built using:

* Python
* Flask
* Scikit-learn
* HTML
* CSS

---

# 🚀 Features

* Detects spam emails instantly
* Machine Learning based prediction
* Confidence score display
* Modern responsive web interface
* Simple and user-friendly design
* Fast and accurate predictions

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

## Other Libraries

* Pandas
* Joblib

---

# 📂 Project Structure

```bash
email-spam-classifier/
│
├── data/
│   └── spam.csv
│
├── model/
│   └── spam_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

# 🖼️ Project Screenshots

## Landing Page

![Landing Page](images/landing-page.png)

---

## Input Screen

![Input Screen](images/input-screen.png)

---

## Output Screen

![Output Screen](images/output-screen.png)
# 📊 Dataset

Dataset used:

* SMS Spam Collection Dataset

Dataset Source:

* Kaggle

The dataset contains:

* Spam messages
* Ham (Not Spam) messages

---

# ⚙️ Machine Learning Workflow

## Step 1: Data Collection

The spam dataset is downloaded from Kaggle.

## Step 2: Data Preprocessing

* Removed unnecessary columns
* Converted labels into numerical values
* Cleaned text data

## Step 3: Feature Extraction

TF-IDF Vectorizer converts text into numerical vectors.

## Step 4: Model Training

Logistic Regression algorithm is used for classification.

## Step 5: Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score

## Step 6: Deployment

The trained model is integrated into a Flask web application.

---

# 📈 Accuracy

The model achieves high accuracy on the test dataset.

Approximate Accuracy:

```bash
97% - 99%
```

---

# ▶️ How to Run the Project

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-link>
```

---

## Step 2: Open Project Folder

```bash
cd email-spam-classifier
```

---

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
.\venv\Scripts\Activate.ps1
```

---

## Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5: Train the Model

```bash
python train_model.py
```

---

## Step 6: Run Flask Application

```bash
python app.py
```

---

## Step 7: Open Browser

Open:

```bash
http://127.0.0.1:5000
```

---

# 🖥️ Application Screens

## Landing Page

* Project introduction
* Navigation bar
* Hero section

## Input Screen

* User enters email content
* Clicks "Classify Email"

## Output Screen

* Displays:

  * SPAM or NOT SPAM
  * Confidence Score

---

# 📚 Concepts Used

* Natural Language Processing (NLP)
* Machine Learning Classification
* TF-IDF Vectorization
* Logistic Regression
* Web Development using Flask

---

# 🔮 Future Improvements

* Add Deep Learning models
* Add User Authentication
* Store prediction history
* Deploy online using Render or Heroku
* Add dark mode
* Add email attachment analysis

---

# 👨‍💻 Author

**Anushka Daflapurkar**

B.E Final Year Student
Python Full Stack & Machine Learning Enthusiast

---

# 📌 Conclusion

This project demonstrates how Machine Learning and NLP can be used to detect spam emails automatically. The system provides accurate predictions with a simple and interactive web interface. It is a beginner-friendly project that helps in understanding real-world applications of Machine Learning.
