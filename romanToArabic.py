class Solution(object):
	@staticmethod
	def roman_to_int(s):
		roman_digit_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		roman_integer_input = []
		for digit in s:
			roman_integer_input.append(digit)
		print(roman_integer_input)
		int_to_return = 0
		tumbler = True
		for roman_symbol_index in range(len(roman_integer_input)):
			if roman_integer_input[roman_symbol_index] == 'I' and roman_integer_input[roman_symbol_index + 1] in ('V', 'X') and tumbler is True:
				"""Тут отнимается потому что на следующем круге прибавится 10"""
				int_to_return -= 1
				tumbler = False
			elif roman_integer_input[roman_symbol_index] == 'X' and roman_integer_input[roman_symbol_index + 1] in ('L', 'C') and tumbler is True:
				int_to_return -= 10
				tumbler = False
			elif roman_integer_input[roman_symbol_index] == 'C' and roman_integer_input[roman_symbol_index + 1] in ('D', 'M') and tumbler is True:
				int_to_return -= 100
				tumbler = False
			else:
				int_to_return += roman_digit_list[roman_integer_input[roman_symbol_index]]
				tumbler = True
		return int_to_return


x = Solution
result = x.roman_to_int('MCMXCIV')
print(result)
