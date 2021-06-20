import sys

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <passwords>")
else:
    password = sys.argv[1]
    print("Password", password)
