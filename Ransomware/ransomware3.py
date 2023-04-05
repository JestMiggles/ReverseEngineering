def decrypt():
    
    # Read in file to decrypt
    file = input("Please enter the name of the file you want to decrypt: ")
    newFile = file[:-7] # This is to remove the '.pay_up' at the end :P
    
    # Open the file to read from and file to write to
    fileInput = open(file, "r")
    fileOutput = open(newFile, "w")
    
    key = "R3V3R53"
    byteRead = fileInput.read(7)
    while(byteRead):
        temp = ""
        for i in range(0, len(byteRead)):
            temp += chr(ord(byteRead[i]) ^ ord(key[i]))
        fileOutput.write(temp)
        byteRead = fileInput.read(7)
        
    # Close file, then re-open it and print the contents
    #fileOutput.close()
    #fileOutput = open(newFile, "r")
    #print(fileOutput.read())



decrypt()