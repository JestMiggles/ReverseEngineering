# Detecting DLL Injection

### Answers

**1) Prove that the loader is using DLL injection. (Don't forget a relevant snapshot in Ghidra.)**

In screenshots [], we see that the program is searching each library and retrieving all processes within them. After this, it sends each process to another function where it is compared with a string to see if we've found the correct process yet.

**2) Identify the process that will be injected into. Seeing a string in Ghidra isn't sufficient -- explain how the process gets selected.**

The process that is being injected into is `explorer.exe`. This is done by the program retrieving all the processes within the different libraries and seeing if any of them match the target processes name.

**3) Identify the entry point of the DLL injection. Where is DllMain?**

The entry point of the DLL injection was renamed `entry` in Ghidra. After renaming it and giving it the proper function signature, we successfully rename it to `DLLMain`.

**4) This malware does something every ______ seconds. How often, and where is the loop where that waiting happens?**

This malware does something every 60,000 milliseconds, or 60 seconds. This loop is within our program `Lab12-01.dll` and is in the function I renamed to `injection`.

**5) What does the malware do every _______ seconds?**

The malware creates a window on the users screen every 60 seconds.
