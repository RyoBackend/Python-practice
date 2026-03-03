class student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self)  :
        print('Name: ',self.name)
        print('age: ',self.age)
        print('Marks :',self.marks)

    def is_pass(self) :

        if self.marks>=40 :
            return 'passed'
        else :
            return 'failed'

s1 = student('Ryo',22,75) 

s1.display()
print('Result : ',s1.is_pass()) 
               
