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

For `control_flow_1`, I used Ghidra to figure out how it worked. First, we look into the `main` function. In here, we see that the input must be one string and that it must have at least 16 characters. After this check, we go to `rock`. In here, we see that the fourth character of our input must be equal to '2'. After this is checked and resolved, we move on to `paper`. In `paper`, we see that we first subtract 0x25U from the eighth element of our string. Then, we check to see if our new value is below 0x2e. If it is, then we move on into our if statement. In here, we left shift 1 by the bitwise AND of our new value after subtraction and 0x3f. After we do this, we take the bitwise AND of our new value and 1 and, if it comes out as 1, we move on to `scissors`. However, we noticed that the only way to have this outcome would to have the eighth value be equal to '%' so that when we do the subtraction in the beginning, the result is 0. Now, onto `scissors`. In this function, we see that the only constraint we have is that the first element of our string must be equal to 0x41, or in ASCII, 'A'. After this is true, we can move on to `lizard`. In here, we see a switch function checking the value of the second element of our string. We see that to move on to `spock`, we need this element to be equal to '6'. Lastly, we move into `spock` and see another switch case, this time checking the 16th element. For us to get through this switch, we need our value to be equal to '*' to get to the `win` function. Once we do this, we enter the `win` function and see that we have successfully cracked this function.

If you run the program `CF1.py`, it will give you a proper key you can use for this crackme that is 16 characters long and follows the rules listed above.

### ControlFlow2

For `control_flow_2`, I used Ghidra to figure out how it worked. First, we look into the `main` function. In here, we see that the input must be one string and that it must have at least 16 characters. After this check, we go to `rock`. In here, we see that the sixth character of our input must be equal to 'Y'. After this is checked and resolved, we move on to `paper`. In `paper`, we see that we first subtract 0x35U from the ninth element of our string. Then, we check to see if our new value is below 0x38. If it is, then we move on into our if statement. In here, we left shift 1 by the bitwise AND of our new value after subtraction and 0x3f. After we do this, we take the bitwise AND of our new value and 1 and, if it comes out as 1, we move on to `scissors`. However, we noticed that the only way to have this outcome would to have the ninth value be equal to '#' so that when we do the subtraction in the beginning, the result is 0. Now, onto `scissors`. In this function, we see that the only constraint we have is that the 11th element of our string must be equal to 0x41, or in ASCII, 'A'. After this is true, we can move on to `lizard`. In here, we see a switch function checking the value of the 14th element of our string. We see that to move on to `spock`, we need this element to be equal to '6'. Lastly, we move into `spock` and see another switch case, this time checking the 12th element. For us to get through this switch, we need our value to be equal to '*' to get to the `win` function. Once we do this, we enter the `win` function and see that we have successfully cracked this function.

If you run the program `CF2.py`, it will give you a proper key you can use for this crackme that is 16 characters long and follows the rules listed above.