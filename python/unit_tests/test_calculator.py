"""
from i_calculator import square

def main():
    test_square()

def test_square():
    if square(2)!=4:
        print("2 square not 4")
    if square(3)!=9:
        print("3 square not 9")
    #we can also use assertion
    try:
        assert square(2) == 4
    except AssertionError:
        print("square of 2 not 4")
    try:
        assert square(3) == 9
    except:
        print("square of 3 not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("square of -2 not 4")
    try:
        assert square(-3) == 9
    except:
        print("square of -3 not 9")
    try:
        assert square(0) == 0
    except:
        print("square of 0 not 0")

if __name__ == "__main__":
    main()
"""
from i_calculator import square

def test_positive():
    assert square(1)==1
    assert square(2)==4
    
    
def test_negative():    
    assert square(-1)==1
    assert square(-2)==4

def test_zero():
    assert square(0)==0
