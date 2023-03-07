#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Source code for the Assembly Machine (Asm)

from inspect import signature

from ram.defs import mnemonics, registers, op_codes, reg_codes

class Assembler(object):
    def __init__(self):
        self.program = bytearray()
    
    def collect(self, instruction):
        self.program.extend(instruction)
    
    def mnemonic(self, opcode, *args):
        op_lambda = mnemonics[opcode]
        op_parameters = signature(op_lambda).parameters
        if (len(args)+1) != len(op_parameters):
            raise ValueError("Mnemonic signature mismatch")
        else:
            ret = op_lambda(op_codes[opcode], *args)
            self.collect(ret)
    
    def pretty_print(self):
        for i in range(0, len(self.program), 4):
            line = '{:04X}'.format(i)
            byte_bin, byte_hex = ('','')
            for j in range(4):
                if i+j < len(self.program):
                    byte_value = self.program[i+j]
                    byte_bin += '{:08b} '.format(byte_value)
                    byte_hex += '{:02X} '.format(byte_value)
            print("| {} | {} | {} |".format(line, byte_bin.strip(), byte_hex.strip()))
    
    def mov(self, rg2, rg1):
        return self.mnemonic("MOV", reg_codes[rg2], reg_codes[rg1])
    
    def wrt(self, rg1, value):
        return self.mnemonic("WRT", reg_codes[rg1], value)