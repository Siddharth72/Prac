## Question 1: Check if a Number is Positive

input_number = input("Enter a number : ")

a = int(input_number)

if a > 0:
    print("Positive number")

## Question 2: Determine if a Number is Odd or Even

input_numbers = input("Enter a number : ")

a = int(input_numbers)

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

## Question 3: Check if a Number is Within the Range of 1 to 10 Inclusive

b = input("Enter a number : ")

input_number = int(b)

if 1 <= input_number <= 10:
    print('In range from 1 to 10')
else:
    print("Out of range")

## Question 4: Categorize Numbers as Small, Medium, or Large

n = input('Enter a number : ')

number = int(n)

if number < 10:
    print("Small")
elif 10 <= number <= 15:
    print("Medium")
else:
    print("Large")

## Question 5: Check if a List is Not Empty

n = input('Enter a number : ')

number = list(n)

if number:
    print("List is not empty")
    print(number)
else:
    print('List is empty')
    
## Question 6: Check the Length of a String

n = input('Enter the texts : ')

print(len(n))

text = input('Enter the texts to test : ')

if len(text) > 15:
    print(f'Too long string : {len(text)}')
else:
    print(f'Shorter string : {len(text)}')


## Question 7: Check if a Year is a Leap Year

y = input("Enter the year : ")

year = int(y)

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f'Leap year : {year}')
else:
    print(f'Non leap year : {year} ')

## Question 8: Check if a Character is a Vowel or Consonant

t = ('a','e','i','o','u')

char = input('Enter the Character  : ')

if char in t:
    print('Vowel Character')
else:
    print('Constant')

## Question 9: Compare Variables `a` and `b`

a = int(input('Enter number 1 value : '))
b = int(input('Enter number 2 value : '))

if a > b:
    print(f'a is greater than b: {'a:',a,'b:',b}')
elif a == b:
    print(f'equal numbers : {'a:',a,'b:',b}')
else:
    print(f'b is greater than a : {'a:',a,'b:',b}')

## Question 10: Check if a Number is Positive, Negative, or Zero

numbers = int(input('Enter a number : '))

if numbers == 0:
    print('Zero')
elif numbers > 0:
    print('Positive')
else:
    print('Negative')
