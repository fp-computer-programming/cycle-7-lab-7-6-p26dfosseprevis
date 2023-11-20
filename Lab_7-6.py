"""
Create a Python file named lab_7-6.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a 2 separate functions within the same document. 
Create a 3rd function which requires both the first two functions within it
Create 4 test cases for your 3rd function. 
"""
def avg(a1,a2):
    """Returns the avg of two numbers"""
    return (a1 + a2)/2
def double(a1):
    """Returns twice the inputed number"""
    return a1*2

def double_avg(a1,a2):
    """returns twice the avrage of two numbers"""
    return double(avg(a1,a2))


print(double_avg(1,1) == 2)
print(double_avg(3,5) == 8)
print(double_avg(14,16) == 30)
print(double_avg(9,5) == 14)