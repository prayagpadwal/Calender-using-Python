def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1998, 9, 3)


# In the above code:

# 1. I have first defined a Python function where I am asking for three user inputs:
#       y: year of birth 
#       m: month of birth 
#       d: date of birth
# 2. Then I am importing the datetime module in Python inside the function
# 3. Then in the next line, I am taking today’s date by using the datetime.now() method of the datetime module
# 4. Then I have introduced a new variable in the next line as dob, where I am using the date of birth as the input given by the user
# 5. Then I am subtracting the dob with today’s date and then dividing it by 365.25 which is returning the age of the user.
