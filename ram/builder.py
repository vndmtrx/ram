#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Source code for the Assembly Machine (Asm)

from inspect import signature
from struct import pack

from ram.defs import mnemonic_defs, registers, opcodes, reg_codes

class Assembler(object):
    def __init__(self):
        self.program = bytearray()
    
    def collect(self, instruction):
        self.program.extend(instruction)
    
    def mnemonic(self, op, *args):
        ret = pack(mnemonic_defs[op], opcodes[op], *args)
        self.collect(ret)
    
     def parse_program(self, string):
        pass
    
    def pretty_print(self):
        for i in range(0, len(self.program), 4):
            line = f'{i:04X}'
            byte_bin, byte_hex = ('','')
            for j in range(4):
                if i+j < len(self.program):
                    byte_value = self.program[i+j]
                    byte_bin += f'{byte_value:08b} '
                    byte_hex += f'{byte_value:02X} '
            print(f'| {line} | {byte_bin.strip()} | {byte_hex.strip()} |')
    
    def mov(self, rg2, rg1):
        return self.mnemonic("MOV", reg_codes[rg2], reg_codes[rg1])
    
    def wrt(self, rg1, value):
        return self.mnemonic("WRT", reg_codes[rg1], value)
    
    def cmp(self, rg2, rg1):
        return self.mnemonic("CMP", reg_codes[rg2], reg_codes[rg1])
    
    def jp(self, value):
        return self.mnemonic("JP", value)
    
    def je(self, value):
        return self.mnemonic("JE", value)
    
    def jn(self, value):
        return self.mnemonic("JN", value)
    
    def jl(self, value):
        return self.mnemonic("JL", value)
    
    def jg(self, value):
        return self.mnemonic("JG", value)
    
    def add(self, rg1):
        return self.mnemonic("ADD", reg_codes[rg1])
    
    def sub(self, rg1):
        return self.mnemonic("SUB", reg_codes[rg1])
    
    def inc(self):
        return self.mnemonic("INC")
    
    def dec(self):
        return self.mnemonic("DEC")
    
    def sav(self, rg1):
        return self.mnemonic("SAV", reg_codes[rg1])
    
    def rtr(self, rg1):
        return self.mnemonic("RTR", reg_codes[rg1])
    
    def swp(self, rg2, rg1):
        return self.mnemonic("SWP", reg_codes[rg2], reg_codes[rg1])
    
    def nop(self):
        return self.mnemonic("NOP")
    
    def hlt(self):
        return self.mnemonic("HLT")