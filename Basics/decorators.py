def get_func():
	print("Inside get function")
	def return_func():
		print("Inside return function")
		return 1
	print("Outside return function")
	return return_func()

#print(return_func)
x = get_func()
print("*********************************************")
print(get_func())
print("*********************************************")
x
print("*********************************************")
x()
print("***********************************************")

