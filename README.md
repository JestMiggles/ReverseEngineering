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
* The DLL file appears to be mimicking kernel32.dll and trying to corrupt our system32 file.
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

## Lab 1-2
### Executive Summary

After analyzing the file Lab01-02.exe, we can concur that this is some kind of malware. It seems to run functions to connect to the internet and redirect you to a website. The website is currently not running so I am uncertain of what this website was supposed to do.

### Indicators of Compromise

Some indications that we were compromised are the functions being inplemented in the file and the location it's targeting.

MD5 Hash: ae4ca70697df5506bc610172cfc288e7

Website: http://www.malwareanalysisbook.com

### Mitigations

To mitigate the damage this program can cause, we can send the hash out to all that may be infected to help them remove the target file and make sure they don't download it if they don't have it yet. We can also block the target website from our network to make sure that we cannot receive data from it, including any malware it may be trying to give us.

### Evidence

When first using PEview on the file, we will see that it is packed and therefore some of the information is compacted and hard to read. So, to get around this we use "upx" to unpack the file so that we can fully see what is inside the file. Afterwards, when we inspect the contents we find some interesting data. We find that this EXE file is running a lot of programs, such as "InternetOpenUrlA" and "InternetOpenA" which are programs that are used to connect us to the internet and send us to a URL. We can also see in the "SECTION .data" section that there is a URL within the file "http://www.malwareanalysisbook.com". Although it is unclear what the purpose of the website is because it is no longer up, I assume it would've been used to download malware to the host computer. Lastly, we see that the program utilizes the kernel32.dll file, most likely trying to hide itself from Windows Defender.

## Lab 1-3
### Executive Summary

After analyzing the file Lab01-03.exe, we find that:
* The file is packed with FSG
* Utilizes functions as main attack from information available

### Indicators of Compromise

There are not a lot of indicators to go off of for this file since it is packed and unable to be packed with any of the tools we have present.

MD5 Hash: 9c5c27494c28ed0b14853b246b113145

### Mitigations

The best way to mitigate the damage that this file can do at the present moment is to search all machines on your network for files matching the target files hash as shown above.

### Evidence

First, I decided to analyze it in PEview. After going through most of the files I found nothing really of note except for in the "SECTION" part of the Lab. In this part, I found two functions of relevance: LoadLibraryA and GetProcAddress. However, without further information, I was unable to tell exactly the purpose of these functions for the malware.

Second, I ran it through Dependency Walker and found evidence for the malware being packed. Unable to unpack the malware using UPX I decided to look into the back of the book for how to unpack this file and found that you need to use FSG (Fast, Small, Good) in order to unpack it, however I could not find a reliable source that was able to unpack the file.

I also inserted the file into VirusTotal and found that the malware started circulating around 2011-03-26 and seem consistent with being from our book. Otherwise, I found no other important information pertaining to my report.

## Lab 1-4
### Executive Summary

After analyzing the file Lab01-04.exe, we find that:
* This is indeed malware
* It tracks your information, such as keyboard input and files accessed.
* It runs programs in your system32 directory.
* Website URL and website programs.

### Indicators of Compromise

Some indicators that our system has been compromised are the files that are being installed on our system and the location that these files are being downloaded in. The files being downloaded on our system that are suspiscious are: wupdmgr.exe and winup.exe. These may correlate with a website that we found within the files: http://practicalmalwareanalysis.com/updater.exe

MD5 Hash: 625ac05fd47adc3c63700c3b30de79ab

### Mitigations

Ways to mitigate the damage that this file can have on your system or network is to send the hash code to all computers on the network to prevent the spread or remove it on compromised machines. Another way would be to block the url stated above from sending packets or dropping packets that this network sends to your machines.

### Evidence

Putting the file into VirusTotal shows us that this file has been circulating since 2011-07-05 and that it was *supposedly* created 2019-08-30 which I personally found funny.

Using PEview and Dependency Walker, we are able to see that this file is, as far as I could tell, not packed or otherwise encrypted. Looking through the "SECTION .data" part of our file using PEview reveals that our program has created two files in our system32 directory: wupdmgr.exe and winup.exe. After looking up these files online I found that these are used to track keyboard input, files that are being accessed, and open Internet and LAN ports. Then, after looking in the "SECTION .rsrc" part of our file we find a link presumably being used in tandom with the files wupdmgrd.exe and winup.exe. Although the domain is not currently owned, I would presume that the file wupdmgrd.exe is used to send the information collected to the URL to be collected.

# Week 3 - Dynamic Analysis

## Lab 3-1
### Executive Summary

After analyzing Lab03-01, we find that:
* The file is packed.
* It communicates with a website.
* When ran, can 

### Indicators of Compromise

Some indicators that we were compromised are the hash of the file Lab03-01.exe matching the hash of the file vmx32to64.exe and that the malware was communicating with a website: www.practicalmalwareanalysis.com.

MD5 Hash (both files): d537acb8f56a1ce206bc35cf8ff959c0

### Mitigations

Some ways that we can mitigate the potential threat this program imposes on our system is by searching all affected machines and those on the same network for files with the same hash and remove them, drop all packages sent to us from the site mentioned above, and block the site from sending or receiving information from us.

### Evidence

When putting the file into VirusTotal, we see that this file has been pinged as malware by multiple different sites. We see also that the hash matches what we found when analyzing the file for its hash and that the file is supposedly packed. It is packed with PENinja, however I could not find a reliable source to download this packer so I was unable to unpack it, so we'll just have to analyze it without unpacking.

Now for the static analysis. Inserting this file into Dependency Walker shows us that there is only one module within the file, kernel32.dll, and one process that was being ran with it, ExitProcess. This is suspiscious since we would expect our program to be doing much more, so I will check to see if maybe it is packed. After using PEview I see no obvious signs of it being packed, however when using VirusTotal saw that it was. Using strings on the file showed us that 
