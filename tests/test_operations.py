from app.operations import addition,subtraction,multiplication,division


def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(5, 3) == 2

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division():
    assert division(6, 3) == 2
    try:
        division(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

    
        
