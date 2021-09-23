
def dynam_solut(weights, capasity):
	table = [[0 for x in range(capasity+1)] for x in range(len(weights)+1)]
	for i in range(1, len(weights)+1):
		for j in range(1, capasity+1):
			if int(weights[i-1]) <= j:
				table[i][j] = max(int(weights[i-1])+table[i-1][j-int(weights[i-1])],
					table[i-1][j])
			else:
				table[i][j] = table[i-1][j]
	return table[len(weights)][capasity]

try:
	input_string = input("Enter weights of bars: ")
	weights = input_string.split()
	print(weights)
	input_string = input("Enter the capasity of knapsack: ")
	capasity = int(input_string)
	print('Max weight of gold: ', dynam_solut(weights, capasity))
except:
	print('error')