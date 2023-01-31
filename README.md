# CS479/579 Reverse Engineering at NMSU

## Summary

This repo will hold your reports on reverse engineering malware samples from "Practical Malware Analysis".

## Setup

In order to setup my system for reverse engineering, I had to format a USB to run Ubuntu off of rather than my own system, since my original system is in Windows. After preparing my USB for Ubuntu, I was able to dual-boot my system into Ubuntu. Next, I installed a Windows virtual machine to run the malware.

## Installed

We currently have not ran software on our machines, however this section will be updated in the future.

# Week 1 - Simple Static Analysis

## Lab 1-1
### Executive Summary

While analyzing the software, I discovered a file "kerne132.dll" within the system32 file directory, indicating that this file may have been used to create a backdoor into our system.

### Indicators of Compromise

Indicators of our system being compromised are the dates/time in which they were compiled, the hashes of the DLL and EXE files, and the location of the DLL file. The compilation time of both files is so close that it can be presumed that the files came together and, most likely, were created by the same person. The location of the file in question "kerne132.dll" is located within "system32", an indication that this file means to manipulate our system. Lastly, the hashes of both files are:

MD5 Hash (EXE):  bb7425b82141a1c0f7d60e5106676bb1\n

MD5 Hash (DLL):  290934c61de9176ad682ffdd65f0a669

### Mitigations

To mitigate the potential harm these files could cause on our system, we need to search the machines for files in the "system32" directory titles "kerne132.dll" and delete them, as well as find any files that match these files hashes and delete them.

### Evidence

Firstly, analyzing the EXE file in strings 
