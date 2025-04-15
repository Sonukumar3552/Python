# a=10
# b=20
# print(a+b)
# print(id(a),id(b))

# x=10
# y=8
# print(bin(x))
# print(bin(y))
# print(x&y)
# print(bin(x&y),x|y)
# data type
# s="SONU PANDIT"
# print(s,type(s))
# s='''sonu hsts
# jshsy
# sjhsst
# '''
# print(s,type(s))
# l=[2,'sonu',4.5]
# print(l,type(l))
# t=(2,'sonu',4.5)
# print(l,type(t))
# d={'name':'sonu',
# 'age':'24'}
# print(d,type(d))
#user input (concinet)
# a=input("enter the value1:-")
# b=input("enter the value2:-")
# print(a+b)
#type cast
# a=int(input("enter the value1:-"))
# b=int(input("enter the value2:-"))
# print(a+b)
# a=eval(input("enter the value1:-"))
# b=eval(input("enter the value2:-"))
# print(a+b)
                                                    #conditional statements
# a=int(input("enter the value:-"))
# if a%2==0:
#    print(a,"even number")
# else: 
#     print(a,"odd number")   
# per=int(input("enter the value:="))
# if per>=60:
#     print("first div")
# elif per>=48:       
#     print("second div")
# elif per>=35:       
#     print("third div")
# else:        
#     print("fail ")
                                                      # loop with range
# for n in range(5):
#     print(n)
# for n in range(1,5):
#     print(n)
# for n in range(1,8,2):
#     print(n)    
                                                           #table print
# n=int(input("Enter the number:-"))
# for a in range(11):
#     print(n*a)
                                                           # reverse
# n=int(input("Enter the number:-"))
# for a in range(10,0,-1):
#     print(n*a)
                                                        #while loop
i=1
# while i<20:
#     print("om sai ram")
#     i=i+1                                                     
                                                        #string indexing
# a="sonu kumar pandit"     
# print(a[6])       #u
# print(a[-2])       #i                                    
                                                  #sting slicing
# a="sonu kumar pandit"     
# print(a[0:6])       
# print(a[0::2])        
                                               #string iteration
# w="sonu kumar pandit"
# t=len(w)
# print(t)
# for a in range(t):
#     print(w[a])
# for a in w:
#     print(a)    
                                             #string function
# w= "sonukumarPANDIT"
# n=w.upper()
# print(n)   
# n=w.title()
# print(n)  
# n=w.capitalize()
# print(n) 
# print(w.find('a'))    
# print(w.isalpha())        
# d="234567890"                                  
# print(w.isdigit())   
# function of pythone
# string format
a= "{} mr {} sonu jii ".format("hello" ,47)
print(a)
b= "{1} mr {0} sonu jii ".format("hello" ,47)
print(b)