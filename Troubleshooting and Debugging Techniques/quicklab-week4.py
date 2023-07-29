#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def download_data(url):
    """Downloads the file from the given URL and returns its content as a list of lines."""
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def preprocess_data(lines):
    """Preprocesses the data and creates a dictionary with start dates as keys and employees as values."""
    data = csv.reader(lines[1:])
    employee_dict = {}
    for row in data:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        employee = "{} {}".format(row[0], row[1])

        if row_date in employee_dict:
            employee_dict[row_date].append(employee)
        else:
            employee_dict[row_date] = [employee]

    return employee_dict

def list_newer(start_date, employee_dict):
    while start_date < datetime.datetime.today():
        if start_date in employee_dict:
            employees = employee_dict[start_date]
            print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    lines = download_data(FILE_URL)
    employee_dict = preprocess_data(lines)
    list_newer(start_date, employee_dict)

if __name__ == "__main__":
    main()