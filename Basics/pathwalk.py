import os

def path_call(path):
	for child in os.listdir(path):
		childPath = os.path.join(path,child)
		#print(childPath)
		if os.path.isdir(childPath):
			path_call(childPath)
		else:
			print(childPath)

print("Give me a path")

path_call(input())