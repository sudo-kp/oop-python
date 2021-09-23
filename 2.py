import sys
import math

function_dict = {'add':'+', 'sub':'-', 'mul':'*',
                 'div':'/', 'sin':'math.sin(', 'cos':'math.cos(',
                 'tg':'math.tan('}

try:
	if len(sys.argv)==4:
		expr=sys.argv[2]+function_dict[sys.argv[1]]+sys.argv[3]
		result=eval(expr)
		print(result)
	elif len(sys.argv)==3:
		expr=function_dict[sys.argv[1]]+sys.argv[2]+')'
		result = eval(expr)
		print(result)
except:
	print('error.')
	

	
