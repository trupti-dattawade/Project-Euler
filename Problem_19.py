"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import datetime, timedelta
start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
sunday_count = 0
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() == 6:  # Sunday
        sunday_count += 1
    current_date = current_date.replace(day=1) + timedelta(days=32)  # Move to the first of the next month
    current_date = current_date.replace(day=1)  # Ensure it's the first of the month

if __name__ == "__main__":
    print(sunday_count)

#output: 171