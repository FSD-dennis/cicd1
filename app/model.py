# app/model.py
from pathlib import Path
import joblib

MODEL_PATH = Path("models/model.joblib")

def load_model():
    """
    Load model from local file. In CI we train and save this.
    In production, you might download from S3 then load.
    """
    if not MODEL_PATH.exists():
        # Fallback dummy model
        class DummyModel:
            def predict(self, X):
                return [42] * len(X)

        print("WARNING: Model file not found, using DummyModel.")
        return DummyModel()

    print(f"Loading model from {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

def predict_example(model):
    """
    Just an example prediction to prove the pipeline works.
    """
    y_pred = model.predict([[1, 2, 3, 4]])  # shape (1, 4)
    return int(y_pred[0])