x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)


x = 5
y = "John"
print(type(x))
print(type(y))


x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)


a = 4
A = "Sally"
#A will not overwrite a

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ['apple','mango','orange']
x , y , z = fruits
print(x)
print(y)
print(z)


x = 'awesome'
print('python is ' + x)

x = "python is "
y = "awesome"
print(x + y)


x = 5
y = 10
print(x + y)


x = "awesome"
def fun():
	print('python is ' + x)
fun()   


x = "awesome"
def fun():
	x = "fantastic"
	print('python is ' + x)
fun() 

def fun():
   global x 
   x = 'fantastic'
fun()
print('python is ' + x)


x = 'awesome'
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
