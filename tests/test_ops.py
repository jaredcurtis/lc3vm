import lc3vm.constants as C
import lc3vm.ops
import lc3vm.utils
import unittest2


class Opcodes(unittest2.TestCase):
    def setUp(self):
        self.registers = [0] * C.R_COUNT

    def test_add(self):
        """Add R1, R2 store R0"""
        instr = lc3vm.utils.set_bits(0, [12, 6, 1])
        self.registers[C.R_R0] = 0
        self.registers[C.R_R1] = 1
        self.registers[C.R_R2] = 2

        lc3vm.ops.add(self.registers, instr)
        self.assertEqual(self.registers[C.R_R0], 3)
        self.assertEqual(self.registers[C.R_R1], 1)
        self.assertEqual(self.registers[C.R_R2], 2)

    def test_immediate_add(self):
        """Add R1, 5 store R0"""
        instr = lc3vm.utils.set_bits(0, [12, 6, 5, 2, 0])
        self.registers[C.R_R0] = 0
        self.registers[C.R_R1] = 1

        lc3vm.ops.add(self.registers, instr)
        self.assertEqual(self.registers[C.R_R0], 6)
        self.assertEqual(self.registers[C.R_R1], 1)

    def test_immediate_add_negative(self):
        """Add -10, 5 store R0"""
        instr = lc3vm.utils.set_bits(0, [12, 6, 5, 2, 0])
        self.registers[C.R_R0] = 0
        self.registers[C.R_R1] = -10

        lc3vm.ops.add(self.registers, instr)
        self.assertEqual(self.registers[C.R_R0], -5)

    def test_update_flags(self):
        self.registers[C.R_R0] = 0
        self.registers[C.R_R1] = lc3vm.utils.set_bits(0, [16])
        self.registers[C.R_R2] = 1

        lc3vm.ops.update_flags(self.registers, C.R_R0)
        self.assertEqual(self.registers[C.R_COND], C.FL_ZRO)

        lc3vm.ops.update_flags(self.registers, C.R_R1)
        self.assertEqual(self.registers[C.R_COND], C.FL_NEG)

        lc3vm.ops.update_flags(self.registers, C.R_R2)
        self.assertEqual(self.registers[C.R_COND], C.FL_POS)
