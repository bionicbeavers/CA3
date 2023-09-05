from calculator import  multiply, sub

def test_multiply(): 
    assert multiply(2,6) == 12 
    assert multiply(2.5,-5) == -12.5 
    assert multiply(3,6) == 18
    assert multiply(3,7) == 21
    assert multiply(3,9) == 27

def test_sub():
    assert sub(2,6) == -4
    assert sub(2.5,-5) == 7.5
    assert sub(3,6) == -3
    assert sub(3,7) == -4
    assert sub(3,9) == -6