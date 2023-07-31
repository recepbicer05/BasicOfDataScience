print("a" , "b", sep="--")


def calculate(x):
    print(x*2)


calculate(5)

#with docstring we can create an expression for the scope of functions
def calculation(arg1, arg2):
    """
    Sum of two numbers

    Parameters
    ----------
    arg1: int, float
    arg2: int, float

    Return
        int, float
    -------

    """
    print(arg1 + arg2)


calculation(2,3)

recep =[]
def append(arg):
    recep.append(arg)

append(25)
append(26)
append(30)
print(recep)


#return: u can use output of function as a input.

def planning(math, control, feedback):
    return (math*4+control*3+feedback*3)/10

print(planning(4, 3, 3.5) * 10)

students = ["Recep","Ahmed","Ismail","Hakan"]

for student in  students:
    print("Student:", student.upper())

def new_salary(salary, rate):
    return salary*rate/100+salary

print(new_salary(1000, 15))

salaries = [10,20,30,40]

for salary in salaries:
    if salary == 10:
        continue #yoksayıyor o değeri kısaca
    print(salary)

for salary in salaries:
    if salary == 20:
        break
    print(salary)


#enumerate ile bir tanım içinde indexler olarak gezebiliriz
students = ["Recep","Ahmed","Ismail","Hakan"]

A=[]
B=[]
for index, student in enumerate(students): # ,1 gibi yazarsan oradan başlatır indexi
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

print(A,B)

# zip ile ayrı ayrı listeleri bir araya getirebiliriz

print(list(zip(students, salaries)))

# lambda functionları kullan-at tipindedir

new_sum = lambda a, b: a+b

print(new_sum(4,7))

