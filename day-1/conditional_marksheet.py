name = input("enter name: ")
std = input("enter std: ")
div = input("enter div: ")
rollnum = input("enter roll num: ")

iot = int(input("enter iot : "))
iws = int(input("enter iws : "))
mgd = int(input("enter mgd : "))
spm = int(input("enter spm : "))

total_marks = iot+iws+mgd+spm
percentage = (total_marks/200)*100

print("Name:",name)
print("STD:",std)
print("DIV:",div)
print("Roll_Num:",rollnum)


print("Total_marks:",total_marks)
print("Percentage:",percentage)


if(percentage >= 90 ):
    print("A")
elif(perncentage >= 70 ):
    print("B")
elif(percentage >= 60 ):
    print("C")    
else:
    print("YOU ARE FAIL")