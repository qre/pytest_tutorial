


def test_pass():
    assert 1 + 1 == 2

def test_fail():
    assert 2 + 2 == 5

def greet(person):
    return "Hi {name}".format(**person)

def test_greet():
    bob = {"name": "Bob"} # Arrange
    greeting = greet(bob) # Act
    assert greeting == "Hi Bob" # Assert
