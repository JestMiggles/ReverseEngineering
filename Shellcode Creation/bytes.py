import binascii

def bytes():
    with open('shellcode', 'rb') as f:
        num = f.read().hex()
    i = 0
    answer = "My code is " + str(int(len(num)/2)) + " bytes. The bytes are:"
    while(i < len(num)):
        answer += " "
        answer += num[i:i+2]
        i += 2
    print(answer)
    
bytes()