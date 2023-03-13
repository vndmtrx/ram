#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Assembler definition

from struct import pack

mnemonics = {
    'MOV': 'Bx2B', # OP REG2 REG1
    'WRT': '2BH' , # OP REG1 INT
    'CMP': 'Bx2B', # OP REG2 REG1
    'JP' : 'BxH' , # OP INT
    'JE' : 'BxH' , # OP INT
    'JN' : 'BxH' , # OP INT
    'JL' : 'BxH' , # OP INT
    'JG' : 'BxH' , # OP INT
    'ADD': 'Bx2B', # OP REG2 REG1
    'SUB': 'Bx2B', # OP REG2 REG1
    'INC': 'B3x' , # OP
    'DEC': 'B3x' , # OP
    'SAV': 'Bx2B', # OP REG2 REG1
    'RTR': 'Bx2B', # OP REG2 REG1
    'SWP': 'Bx2B', # OP REG2 REG1
    'NOP': 'B3x' , # OP
    'HLT': 'B3x' , # OP
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