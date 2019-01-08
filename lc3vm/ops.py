import lc3vm.constants as c


def update_flags(registers, r):
    if registers[r] == 0:
        registers[c.R_COND] = c.FL_ZRO
    elif registers[r] >> 15:  # a 1 in left-most bit indicates negative
        registers[c.R_COND] = c.FL_NEG
    else:
        registers[c.R_COND] = c.FL_POS


def mem_read(memory, address):
    return memory[address]


def sign_extend(x, bit_count):
    if x >> (bit_count - 1) & 1:
        x |= 0xFFFF << bit_count
    return x


def add(registers, instr):
    r0 = (instr >> 9) & 0x7  # destination register
    r1 = (instr >> 6) & 0x7  # source register
    imm_flag = (instr >> 5) & 0x1  # immediate mode?

    if imm_flag:
        imm5 = sign_extend(instr & 0x1F, 5)
        registers[r0] = registers[r1] + imm5
    else:
        r2 = instr & 0x7  # second source register
        registers[r0] = registers[r1] + registers[r2]

    update_flags(registers, r0)


def ldi(registers, instr):
    r0 = (instr >> 9) & 0x7
    pc_offset = sign_extend(instr & 0x1ff, 9)
    registers[r0] = mem_read(mem_read(registers[c.R_PC] + pc_offset))

    update_flags(registers, r0)
