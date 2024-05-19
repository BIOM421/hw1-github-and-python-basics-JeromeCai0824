def hello_world():
	return "Hello World!"

def hello_world_n(N):
	string = ''
	for n in range(0,N):
		string += hello_world() + ' '
	return string