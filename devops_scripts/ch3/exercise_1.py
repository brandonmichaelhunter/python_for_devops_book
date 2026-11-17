

# Exercise - 1
# Use sys to write a script that prints command line only when run from the command line.
import sys    
print('Hello, this script is running from the command line!')
def main() -> None:
    if sys.argv:
        print("command line")
if __name__ == '__main__':
    main()
