f = open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt")
print(f.read())

f.close()

## using for the same work 

with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt") as f:
    print(f.read()) ## dont need to close 