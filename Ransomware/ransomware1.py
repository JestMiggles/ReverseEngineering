def decrypt():
    file = input("Please enter the name of the file you want to decrypt: ")
    newFile = file[:-7] # This is to remove the '.pay_up' at the end :P
    fileInput = open(file, "rb")
    fileOutput = open(newFile, "w")
    while(fileInput.read(1)):
        fileInput = fileInput ^ 0x34
        fileOutput.write(fileInput)
    
decrypt()