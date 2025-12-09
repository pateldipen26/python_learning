f = open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt")
data = f.read()
print(data)
f.close()

f = open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt")

content = f.read()

if("bad" in content):
    print("They are come in his prime area")
else:
    print("they word are not coming in this order")

f.close()