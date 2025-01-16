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
    model, _ = train_model(data)
    return model

def test_valid_input(model):
    # Valid input data
    input_data = pd.DataFrame([{
        "Pclass": 1,
        "Sex": 1,
        "Age": 29,
        "SibSp": 0,
        "Parch": 0,
        "Fare": 100,
        "Embarked": 1
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
    # Edge case: Minimum and maximum values
    input_data = pd.DataFrame([{
        "Pclass": 3,
        "Sex": 0,
        "Age": 1,      # Minimum age
        "SibSp": 8,    # Maximum siblings/spouse
        "Parch": 8,    # Maximum parents/children
        "Fare": 512.3, # High fare value
        "Embarked": 3  # Unusual embarkation
    }])
    prediction = model.predict(input_data)
    assert prediction in [[0], [1]], "Prediction should be 0 or 1"