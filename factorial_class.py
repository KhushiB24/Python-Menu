class Factorial:
    def __init__(self):
        self.factorial = [0, 1]
  
    # Defining __call__ method
    def __call__(self, a):
        fact = int(input("Enter a number: "))    
fact = 1    
if fact < 0:    
     print(" Factorial does not exist for negative numbers")    
elif fact == 0:    
      print("The factorial of 0 is 1")    
else:    
      for i in range(1,fact + 1):    
        factorial = fact*i    
      print("The factorial of",fact,"is",factorial)    