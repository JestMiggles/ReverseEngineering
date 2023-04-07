# Ransomware

### Ransomware 1

For ransomware1, I wrote my program so that it takes in the name of the file you want to decrypt with the ".pay_up" extension, creates a file of the same name without the extension, and decrypts it. While analyzing the program in Ghidra, we see that the program is calling in one byte of data at a time and XORing said data with the value 0x34. After performing the XOR, we push this value into the new file without the extension. Finally, in my program if you remove the comments at the bottom it will automatically print the output of the file.

My decryption for this program is in the program `ransomware1.py` and the data in the file `secret.txt` is:
"Dear Student,

You have decrypted the message. Good job!

"Many of the engineers I interviewed worked on reverse-engineering technology. It's a hallmark of Area 51."
 ~ ANNIE JACOBSEN

Go NMSU RE!"

Will add screenshots when I get home as Ghidra is on my other PC and my wifi is out currently :'D

### Ransomware 2

For ransomware2, I was able to deduce through looking at the code in Ghidra that the code this time was taking in input from the desired file and was XORing the data with the string "1337" to decrypt and encrypt our files. So, when writing my code, I would take the desired file to decrypt as input, create another file with the same name without the ".pay_up" extension. Then, I would pull 4 bytes from the encrypted file, XOR it with the string "1337", and then write the new bytes into our new decrypted file. Finally, in my program if you remove the comments at the bottom it will automatically print the output of the file.

My decryption for this program is in the program `ransomware2.py` and the data in the file `secret.txt` is:
"Dear Student,

You have decrypted the message. Good job!

"Basically, if reverse engineering is banned, then a lot of the open source community is doomed to fail."
 ~ Jon Lech Johansen

Go NMSU RE!"

Will add screenshots when I get home as Ghidra is on my other PC and my wifi is out currently :'D

### Ransomware 3

For ransomware3, they do a similar method to the second program, however instead they XOR our input with the string "R3V3R53" and pull 7 bytes at a time. Therefore, for my decryption, I take the desired file to decrypt as input, then create another file without the "pay_up" extension. Then, I cycle through the decrypted file, pulling 7 bytes per round, and XORing the bytes with our key "R3V3R53". Once we XOR these, we then push the values into the new file and repeat the process.Finally, in my program if you remove the comments at the bottom it will automatically print the output of the file.

My decryption for this program is in the program `ransomware3.py` and the data in the file `secret.txt` is:
"Dear Student,

You have decrypted the message. Good job!

"A good engineer thinks in reverse and asks himself about the stylistic consequences of the components and systems he proposes."
 ~ Helmut Jahn

Go NMSU RE!"

Will add screenshots when I get home as Ghidra is on my other PC and my wifi is out currently :'D