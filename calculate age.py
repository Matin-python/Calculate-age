from datetime import datetime

#Calculates how many leap years we have had since the day you were born.
def leap_year(age, year):
    count_leap_year = 0
    for year in range (year - age, year+1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count_leap_year += 1
    return count_leap_year

#Calculates how many days have passed since the day you were born.
def to_days(month):
    day = 0
    for i in range(month-1):
        day += Gregorian_month[i]
    
    days = age * 365 + day + (today_time[2] - 1) + num_leap_year
    return days

#Calculates how many hours have passed since the day you were born.
def to_hours(days):
    hours = days * 24
    return hours

#Calculates how many seconds have passed since the day you were born.
def to_sec(days):
    sec = days * 24 * 3600
    return sec

Gregorian_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Solar_month = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]

today_time = datetime.today().strftime('%Y-%m-%d').split("-")
today_time = [int(item) for item in today_time]

while True:
    temp= int(input("Enter 1 if you want to enter your age and 2 if you want to enter the year you born:"))
    if temp == 1:
        age = int(input("Enter your age:"))
        break
    elif temp == 2:
        age = int(input("Enter the year you were born in Gregorian calendar:"))
        age = today_time[0] - age
        break
    else:
        print('The number you entered is not valid. Try again.')

num_leap_year = leap_year(age, today_time[0])
months = age * 12 + (today_time[1] - 1)
days = to_days(today_time[1])
hours = to_hours(days)
seconds = to_sec(days)

print('You are %d years old.' %(age))
print('Equals to %d months, %d days, %d hours, %d seconds.' %(months, days, hours, seconds))