class ListEvenSum :

    def get_non_negative_number (self,prompt) :
        while True :
            try :
                user_input = int(input(prompt))
                if user_input < 0 :
                    raise ValueError
                return user_input
            except ValueError :
                print ('Value error, Non negative input value only')
    
    def list_creation (self,user_input) :
        the_list = []
        for i in range (user_input):
            while True :
                try :
                    elements = int(input(f'Enter the value of {i+1} element : '))
                    the_list.append(elements)
                    break
                except ValueError :
                    print(f'Value must not contain any string or character')
        return the_list
    
    def add(self, the_list):
        total=sum(i for i in the_list if i%2 == 0)
        return total
        
                 


if __name__==  "__main__" :        
    user = ListEvenSum()
    user_input = user.get_non_negative_number('Enter the number of elements contain inside the list : ')
    print (user_input)
    the_list = user.list_creation(user_input)
    print(f'The created list is : ',the_list)
    print(f'the sum of even numbers inside the list is : ',user.add(the_list))
