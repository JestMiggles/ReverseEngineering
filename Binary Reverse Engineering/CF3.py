import random

password = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5]

choices = ["0","1","2","3","4","5","6","7","8","9",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def CF3():
    fill()
    rock()
    paper()
    spock()
    answer = ""
    for i in range(0, 16):
        answer += password[i]
    print(f"Password choice: {answer}")


def fill():
    for i in range(0, 16):
        temp = random.randint(0,61)
        password[i] = choices[temp]

 
def rock():
    temp = random.randint(0,61)
    password[1] = choices[temp]
    temp = random.randint(0,61)
    password[3] = choices[temp]
    temp = random.randint(0,61)
    password[5] = choices[temp]
    temp = random.randint(0,61)
    password[6] = choices[temp]
    
    if(not(ord(password[1]) + ord(password[3]) - ord(password[5]) == ord(password[6]))):
        rock()


def paper():
    temp = random.randint(0,61)
    password[7] = choices[temp]
    
    if(not(ord(password[6]) ^ ord(password[7]) < 3)):
        paper()
        
        
def scissors():
    temp = random.randint(0,61)
    password[10] = choices[temp]
    password[12] = choices[temp]


def lizard():
    temp = random.randint(0,61)
    password[8] = choices[temp]
    
    if(not(ord(password[8]) ^ ord(password[7]) >= 4)):
        lizard()


def spock():
    scissors()
    lizard()
    temp = random.randint(0,61)
    password[9] = choices[temp]
    
    if(not((ord(password[12]) ^ ord(password[8]) ^ ord(password[9])) != (ord(password[10]) < 3)) or (ord(password[8]) == ord(password[9]))):
        spock()
        

CF3()