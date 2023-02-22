# Week 4 Assignment

## Questions

### CS 479 Questions

**1. What is the difference between machine code and assembly?**

The difference is that machine code is a high level language that is compiled to be read by the CPU, while assembly is a low level language that is used by us to analyze and tell what the program is doing.

**2. If the ESP register is pointing to memory address 0x001270A4 and I execute a `push eax` instruction, what address will ESP now be pointing to?**

When you do a `push eax` instruction, it will decrement the address by 4 bytes, making the new address being pointed to 0x001270A0.

**3. What is a stack frame?**

A stack frame clarifies the organization of stacks. This means that it stores local variables on the stack.

**4. What would you find in a data section?**

You would find a collection of the files global and static local variables.

**5. What is the heap used for?**

The heap is used for allocating space for new values and freeing space when said values are no longer of use.

**6. What is in the code section of a program's virtual memory space?**

The executable code is in the program's virtual memory space.

**7. What does the `inc` instruction do, and how many operands does it take?**

The `inc` instruction increments a register by one and is a single operand.

**8. If I perform a `div` instruction, where would I find the remainder of the binary division (modulo)?**

If you perform the `div` instruction, you will find the remainder of the modulo in the EDX register.

**9. How does `jz` decide whether to jump or not?**

`jz` decides whether to jump based on the ZF flag. If the ZF flag is 1, it jumps. Otherwise, it doesn't jump.

**10. How does `jne` decide whether to jump or not?**

`jne` decides whether to jump or not based on the ZF flag. If the ZF flag is 0, it jumps, otherwise it doesn't.

**11. What does a `mov` instruction do?**

A `mov` instruction can move data into registers or RAM.

**12. What does the `TF` flag do and why is it useful for debugging?**

The `TF` flag makes it so that the processor will only execute one instruction at a time, making it easier to see what your code is doing and where the error may be occuring.

**13. Why would an attacker want to control the EIP register inside a program they want to take control of?**

An attacker would want to control this register because the EIP controls what code is executed next, so if the attacker injects the system with malware they can then point the EIP to where the corrupted code is and have it ran.

**14. What is the AL register and how does it relate to EAX?** 

The AL register is used to reference the 8 lowest bits in the EAX register.

**15. What is the result of the instruction `xor eax, eax` and where is it stored?**

The result of this instruction is to clear the EAX register, and it is stored in the EAX register as empty, or 0.

### CS 579 Questions

**I. What does the `leave` instruction do in terms of registers to leave a stack frame?**

The `leave` instruction is used to revert the EBP back to before it was entered by copying EBP to ESP and then restoring the old EBP. (reference: https://stackoverflow.com/questions/29790175/assembly-x86-leave-instruction)

**II. What `pop` instruction is `retn` equivalent to?**

When you use the `retn` function, it pops the value at the top of the stack into the EIP register, thus making `retn` equivalent to the `pop eip` instruction. (reference: https://c9x.me/x86/html/file_module_x86_id_280.html)

**III. What is a stack overflow?**

A stack overflow occurs when the stack is full and you try adding more addresses to it. This is due to limited memory and address space within the stack.

**IV. What is a segmentation fault (a.k.a. a segfault)?**

A segmentation fault occurs when we exceed the area of memory we were trying to access, like if we try to reach out of bounds of an array.

**V. What are the ESI and EDI registers for?**

The ESI register is the source index register, and the EDI register is the destination index register.

## Ghidra Analysis

When running the program, we can see that it requires a key. If we enter an integer (except for presumably the right key), we get a 'nope' as an answer. However, I noticed that if we input a string of any kind it tells us that we are correct and have to go keygen the file. So, next we'll look into the file with Ghidra.

First, we decide to look into the main function. While inspecting it, we find an interesting function: `validate_key`. This function seems to take in our input and modulus it with 0x4c7 (1223), and if the result is 0 then we correctly cracked it. This means that any integer that is divisible by 1223 is a possible key.
