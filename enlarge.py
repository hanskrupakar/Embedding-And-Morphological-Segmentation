with open('input', 'r+') as f:
	tam = f.read()
	f.seek(0)
	f.write(tam * 20)
	f.truncate()
