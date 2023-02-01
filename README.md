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

* The EXE and DLL files seem to be malware
* The DLL file appears to be mimicing kernel32.dll and trying to corrupt our system32 file.
* Both programs appear to have come from the same person, leading me to assume that the EXE file is meant to run the DLL file.

### Indicators of Compromise

Indicators of our system being compromised are the dates/time in which they were compiled, the hashes of the DLL and EXE files, and the location of the DLL file. The compilation time of both files is so close that it can be presumed that the files came together and, most likely, were created by the same person. The location of the file in question "kerne132.dll" is located within "system32", an indication that this file means to manipulate our system. Lastly, the hashes of both files are:

MD5 Hash (EXE):  bb7425b82141a1c0f7d60e5106676bb1

MD5 Hash (DLL):  290934c61de9176ad682ffdd65f0a669

Date of Compilation (EXE): 2010/12/19 Sun 16:16:19 UTC

Date of Compilation (DLL): 2010/12/19 Sun 16:16:38 UTC


### Mitigations

To mitigate the potential harm these files could cause on our system, we need to search the machines for files in the "system32" directory titles "kerne132.dll" and delete them, as well as find any files that match these files hashes and delete them.

### Evidence

Firstly, using PEview reveals some interesting information for us. If we look into the EXE file, we will notice that under the "SECTION .data" section, we can find the message "WARNING_THIS_WILL_DESTROY_YOUR_MACHINE", which is a message that may indicate that this is malicious software. Secondly, after reviewing this section, we notice the appearance of "kerne132.dll" and "kernel32.dll" being manipulated in the "system32" directory, leading me to assume that "kerne132.dll" is meant to mimic the original kernel file in order to gain access to the systems software, acting as a trojan horse.

After analyzing the DLL and EXE files, if we go into the "IMAGE_FILE_HEADER" sections using PEview we notice that both files were created within seconds of one another. This may indicate to us that these programs were created by the same person and most likely work in unison to corrupt our data.
