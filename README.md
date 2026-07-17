# Crop Recommendation System

Crop Recommendation System is a Machine Learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The system helps farmers and agricultural enthusiasts make informed decisions by analyzing factors such as Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.

---

## Features

- **Machine Learning-Based Prediction:** Recommends the most suitable crop using a trained Machine Learning model.
- **Interactive Web Application:** User-friendly interface built with Streamlit for easy input and prediction.
- **Real-Time Recommendations:** Instantly predicts the best crop based on user-provided values.
- **Modern Dashboard:** Attractive UI with responsive cards, agriculture-themed design, and intuitive layout.
- **High Prediction Accuracy:** Naive Bayes model achieving **99.55% accuracy**.
- **Data Visualization & Analysis:** Comprehensive data preprocessing, EDA, and model comparison performed using Jupyter Notebook.

---

## Tech Stack

### Frontend
- Streamlit
- HTML & CSS (Custom Styling)

### Machine Learning
- Python
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Data Visualization
- Matplotlib

---

## Project Structure

```text
Crop-Recommendation-System/
│
├── Dataset/
│   └── Crop_recommendation.csv
│
├── Models/
│   ├── crop_recommendation_model.pkl
│   └── label_encoder.pkl
│
├── Research Papers/
│
├── Jupyter Notebooks/
│
├── Streamlit App/
│   ├── assets/
│   │   └── FarmImage.jpg
│   ├── app.py
│   └── requirements.txt
│
├── requirements.txt
└── README.md
```

---

## Model Performance

The following Machine Learning models were trained and evaluated:

| Model | Accuracy |
|--------|----------|
| Naive Bayes | **99.55%** |
| Random Forest | 99.32% |
| Decision Tree | 98.64% |
| XGBoost | 98.64% |
| Support Vector Machine (SVM) | 96.82% |
| Logistic Regression | 96.36% |
| K-Nearest Neighbors (KNN) | 95.68% |

**Best Performing Model:** Naive Bayes

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.10+
- pip

---

### Installation & Setup

#### Clone the Repository

```bash
git clone https://github.com/mahiich07/Crop-Recommendation-System.git

cd Crop-Recommendation-System
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Application

```bash
cd "Streamlit App"

streamlit run app.py
```

The application will run at:

```
http://localhost:8501
```

---

## Input Features

The model predicts the most suitable crop using:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

---

## Application Preview

<p align="center">
  <img src="images/home-page.png" alt="Crop Recommendation System" width="900">
</p>

---

## Developed By

**Mahi Chaudhary**

B.Tech Artificial Intelligence & Machine Learning  
Indira Gandhi Delhi Technical University for Women (IGDTUW)

---
