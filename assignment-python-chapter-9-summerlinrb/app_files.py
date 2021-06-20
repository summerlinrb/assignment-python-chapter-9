from pathlib import Path
import csv
import json


# Chapter 9.6 - WOrking with CSV files
print("\n9.6 - Working with CSV Files" + "-" * 20)

# create a csv file
with open("data.csv", "w") as file:
    writer = csv.writer(file)
    # write column names
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])

"""
On windows, the code for 9.6 adds a blank line aftger every row.
Use newline = '' argument to prevent this as follows.
"""
with open("data_noblanklines.csv", "w", newline='') as file:
    writer = csv.writer(file)
    # write the column names
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1000, 2, 15])

# read content from a csv file
print("read all content from a csv file")
with open("data.csv") as file:
    reader = csv.reader(file)
    # often we need to work with lits or tuple.
    # convert the reader object to a list.
    data = list(reader)
    print(data)
    # or convert the reader object to a tuple.
    #data = tuple(reader)


print("read each row from a csv file")
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Chapter 9.7 - Working with JSON files
print("\n9.6 Working with JSON files" + "-" * 20)
# create a list containing a dictionary of key:value pairs
movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}
]

# call .dumps() to format the list into JSON formatted string
data = json.dumps(movies)
# write the JSON formatted string to a file
Path("moves.json").write_text(data)


# read data from a JSON file
data = Path("moves.json").read_text()
movies = json.loads(data)
print(movies[0])
print(movies[1])
"""
How do you get a value from a dictionary embeded inside a list?
    movies[] is a list. movies[1] gets the second item in the list
    which is a dictionary obkject in this case
    .get('key_name') will return a value of a key from a dictionary object
    Specify the key_name.
"""
print(f"In what year was Kindergarten Cop released? {movies[1].get('year')}")

# How to loop through a list of dictionaries, one of many ways
for movie in movies:
    print(
        f"The movie, {movie.get('title')} was released in {movie.get('year')}")
