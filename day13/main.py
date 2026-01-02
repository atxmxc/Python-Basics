# command line arguements
# instead of the options menu in the project in the to do list, we canrun the script without menus using command line
import argparse
import sys
'(add | view | remove | export | exit)'
# goes to #
'python project.py --export'
'python project.py --add "wash clothes"'
'python project.py --view'
# now we can use a new library, called sys
print(sys.argv)
# however, this is low level and quite messy
['C:\\\\Users\\\\Admin\\\\Documents\\\\PythonBasics\\\\day13\\\\main.py',
    'hello', 'world']  # output
# instead we use argparse
parser = argparse.ArgumentParser(description="First CLI Tool")

parser.add_argument("--name", help="Your Name")
parser.add_argument("--age", help="your age")

args = parser.parse_args()

if args.name:
    print(f"Hello {args.name}")

if args.age:
    print(f"You are {args.age} years old")

# Flags vs Values
'--export'  # this is a flag, meaning it only has True or False
'-add "wash"'  # this is a value arguements as it takes an input
