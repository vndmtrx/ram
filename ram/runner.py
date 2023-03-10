#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Source code for the Assembly Machine (Asm)

from ram.defs import mnemonics, registers, op_codes, reg_codes

class Machine(object):
    def __init__(self, program):
        self.reg = {'PTR': 0, 'TMP': 0, 'ACC': 0, 'CNT': 0, 'STO': 0}
        self.pc = 0
        self.program = program
    
    def execute(self):
        while True:
            op = struct.unpack_from('B', self.program, offset=self.pc)
            
            if op == op_codes['MOV']:
                rg2, rg1 = struct.unpack_from('xx2B', self.program, self.pc)
            if op == op_codes['JP']:
                value = struct.unpack_from('xxH', self.program, self.pc)
                continue
                
            self.pc += struct.calcsize('4B')