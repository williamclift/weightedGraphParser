'''
  Scanner
      @author William Clift
      @date   20 April 2021
    Prin. Prog. Lang. - Dr. Mongan

    Run:
      python scanner.py
'''

'''
Samples to Run (Include the quotations):
	'someNode - 5 > anotherNode'
	'someNode - > anotherNode'
	'someNode - 5 > anotherNode < - aFinalNode'


'''


'''
Weighted and Directed Graphs - Defines the connections between nodes with the option for weighted edges

0. 				- >				node - > node 
1. 				< -				node < - node
2(weight). 		- [0-9]* >		node - weight > node
3(weight). 		< [0-9]* -		node < weight - node
4. 				weight			[0-9]*

'''
const = ['-', '<', '>']
nodes = []
tokens = []

def isWeight(w):
	if w.isdigit():
		return True
	else:
		return False

def getToken():
	result = tokens.pop()
	if result == '-' or result == '<':
		next = tokens.pop()
		if isWeight(next):
			next += ' ' + tokens.pop()
		result += ' ' + next
	return result

def getNode():
	return nodes.pop()

def processString(string):
	arr = string.split(' ')
	i = 0
	while i in range(len(arr)):
		e = arr[i]
		if e == '-':
			next = arr[i+1]
			if isWeight(next):
				i+=1
				tokens.insert(0, str(2)+'('+str(next)+')')
			else:
				tokens.insert(0, str(0))
			i+=1
		elif e == '<':
			next = arr[i+1]
			if isWeight(next):
				i+=1
				tokens.insert(0, str(3)+'('+str(next)+')')
			else:
				tokens.insert(0, str(1))
			i+=1
		else:
			nodes.insert(0, e)
		i+=1


string = input("Graph Structure: ")
print(string)
processString(string)
print(nodes)
print(tokens)

while len(nodes) > 0:
	print(getNode())
	if len(tokens) > 0:
		print(getToken())






