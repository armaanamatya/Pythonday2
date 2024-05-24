#Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." 
# Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.

import csv

try:
    file = open("data.csv", "r")
    reader = csv.reader(file)
    adults = []
    for row in reader:
        if row:
            name, age = row
            if int(age) >= 18:
                adults.append(row)
    file.close()

    file = open("adults.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerows(adults)
    file.close()

    print("adults.csv file created successfully.")
except:
    print("Error: data.csv file not found.")
    

# Create a function add_to_json that takes a filename and a dictionary as input. 
# The function should read the JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.
import json

filename = input("Filename? ")

def add_to_json(filename, new_data):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(new_data)

    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

new_entry = {"name": "John", "age": 35}
add_to_json(filename, new_entry)

# Create a function search_log that takes a log file and a search keyword as input. 
# The function should find and display all lines containing the search keyword.

def search_log(log_file, keyword):
    try:
        with open(log_file, "r") as file:
            for line in file:
                if keyword in line:
                    print(line)
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
