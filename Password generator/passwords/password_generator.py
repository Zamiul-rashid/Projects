import random
import os 
def generate():
    alpha = [i for i in range(ord("a"),ord("z")+1)] + [i for i in range(ord("A") , ord("Z")+1)]
    digit = [i for i in range (48,58)] 
    spacial_chr = [i for i in range(33,48)]+[i for i in range (58,65)]+[i for i in range(91-97)]
    
    total = alpha + digit + spacial_chr
    length = 16
    passwrd=""
    for i in range(length):
        passwrd +=  chr(random.choice(total))
    return passwrd

def file_write(password):
    # with open("E:\Zamiul_codes_source\Projects\Password generator\passwords\passwords_generated.txt ","a+") as file:#enter your own directory
    #     temp = file.read()
    # with open("E:\Zamiul_codes_source\Projects\Password generator\passwords\passwords_generated.txt ","a" ) as file:#enter your own directory
    #     file.write("Password is : " + temp+ password + "\n")
    with open(os.path.join(os.getcwd(),"\passwords\passwords_generated.txt"),"a+")as file:#enter your own directory
        temp = file.read()
    with open(os.path.join(os.getcwd(),"\passwords\passwords_generated.txt"),"a" ) as file:#enter your own directory
        file.write("Password is : " + temp+ password + "\n")
        
def clear(password):
    # with open("E:\Zamiul_codes_source\Projects\Password generator\passwords\passwords_generated.txt ","w") as file:
    #     file.write("Password is : " + password +"\n" )
    with open(os.path.join(os.getcwd(),"\passwords\passwords_generated.txt"),"w") as file:
        file.write("Password is : " + password +"\n" )
        

while True:
    print("Do you want to clear all the previous passwords? (Y/N) ")
    user = input()

    if user == "N":
        password = generate()
        file_write(password)
        print(f"Password saved to desktop in 'passwords_generated.txt'")
        break

    elif user == "Y":
        password = generate()
        clear(password)
        print(f"Password saved to desktop in 'passwords_generated.txt'")
        break

    else:
        print('Improper input: "Please enter Y or N" ')
    