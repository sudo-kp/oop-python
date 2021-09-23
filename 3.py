import sys


def is_formula(str, k):
	if not(str[k] in '1234567890+-'):
		return False
	if k==len(str)-1:
		if str[k].isdigit():
			return True
		else:
			return False
	if str[k] in '+-' and str[k+1] in '+-':
		return False
	return is_formula(str, k+1)

try:
	if is_formula(sys.argv[1], 0):
		print("True, ", eval(sys.argv[1]))
	else:
		print("False, ", None)	
except:
	print('error.')
