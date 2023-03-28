import random

password = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]

choices = ["0","1","2","3","4","5","6","7","8","9",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def CF1():
    fill()
    rest()
    answer = ""
    for i in range(0, 16):
        answer += password[i]
    print(f"Password choice: {answer}")
    
def fill():
    for i in range(0, 16):
        temp = random.randint(0,61)
        password[i] = choices[temp]
        
def rest():
    password[3]  = "2"
    password[7]  = "%"
    password[0]  = "A"
    password[1]  = "6"
    password[15] = "*"
    
CF1()