## Question 1: Check If List is Empty

list_value = list(input('Enter the list value : '))

if not list_value:
    print(f'Emplty list : {list_value}')
else:
    print(f'Not an empty list : {list_value}')

## Question 2: Non-zero Number Check

numbers = int(input('Enter the number : '))

if numbers > 0:
    print(f'Non-Zero number : {numbers}')
else:
    print(f'Zero -numbers or negative numbers: {numbers}')

## Question 3: Non-empty String Check

text = input('Enter the text : ')

if not text:
    print(f'text is empty')
else:
    print(f'text is not empty : {text}')

## Question 4: Dictionary Empty Check

key = input('Enter the key value : ')

value = input('Enter the value : ')

dict_check = {key,value}

if not dict_check:
    print(f'Dict is empty')
else:
    print(f'Dict : {dict_check}')

## Question 5: Truthy Value Check
my_value = input('Enter the text : ')

if my_value is None or my_value == 'None':
    print(f'value is empty : {my_value}')
else:
    print(f'value is not empty : {my_value}')
    
    
## Question 6: None Check
my_value = input('Enter the text : ')

if my_value is None or my_value == 'None':
    print(f'value is empty : {my_value}')
else:
    print(f'value is not empty : {my_value}')

## Question 7: Truthy List Check in One Line

my_list = list(input('Enter the list values : '))

print(f'Truthly list : {my_list}') if my_list else print(f'Empty list : {None}')

## Question 8: Check for 0 or None
numbers = int(input('Enter the number : '))

print(f'Zero Numbers or Undefined number : {numbers}') if numbers == 0 or numbers is None else print(f'Non-Zero number : {numbers}')

## Question 9: All Arguments Truthy

def all_argumnets(*args):
    return all(args)

print(all_argumnets(1,'3','basic'))     

## Question 10: Check for Blank String

blank_string = ' ' #'Enter the value as blank or non blank'

if not blank_string.strip():
    print(f'Values : {blank_string}')
else:
    print(f'Not Blank')