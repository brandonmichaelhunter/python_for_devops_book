# Exercise 3: Use fire to access methods in an existing Python script from the command line
import sys
import fire 

def greet(name="World"):
    return f"Hello, {name}!"

def add(a: int, b: int):
    return a + b

if __name__ == '__main__':
    fire.Fire()
