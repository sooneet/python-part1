a = 'welcome'
print(a[0])

for x in 'banana':
  print(x)

a = "Hello"
print(len(a))

txt = "The best things in life are free!"
print('free' in txt)


txt = "The best things in life are free!"
if 'free' in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print('expensive' not in txt)    


txt = "The best things in life are free!"
if 'expensive' not in txt:
    print("Yes, 'expensive' is not present.")


b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-6:-3])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace('H','J'))

a = "Hello, World!"
b = a.split(',')
print(b)

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 35
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {3} for {1} dollars."
print(myorder.format(quantity,itemno,price))


txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
