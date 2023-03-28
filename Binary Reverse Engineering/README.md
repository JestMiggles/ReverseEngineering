# Binary Reverse Engineering with Crackmes

### EZCrackMe1

For `ezcrackme1`, I used uftrace to figure out the password. First, I ran the program and saw that it wants the user to run it, then be prompted for input. Afterwards, it seems to compare it to a secret key and output whether you guessed right or not. Then, I ran it using uftrace to see what functions it was using and what it was doing at each step. After running it with uftrace, I see that after it takes my input, it compares my input to the string "picklecucumberl337". After running the program and using this phrase as the input I was able to successfully crack the code.

Thus, the password is "picklecucumberl337" and is able to be outputted using the program `ezAnswers.py`.

### EZCrackMe2

For `ezcrackme2`, I used strings to try cracking it. Firstly, I ran the program and saw that it ran similar to `ezcrackme1` and had the user run it, then input a phrase. So, after seeing this I ran strings on it this time and saw some interesting output, one of which was the phrase "artificialtree" before the win text. So, I decided to try this phrase as the input and sure enough, it proved to be the password.

Thus, the password is "artificialtree" and is able to be outputted using the program `ezAnswers.py`.

### EZCrackMe3

For `ezcrackme3`, both uftrace and strings proved to be inefficient in finding the answer, so I turned to using Ghidra. After running the program and seeing that it ran the same as the previous two, I decided to try uftrace. Through seeing this, I saw the phrase "strawberry" being compared with our input so I decided to try it and, sadly, it was not the correct input. So, I decided to use strings to see if I could find anything else. After running strings on the program, I found "kiwi" posted in there as well, and after trying that phrase it still did not work. Lastly, I ran Ghidra on it to see exactly what was happening. Using Ghidra, I was able to trace that it combines the strings "strawberry" and "kiwi" together, and after trying the phrase "strawberrykiwi" I was able to successfully crack the code.

Thus, the password is "strawberrykiwi" and is able to be outputted using the program `ezAnswers.py`.

### ControlFlow1

