#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Assembler definition

from struct import pack

func_op           = lambda op: pack('B3x', op)
func_op_addr      = lambda op, rg1: pack('B2xB', op, rg1)
func_op_addr_addr = lambda op, rg2, rg1: pack('Bx2B', op, rg2, rg1)

func_op_val       = lambda op, val: pack('BxH', op, val)
func_op_addr_val  = lambda op, rg1, val: pack('2BH', op, rg1, val)

mnemonics = {
    'MOV': func_op_addr_addr,
    'WRT': func_op_addr_val,
    'CMP': func_op_addr_addr,
    'JP' : func_op_val,
    'JE' : func_op_val,
    'JN' : func_op_val,
    'JL' : func_op_val,
    'JG' : func_op_val,
    'ADD': func_op_addr,
    'SUB': func_op_addr,
    'INC': func_op,
    'DEC': func_op,
    'SAV': func_op_addr,
    'RTR': func_op_addr,
    'SWP': func_op_addr_addr,
    'NOP': func_op,
    'HLT': func_op
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