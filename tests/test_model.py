from main import load_and_preprocess_data, train_model
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))


def test_data_loading():
    data = load_and_preprocess_data()
    assert not data.isnull().sum().any(), "Data contains missing values after preprocessing"


def test_model_accuracy():
    data = load_and_preprocess_data()
    model, accuracy = train_model(data)
    assert accuracy >= 0.75, "Model accuracy is below 75%"
