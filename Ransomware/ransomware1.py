def decrypt():
    file = input("Please enter the name of the file you want to decrypt: ")
    newFile = file[:-7] # This is to remove the '.pay_up' at the end :P
    
    # Open the file to read from and file to write to
    fileInput = open(file, "rb")
    fileOutput = open(newFile, "w")
    byteRead = fileInput.read(1)
    # Read input until all is read, and decrypt
    while(byteRead):
        byteRead = chr(int.from_bytes(byteRead, "little") ^ 0x34)
        fileOutput.write(byteRead)
        byteRead = fileInput.read(1)
    
    # Close file, then re-open it and print the contents
    fileOutput.close()
    fileOutput = open(newFile, "r")
    print(fileOutput.read())
    
decrypt()