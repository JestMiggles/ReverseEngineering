# Shellcode Creation

## Questions

**1. A code block containing your assembly instructions for your shellcode**

My code containing all my assembly instructions are located in the file `shellcode.S`.

**2. A step-by-step explanation of your assembly code and how it sets up the system call**

Line 1: I first XOR the register `rax` with itself to create a register that is empty without pushing NULL values.

Line 2: Then, I push the location of this value onto the stack.

Line 3: Next, I move this location into the register `rdx`.

Line 4: I push this location onto the stack now.

Line 5 & 6: I now move the location of `rdx`, which is pointing to the location of `rax`, into registers `rdx` and `rsi` so that I have these pointing to an address rather than a value.

Line 7: Next, push the string `/bin/sh` into register `rax`, however with the bits `0xff` at the end since we can't push any NULL values.

Line 8: Shift value in `rax` by eight bits to the right so that the string is now officially `/bin/sh`.

Line 9: Push this value onto the stack.

Line 10: Move this address into register `rdi`.

Line 11: Move the value `0x3B` into register `rax`.

Line 12: Call the system with our values and addresses all in order.

**3. Report how many bytes total are in your assembly, and include the whole thing in ascii**

My program is currently 41 bytes long. I am currently working on creating the python script to print out all the bytes.

**4. Explain what you did to ensure there were no NULL bytes in your code.**

To ensure no NULL bytes in the first part, I XORed the register `rax` with itself so that the value in there would be equal to zero. Then, I pushed the address.

To ensure there were no NULL values when pushing the string `/bin/sh`, I instead pushed the string without NULL values at the beginning and instead added two random characters to the end of the string. Then, I performed a right shift by 8 bits so that the extra two random characters would be pushed off and replaced with two NULL values in the beginning of the string.