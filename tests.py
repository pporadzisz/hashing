import pytest
from hashing import Hashing

def test_hashing_short_password():
    password = "a82aff09"
    with pytest.raises(Exception):
        Hashing.create_hash(password=password)

def test_hashing_short_salt():
    salt = "a82a888"
    with pytest.raises(Exception):
        Hashing.create_hash(salt=salt)

def test_hashing_less_iterations():
    iterations = 99
    with pytest.raises(Exception):
        Hashing.create_hash(iterations=iterations)

@pytest.mark.parametrize(
    "password, salt, iterations",
    [
        ("LHjzPxxqBQywKkXDLH9f","a7jSw91dYNUEGjbS3PX9CJAnQh461xs3",100),
        ("pHjzPxxqBQywKkXDLH9f","a7jSw91dYNUEGjbS3PX9CJAnQh461xs2",150)
    ]   
)
def test_hash_is_created(password, salt, iterations):
    Hashing.create_hash(password=password, salt=salt, iterations=iterations)
    assert len(Hashing.create_hash(password=password, salt=salt, iterations=iterations))==4

def test_hash_is_created2_without_parameters():
    assert len(Hashing.create_hash())==4