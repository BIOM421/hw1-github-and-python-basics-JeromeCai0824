def hello_world():
	return "Hello World!"

def hello_world_n(N):
	string = hello_world()
	for n in range(1,N):
		string += ' ' + hello_world()
	return string

print(hello_world_n(3))