from datetime import datetime

#Calculates how many leap years we have had since the day you were born.
def leap_year(age, year):
    count_leap_year = 0
    for year in range (year - age[0], year+1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            count_leap_year += 1
    return count_leap_year

#Calculates how many days have passed since the day you were born.
def to_days(age):
    day = 0
    for i in range(age[1]):
        day += Gregorian_month[-i]
    
    days = age[0] * 365 + day + age[2] + num_leap_year
    return days

#Calculates how many hours have passed since the day you were born.
def to_hours(days):
    hours = days * 24
    return hours

#Calculates how many seconds have passed since the day you were born.
def to_sec(days):
    sec = days * 24 * 3600
    return sec

#Calculates your age.
def calculate_age(age):
    age[0] = today_time[0] - age[0]
    age[1] = today_time[1] - age[1]
    age[2] = today_time[2] - age[2]
    if age[2] < 0 :
        age [1] -= 1
        age [2] += 30 
    if age[1] < 0 :
        age [0] -= 1
        age [1] += 12
    return age


Gregorian_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
age = [0]

today_time = datetime.today().strftime('%Y-%m-%d').split("-")
today_time = [int(item) for item in today_time]

while True:
    temp= int(input("Enter 1 if you want to enter your age and 2 if you want to enter the time you were born:"))
    if temp == 1:
        age[0] = int(input("Enter your age:"))
        break
    elif temp == 2:
        while True:
            age = input("Enter the time you were born in Gregorian calendar(\"2026-01-01\"):").split("-")
            if len(age) == 3 and all(part.isdigit() for part in age):
                year, month, day = map(int, age)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    age = [int(item) for item in age]
                    age = calculate_age(age)
                    break
                else:
                    print("Invalid month or day. Please try again")
            else:
                print("Invalid format.")
        break
    else:
        print('The number you entered is not valid. Try again.')

num_leap_year = leap_year(age, today_time[0])
months = age[0] * 12 + age[1]
days = to_days(age)
hours = to_hours(days)
seconds = to_sec(days)

print('You are %d years and %d month and %d days old.' %(age[0], age[1], age[2]))
print('Equals to %d months, %d days, %d hours, %d seconds.' %(months, days, hours, seconds))