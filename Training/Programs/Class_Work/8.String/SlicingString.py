b = "Hello, World!"
print(b[2:5]) # start from 2 but end at 5-1 #output -> llo


b = "Hello, World!"
print(b[:5]) #if the starting position is blank then it's 0 #output -> Hello


b = "Hello, World!"
print(b[2:])#if the ending position is blank then it's last value #output -> llo, World!

b = "Hello, World!"
print(b[:])#if the starting position is blank then it's 0 last position is blank then value is last value#output -> Hello, World!


b = "Hello, World!"
print(b[-5:-2]) # starting index starts from -5+1=-4 to -2 
"""
negative indexing
x= "Hello";
x[-3:-1] -> lo {-3 means -3 + 1 = starts -2 index}
"""


# Two rules
#1/. RTL - Right to left (all programming language follows this rule)
#1/. LTR - left to Right (normal human language follows this rule to write except some countries)
x = 'Welcome'
print(x[3:5]) #co
x = x[3:5]
print(x) #

x = 24 + 34/2 * 5 + 2 * 6 #34/2 = 17 * 5 = 85 + 12 = 91 + 24 = 121
#6*2+5*17+24=x
#12+5*17+24=x
#12+85+24 =x
#121=x
print(x) #121