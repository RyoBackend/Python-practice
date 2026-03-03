class Rectangle :

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self) :
        return 2 * (self.length + self.width)

x=int(input('Enter the length of the rectangle : '))  
y=int(input('Enter the witdth of the rectangle : ')) 
rect = Rectangle(x,y)


print('Area : ',rect.area())
print('Peremeter : ', rect.perimeter())
