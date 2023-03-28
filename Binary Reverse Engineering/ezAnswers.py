def answers():
    while(1):
        print("Welcome to the EZ answers program!")
        print("To see the answer to EZ1, type in \"1\"")
        print("To see the answer to EZ2, type in \"2\"")
        print("To see the answer to EZ3, type in \"3\"")
        print("To end the program, type in \"4\"")
        choice = input("Your choice: ")
        
        if(choice == "1"):
            print("EZ1 answer: picklecucumberl337\n")
        elif(choice == "2"):
            print("EZ2 answer: artificialtree\n")
        elif(choice == "3"):
            print("EZ3 answer: strawberrykiwi\n")
        elif(choice == "4"):
            print("Bye! :D")
            break
        else:
            print("Invalid input!\n")
            
answers()