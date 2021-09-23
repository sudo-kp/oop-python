#import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('a', type=str)
#parser.add_argument('s', type=str)
#parser.add_argument('b', type=str)
#args = parser.parse_args();
#expr = args.a + args.s + args.b
#print(eval(expr))


import sys

try:
	print(eval(sys.argv[1]))
except:
	print('Error')
