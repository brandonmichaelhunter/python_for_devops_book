# Exercise 2: Use click to create a command-line tool that takes a name as an argument and prints 
# it if it does not begin with a p.
import sys
import click 

@click.command() # a function should be expsed to a command line access.
@click.argument('name') # the argument is passed to the function as a parameter.
def main(name: str) -> None:
    if not name.lower().startswith('p'):
        print(name)
    else:
        print("The name should not start with 'p'.")

if __name__ == '__main__':
    main() # the function is called when the script is run from the command line.