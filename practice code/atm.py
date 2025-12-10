balance = 7000
Z_pin = 2607

print("-----Welcome To ATM-----")
    
while True:
    A = int(input("""
          to check balance enter 1:
          to add money in account enter 2:
          to withdraw money enter 3:
                  
          choose the number for easy way :"""))
    pin = int(input("enter pin:"))
    if(Z_pin!=pin):
        print("incorrect password")
        break
    else:
        print("login successfully")
        if(A == 1):
            print("your balance",balance,"in bank")
        elif(A == 2):
            deposit = int(input("enter amount to deposit :"))
            balance +=deposit
            print("you have Rs:",balance,"in your account")
        elif(A == 3):
            withdraw =int(input("enter amount to withdraw :"))
        Y_N = input("enter yes to continue or no to exit :")
        if(Y_N =="no" or "n"):
            break
        elif(Y_N =="yes" or "y"):
            continue 