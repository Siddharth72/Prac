## Question 1: Age Classification
age = int(input('Enter the age : '))

if age <= 12:
    print(f'Child : {age}')
elif age <= 18:
    print(f'Teen : {age}')
else:
    print(f'Adult : {age}')

## Question 2: Grade Determination

grade = int(input('Enter the grade :'))

if grade >= 90  and grade <= 100:
    print(f'Grade A : {grade}')
elif grade >= 80 and grade < 90:
    print(f'Grade B : {grade}')
elif grade >= 70 and grade < 80:
    print(f'Grade C : {grade}')
elif grade >= 60 and grade < 70:
    print(f'Grade D : {grade}')
elif grade >= 50 and grade < 60:
    print(f'Grade E : {grade}')
else:
    print(f'Grade F : {grade}')

## Question 3: Day of the Week

day_of_the_week = {1 : 'Monday',
                   2 : 'Tuesday',
                   3 : 'Wednesday',
                   4 : 'Thursday',
                   5 : 'Friday',
                   6 : 'Saturday',
                   7 : 'Sunday'}

day = int(input('Enter the day value : '))

day_name = day_of_the_week.get(day)

print(f'Day of the week : {day,day_name}')

if day == 1:
    print(f'Day of the week : {day,day_name}')
elif day == 2:
    print(f'Day of the week : {day,day_name}')
elif day == 3:
    print(f'Day of the week : {day,day_name}')
elif day == 4:
    print(f'Day of the week : {day,day_name}')
elif day == 5:
    print(f'Day of the week : {day,day_name}')
elif day == 6:
    print(f'Day of the week : {day,day_name}')
elif day == 7:
    print(f'Day of the week : {day,day_name}')
else:
    print(f'Invalid input : {day}')

## Question 4: Triangle Type

a_side = int(input('Enter side 1 : '))
b_side = int(input('Enter side 2 : '))
c_side = int(input('Enter side 3 : '))

if a_side == b_side == c_side:
    print(f'Equilatertal triangle -- a : {a_side} -- b : {b_side} -- c : {c_side} ')
elif a_side == b_side or b_side == c_side or c_side == a_side:
    print(f'Isosceles triangle -- a : {a_side} -- b : {b_side} -- c : {c_side} ')
else:
    print(f'Scalene triangle -- a : {a_side} -- b : {b_side} -- c : {c_side} ')

## Question 5: Simple Calculator

operator = input('Enter the operator function : ')
num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))

if operator == '+':
    print(f'Addition operator : {num1,num2} : {num1+num2}')
elif operator == '-':
    print(f'Subtration operator : {num1,num2} : {num1-num2}')
elif operator == '*':
    print(f'Multiplication operator : {num1,num2} : {num1*num2}')
elif operator == '/':
    print(f'Division operator : {num1,num2} : {num1/num2}')
else: 
    print(f'Invalid operator : {num1,num2} : {operator}')

## Question 6: Season by Month

months_with_seasons = {1 : 'Winter',
                       2 : 'Winter',
                       3 : 'Summer',
                       4 : 'Summer',
                       5 : 'Summer',
                       6 : 'Summer',
                       7 : 'Rainy Season',
                       8 : 'Rainy Season',
                       9 : 'Rainy Season',
                       10 : 'Autumn',
                       11 : 'Autumn',
                       12 : 'Winter'}

months = int(input('Enter the month : '))

seasons = months_with_seasons.get(months)

if months in [1,12,2]:
    print(f'Month falls under Winter : {months}')
elif months in [3,4,5,6]:
    print(f'Month falls under Summer : {months}')
elif months in [7,8,9]:
    print(f'Month falls under Rainy Season : {months}')
elif months in [10,11]:
    print(f'Month falls under Autumn Season : {months}')
else:
    print(f'Invalid month given (between 1 - 12): {months}')

## Question 7: Love Me, Love Me Not

petals = int(input('Enter the petals : '))

if petals % 2 == 0:
    print(f'Love me not')
else:
    print('Love me')

## Question 8: Time of Day Greeting

hours = int(input('Enter the hour : '))

if hours > 0 and hours < 6:
    print(f'Midnight Hours : {hours}')
elif hours >= 6 and hours < 12:
    print(f'Morning Hours : {hours}')
elif hours >= 12 and hours < 18:
    print(f'Afternoon Hours : {hours}')
elif hours >= 18 and hours < 24:
    print(f'Night Hours : {hours}')
else:
    print(f'Invalid hours : {hours}')

## Question 9: Text-based Menu

options = input('Enter the option : ')

if options == 'A':
    print(f'Option A')
elif options == 'B':
    print(f'Option B')
elif options == 'C':
    print(f'Option C')
elif options == 'D':
    print(f'Option D')
else:
    print(f'Invalid Option -- {options}')

## Question 10: Integer Size Classification

number = int(input('Enter the number : '))

if number <= 100:
    print(f'Small number : {number}')
elif number <= 1000:
    print(f'Medium number : {number}')
else:
    print(f'Large number : {number}')