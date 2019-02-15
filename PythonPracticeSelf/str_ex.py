
'''
Hello = "Hello World"
print(Hello)
len(Hello)

First5 = Hello[0:5]
print(First5)

HelloBig = (First5 + " Big " + Hello[6:len(Hello)] )
print(HelloBig)
print(HelloBig.upper())
print(HelloBig.lower())
print(HelloBig.lower().title())

first = 'Lily'
last = 'Wang'
print("My first name is %s, my last name is %s." %(first, last) )
print( (first+" "+last).upper() )
print( (first+" "+last).lower() )
print( (first+" "+last).lower().title() )
print(len(first+" "+last))
print(first[0]+"."+last[0]+".")

name = []
name.append(first)
name.append(last)
print(name)

s = "_"
s = s.join(name)
print(s)
print(s[:4] + s[5:])
'''

print("What are your name?")
name = input()
print("Hello, %s" %name)

print("Please enter a lower number: ")
lnumber = int(input())

print("Please enter a higher number: ")
hnumber = int(input())
print(lnumber+hnumber)
print("There are %d numbers between %d and %d." % (hnumber-lnumber, lnumber, hnumber))

i=0
m=9
number=[]
squareNumber = []
while i <= m:
    if i>m:
        break
    number.append(i)
    squareNumber.append(i*i)
    i += 1
    
print(number)
print(squareNumber)

matrixList=[[4,6,7],[3,5,7],[2,5,4]]
for ml in matrixList:
    print(ml)
    

m =len(matrixList)
print(m)
for l in matrixList:
    i= 0
    while i < m:
        print(l[i], end = ' ')
        i += 1
    print("\n")
        
    


