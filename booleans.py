print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
	print('b is greater')
else :
	print('c is not greater')

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def fun():
  return True
    
print(fun()) 


def fun():
	return True

if fun():
	print('yes')
else:
	print('no')

x = 20
print(isinstance(x,int))
