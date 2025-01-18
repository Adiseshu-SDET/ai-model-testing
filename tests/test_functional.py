import pytest
from main import load_and_preprocess_data, train_model
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import load_and_preprocess_data, train_model


@pytest.fixture
def model():
    # Load data and train the model
    data = load_and_preprocess_data()
    model, _ = train_model(data)  # Unpack model and ignore accuracy
    return model

def test_valid_input(model):
    # Match the training features
    input_data = pd.DataFrame([{
        "Pclass": 1,
        "Sex": 1,
        "Age": 29,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 100,
        "Embarked_1": 1,
        "Embarked_2": 0
    }])
    prediction = model.predict(input_data)
    assert prediction in [[0], [1]], "Prediction should be 0 or 1"


def test_invalid_input(model):
    # Invalid input data (missing columns)
    input_data = pd.DataFrame([{
        "Pclass": 1,
        "Sex": 1,
        "Age": 29
    }])
    with pytest.raises(Exception):
        model.predict(input_data)

def test_edge_case_input(model):
    # Ensure input matches the training features
    input_data = pd.DataFrame([{
        "Pclass": 3,
        "Age": 1,       # Minimum age
        "SibSp": 8,     # Maximum siblings/spouse
        "Parch": 8,     # Maximum parents/children
        "Fare": 512.3,  # High fare value
        "Sex_male": 0,  # One-hot encoded column
        "Embarked_Q": 0,  # One-hot encoded column
        "Embarked_S": 1   # One-hot encoded column
    }])
    prediction = model.predict(input_data)
    assert prediction in [[0], [1]], "Prediction should be 0 or 1"