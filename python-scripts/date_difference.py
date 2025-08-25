#!/usr/bin/env python3

# date_difference.py
# Calculates the difference between two dates.

from datetime import datetime
import sys


def main(first_date_str, second_date_str):
    try:
        # Convert input to datetime objects
        date1 = datetime.strptime(first_date_str, "%d-%m-%Y")
        date2 = datetime.strptime(second_date_str, "%d-%m-%Y")

        difference = (date2 - date1)

        print(f"The difference is {difference.days} days")

    except Exception as e:
        print(f"There was an error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    if sys.argv[1] == "--help":
        print("Usage: date_difference.py <first_date> <second_date>")
        print("Dates should be in format 'day-month-year'")
        sys.exit()
    main(sys.argv[1], sys.argv[2])
