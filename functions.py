
import sys

def hex_add_1(Cell1):
	hexnum = "0x"+Cell1
	result = hex(int(hexnum,16) + 1)
	result = result.lstrip('0x').rstrip('L')
	result = result.upper()
	return result

