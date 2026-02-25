from datetime import datetime

while True:
    try:
        birth_str = input("Enter birth date(\"2026-01-01\"):")
        birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
        break
    except ValueError:
        print ('Invalid date format')

today = datetime.today()

age = today - birth_date

days = age.days
hours = days * 24
seconds = days * 24 * 3600
months = days // 30   # approximate
years = days // 365   # approximate

print(f"You are approximately {years} years old.")
print(f"Equals to {months} months, {days} days, {hours} hours, {seconds} seconds.")