#!/usr/bin/env python
from pwn import *
import os

#context.log_level = 'critical'

# To load the binary
elf = ELF('./be-quick-or-be-dead-1')

# To make changes in a particular function
# elf.asm(address, assembly)
number = 0xeb866516  # got this number after disassembling the calculate_key function

elf.asm( elf.symbols['set_timer'],'ret') # explicit 'ret' in assembly skips the function
print(number)
elf.asm( elf.symbols['calculate_key'],'mov eax,%s\nret\n' %(number & 0xFFFFFFFF))
elf.save('./patched_be-quick-or-be-dead-1')

# For direct execution via this python file ==

os.system('chmod +x ./patched_be-quick-or-be-dead-1')	# For making file executable
p = process('./patched_be-quick-or-be-dead-1') 		# To initiate a process or to run the binary
p.poll('true')						# Poll till the function exits
print(p.recvall())
