# tests/test_basic.py
from app.model import load_model, predict_example

def test_predict_example_runs():
    model = load_model()
    pred = predict_example(model)
    # just check it returns an int / something sane
    print("PRED VALUE =", pred)
    assert isinstance(pred, int)
