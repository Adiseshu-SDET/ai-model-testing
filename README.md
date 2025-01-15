# AI Model Testing Project

This project demonstrates a complete workflow for developing, testing, and deploying an AI model. The primary objective is to build and test a machine learning model, expose it via a REST API, and automate the entire process using CI/CD pipelines. Below is a detailed summary of the work done.

---

## **Table of Contents**
1. [Project Description](#project-description)
2. [Setup Instructions](#setup-instructions)
3. [Key Features](#key-features)
4. [Step-by-Step Workflow](#step-by-step-workflow)
5. [CI/CD Pipeline](#cicd-pipeline)
6. [API Usage](#api-usage)
7. [Technologies Used](#technologies-used)

---

## **Project Description**
This project involves:
1. Building a machine learning model to predict survival on the Titanic dataset.
2. Automating testing for the model’s functionality and accuracy using PyTest.
3. Exposing the trained model as a REST API using Flask.
4. Containerizing the application using Docker.
5. Automating CI/CD workflows using GitHub Actions.

---

## **Setup Instructions**

### **Pre-requisites**
- Python 3.9 or above
- Docker installed on your machine
- A GitHub account
- Optional: Docker Hub account

### **Setup the Project**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-model-testing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application locally:
   ```bash
   python app.py
   ```

4. Test the application locally:
   ```bash
   pytest
   ```

5. Build and run the Docker container:
   ```bash
   docker build -t ai-model-api .
   docker run -p 5000:5000 ai-model-api
   ```

---

## **Key Features**
- **Machine Learning Model**: Logistic regression on Titanic dataset.
- **Testing**: Automated testing with PyTest.
- **API**: Flask-based REST API for model predictions.
- **Containerization**: Dockerized application.
- **CI/CD**: GitHub Actions for automation.

---

## **Step-by-Step Workflow**

### **1. Data Loading and Preprocessing**
- Loaded the Titanic dataset.
- Cleaned data by handling missing values and encoding categorical variables.
- Prepared the data for training.

### **2. Model Training and Evaluation**
- Trained a logistic regression model.
- Evaluated accuracy to ensure the model meets performance criteria.

### **3. Automated Testing**
- Wrote PyTest scripts to:
  - Validate data preprocessing.
  - Ensure model accuracy meets thresholds.
- Integrated tests into the CI/CD pipeline.

### **4. Exposing the Model as an API**
- Created a Flask REST API with an endpoint to make predictions.
- Tested the API locally with tools like Postman and cURL.

### **5. Dockerization**
- Wrote a Dockerfile to containerize the application.
- Built and ran the Docker container locally.
- Pushed the container image to Docker Hub.

### **6. CI/CD Pipeline**
- Configured GitHub Actions to:
  - Run automated tests.
  - Generate and upload test/coverage reports.
  - Build and push the Docker image to Docker Hub.
- Verified the pipeline’s success on every commit.

---

## **CI/CD Pipeline**

The GitHub Actions pipeline automates the following steps:

1. **Checkout Code**:
   - Clones the repository.
2. **Set Up Python**:
   - Installs dependencies from `requirements.txt`.
3. **Run Tests**:
   - Executes PyTest scripts.
   - Generates test and coverage reports.
4. **Build and Push Docker Image**:
   - Logs into Docker Hub using GitHub secrets.
   - Builds and pushes the Docker image.

---

## **API Usage**

### **Endpoint**
- **URL**: `http://<host>:5000/predict`
- **Method**: POST

### **Input Example**
```json
{
  "Pclass": 3,
  "Sex": 1,
  "Age": 25,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": 2
}
```

### **Response Example**
```json
{
  "prediction": 0
}
```

---

## **Technologies Used**
- **Programming Language**: Python 3.9
- **Libraries**: Flask, Scikit-learn, PyTest
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

---

### **Next Steps**
1. Explore AI model testing techniques:
   - Functional testing.
   - Performance testing.
   - Bias and fairness testing.
2. Deploy the container on a cloud platform.
3. Integrate notifications into the CI/CD pipeline.

---
