# a =int(input("enter your age :"))

# if(a>=18):
#     print("you are able to play tournament")
# else:
#     print("you can not able to play tournament")

# print("slot are less")

# # comparision for numbers

# a1 = int(input("enter num 1: "))
# a2 = int(input("enter num 2: "))
# a3 = int(input("enter num 3: "))
# a4 = int(input("enter num 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("greatest number is a1:", a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("greatest number is a2:", a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("greatest number is a3:", a3)
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("greatest number is a4:", a4)

# # marksheet fail and pass

# marks1 = int(input("Enter marks 1:"))
# marks2 = int(input("Enter marks 2:"))
# marks3 = int(input("Enter marks 3:"))
# # total = marks1+marks2+marks3
# # percentage = (total/300)*100

# total_percentage=(((marks1+marks2+marks3)*100)/300)

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("you are pass :",total_percentage)
# else:
#     print("you are faile ple try next year :",total_percentage)

# # message are spam or unspam

# p1 = "make lot of money"
# p2 = "buy now"
# p3 = "click this link"
# p4 = "open this link"
# p5 = "buy this"
# p6 = "enter your number"

# message = input("Enter your commit :")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message) or (p5 in message) or (p6 in message)):
#     print("this commit is spam")
# else:
#     print("this is not spam")

# # using for name alphabet counting

# carname = input("enter username :") 

# if(len(carname)<10):
#     print("your car name have a normal alphabet")
# else:
#     print("your car name has biger alphabet")

# l = ["dipen","zalak","dharmi","tejas","vijay"]

# name = input("Enter your name :")

# if(name in l):
#     print(" congratulations  you are selected for the global tournament , connect the our team")
# else:
#     print("you are not selected , better luck next time")    

# marksheet for grade

# marks = int(input("enter your marks :"))

# if(marks<=100 and marks>=90):
#     grade = "ex"
# elif(marks<=90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "FAIL"

# print("your grade is :", grade)

post = input("enter your post :")

if("dipen".lower() in post.lower()):
    print("this post talking about dipen")
else:
    print("this post not talking about dipen")