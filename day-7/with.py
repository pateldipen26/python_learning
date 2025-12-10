# f = open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt")
# print(f.read())

# f.close()

# ## using for the same work 

# with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\day-7\file.txt") as f:
#     print(f.read()) ## dont need to close 

import random   

print("you play game")
# print(score)
with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\myfile.txt") as f:
    score = random.randint(1,100)
    hiscore = f.read()
    if(hiscore!=""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
            
    print(f"your score: {score}")
    if(score>hiscore):
         with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\myfile.txt","w") as f:
            f.write(str(score))
    # return score 

# import random

# print("you play game")

# # generate score first
# score = random.randint(1, 100)
# print("Your score:", score)

# filepath = r"C:\Users\Dipen\OneDrive\Desktop\python_learning\myfile.txt"

# # read high score
# try:
#     with open(filepath) as f:
#         content = f.read().strip()
#         hiscore = int(content) if content else 0
# except FileNotFoundError:
#     hiscore = 0  # if file does not exist, start with 0

# print("High score:", hiscore)

# # update high score if needed
# if score > hiscore:
#     print("🎉 New High Score!")
#     with open(filepath, "w") as f:
#         f.write(str(score))
# else:
#     print("High score remains the same.")


# import random

# with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\myfile.txt")as f:
#     score=random.randint(1,100)
#     high=f.read()
#     if (high!=""):
#         high=int(high)
#     else:
#         high=0

#     print(f"Your score :{score}")

#     if (score>high):
#         with open(r"C:\Users\Dipen\OneDrive\Desktop\python_learning\myfile.txt","w") as f:
#             f.write(str(score))

