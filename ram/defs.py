#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Assembler definition

from struct import pack

mnemonics = {
    'MOV': lambda op, rg2, rg1: pack('Bx2B', op, rg2, rg1),
    'WRT': lambda op, reg, val: pack('2BH', op, reg, val),
    'CMP': lambda op, rg2, rg1: pack('Bx2B', op, rg2, rg1),
    'JP' : lambda op, reg, val: pack('2BH', op, reg, val),
    'JV' : lambda op, val: pack('BxH', op, val),
    'JR' : lambda op: pack('B3x', op),
    'JE' : lambda op, val: pack('BxH', op, val),
    'JN' : lambda op, val: pack('BxH', op, val),
    'JL' : lambda op, val: pack('BxH', op, val),
    'JG' : lambda op, val: pack('BxH', op, val),
    'ADD': lambda op: pack('B3x', op),
    'SUB': lambda op: pack('B3x', op),
    'INC': lambda op: pack('B3x', op),
    'DEC': lambda op: pack('B3x', op),
    'SAV': lambda op, reg: pack('B2xB', op, reg),
    'RTR': lambda op, reg: pack('B2xB', op, reg),
    'SWP': lambda op, rg2, rg1: pack('Bx2B', op, rg2, rg1),
    'NOP': lambda op: pack('B3x', op),
    'HLT': lambda op: pack('B3x', op)
}

registers = (
    'PTR', 
    'TMP', 
    'ACC', 
    'CNT', 
    'STO', 
    'FLAGS'
)

flags = (
    'CF', # Carry Flag
    'ZF', # Zero Flag
)

op_codes = {v: i for i, v in enumerate(mnemonics, start=0x01)}
reg_codes = {v: i for i, v in enumerate(registers, start=0x01)}