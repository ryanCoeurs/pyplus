
def my_add(num1, num2):
    return num1 + num2

def my_mult(num1, num2):
    return num1 * num2


def test_my_add():
    assert my_add(1, 1) == 2
    assert my_add(0, 1) == 1
    assert my_add(-1, 1) == 0

def test_my_mult():
    assert my_mult(1, 1) == 1
    assert my_mult(0, 1) == 0
    assert my_mult(-1, 1) == -1
