# Detecting DLL Injection

### Answers

**1) Prove that the loader is using DLL injection. (Don't forget a relevant snapshot in Ghidra.)**

**2) Identify the process that will be injected into. Seeing a string in Ghidra isn't sufficient -- explain how the process gets selected.**

**3) Identify the entry point of the DLL injection. Where is DllMain?**

**4) This malware does something every ______ seconds. How often, and where is the loop where that waiting happens?**

This malware does something every 60,000 milliseconds, or 60 seconds. This loop is within our program `Lab12-01.dll` and is in the function I renamed to injection.

**5) What does the malware do every _______ seconds?**
