import random
array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
choices = ["-",
           "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def passwordGen():
    rock1()
    rock2()
    paper1()
    paper2()
    paper3()
    scissors()
    answer = ""
    for i in range(0,19):
        answer += array[i]
    print(answer)
    
def rock1():
    temp = random.randint(0,52)
    array[8] = choices[temp]
    temp = random.randint(0,52)
    array[10] = choices[temp]
    
    if((ord(array[8]) ^ ord(array[10])) + 0x30 >= 0x3a):
        rock1()
    else:
        array[15] = chr((ord(array[8]) ^ ord(array[10])) + 0x30)
        array[3] = array[15]
        
def rock2():
    temp = random.randint(0,52)
    array[5] = choices[temp]
    temp = random.randint(0,52)
    array[13] = choices[temp]
    
    if((ord(array[5]) ^ ord(array[13])) + 0x30 >= 0x3a):
        rock2()
    else:
        array[18] = chr((ord(array[5]) ^ ord(array[13])) + 0x30)
        array[0] = array[18]
        
        
def paper1():
    temp = random.randint(0,52)
    array[2] = choices[temp]
    temp = random.randint(0,52)
    array[1] = choices[temp]
    
    if(ord(array[2]) + ord(array[1]) < 0xab):
        paper1()
        
def paper2():
    temp = random.randint(0,52)
    array[17] = choices[temp]
    temp = random.randint(0,52)
    array[16] = choices[temp]
    
    if(ord(array[17]) + ord(array[16]) < 0xab):
        paper2()
        
def paper3():
    if(ord(array[2]) + ord(array[1]) == ord(array[17]) + ord(array[16])):
        paper1()
        paper2()
        paper3()

def scissors():
    array[14] = "-"
    array[4] = array[14]
    array[9] = array[4]
    
    temp = random.randint(0,52)
    array[6] = choices[temp]
    temp = random.randint(0,52)
    array[7] = choices[temp]
    temp = random.randint(0,52)
    array[11] = choices[temp]
    temp = random.randint(0,52)
    array[12] = choices[temp]

passwordGen()