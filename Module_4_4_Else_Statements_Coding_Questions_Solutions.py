## Question 1: Even or Odd

number = int(input('Enter the number : '))

if number % 2 == 0:
    print(f'Even number : {number}')
else:
    print(f'Odd number : {number}')

## Question 2: Adult or Minor

age = int(input('Enter the age : '))

if age >= 18:
    print('Adult')
else:
    print('Minor')

## Question 3: Check If List is Empty


list_value = list(input('List values : '))

if list_value:
    print(f'List is not empty : {list_value}')
else:
    print(f'List is empty: {list_value}')


## Question 4: Contains 'a' or Not

text = input('Enter the texts : ')
     
if 'a' in text:
    print(f'Yes a is in the text : {text}')
else:
    print(f'a is not there in text : {text}')

## Question 5: Print Larger Number or 'Equal'
number1 = int(input('Enter the number1 : '))
number2 = int(input('Enter the number2 : '))

if number1 > number2:
    print(f'Number 1 is greater than number 2 : {number1,number2}')
elif number1 == number2:
    print(f'Numbers are eaqual : {number1,number2}')
else:
    print(f'Number 2 is greater than Number 1 : {number1,number2}')

## Question 6: Categorize Character

n = input('Enter the digit or character : ')

if n.isdigit():
    print(f'Digit : {n}')
elif n.isalpha():
    print(f'Character : {n}')
else:
    print(f'Special character : {n}')

## Question 7: Number Categorization

number = int(input('Enter the number : '))

if number == 0:
    print(f'Zero : {number}')
elif number > 0:
    print(f'Positive number : {number}')
else:
    print(f'Negative : {number}')

## Question 8: User Input Validation

user_input = input('Enter T o F :')

if user_input == 'True':
    print('Yes')
elif user_input == 'False':
    print('No')
else:
    print('Invalid input')

## Question 9: Leap Year Determination
year = int(input('Enter the year : '))

if (year% 4 == 0 and year % 100!= 0) or (year%400 == 0):
    print(f'Leap year : {year}')
else:
    print(f'Non Leap year : {year}')

## Question 10: Score Categorization

score = int(input('Enter the score : '))

if score >= 90:
    print(f'High score : {score}')
elif score >= 80 and score < 90:
    print(f'Medium  score : {score}')
else:
    print(f'Average score : {score}')