'''
Program : List Even Sum Program

Description:
This program creates a list of integers provided by the user
and calculates the sum of even numbers from that list.

Features :
- Valide user input
- Prevents negative numbers
- Handles invalid inputs using the exception handling
- Calculate the sum of even numbers in the list

Concepts used :
- Functions
- Exception handling (try/except)
- Input validation
- Loops
- Genetal expression
- Type checking

Author : Ryo
Date : 2026
'''


def add (elements) :
    if not isinstance(elements,list) :
        raise TypeError('List Expected')

    return sum(i for i in elements if i%2==0)
def to_eliminate_negative_integers(prompt):
    while True :
        try :
            input_number=int(input(prompt))
            if input_number<0 :
                raise ValueError('Input value must not be a negative integer')
            return input_number
        except ValueError :
            print('Enter non negative number')

def list_creation (value):
    the_list =[]
    for i in range(value):
        while True :
            try:
                b=int(input(f'Enter the {i+1} element : '))
                if b<0:
                    raise ValueError('Negative integers are not allowed')
                the_list.append(b)
                break
            except ValueError:
                print('Enter the integer')
    return the_list

if __name__ =="__main__" :
    input_number = to_eliminate_negative_integers(f'How manu values needed to be added in the list : ')
    elements=list_creation(input_number)
    print('The list is : ',elements)
    print(add(elements))

