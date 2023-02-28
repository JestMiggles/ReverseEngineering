# Week 5

### Crackme 1 Solution:

To solve this crackme, you need to download the file `crackMe1.py`. My solution goes through each rule and makes sure it passes it correctly before moving onto the next. I created an array of all possible characters that could be used, and would randomly select elements from said array until I found a combination that worked for the selected rule.

### How I Cracked It

1. We tested the code in terminal.
2. We found that we need to enter a 19 character string, and that if we get it wrong, the file deletes itself.
3. We redownload the file and make it immutable so the file can't delete itself.
4. We start looking into the main function and see four interesting functions: `rock`, `paper`, `scissors`, and `cracker`.
5. First, we look into `rock`.
6. To pass rock, we need to make sure that all of the elements in our string are either a capital or lowercase letter, an integer between 0 and 9, or a dash.
7. We also need the string to only be 19 characters long; nothing more, nothing less.
8. Then, we move to `paper`.
9. For paper, we are comparing different elements within our input and comparing them to one another.
10. We see to pass the first one, we need elements to be within 10 ASCII values of one another.
11. Then, we need elements 3 and 15 to be equal to said comparison, so we set them equal to those in our code.
12. Next, we move onto `scissors`.
13. 