with open('Morph2Vec.TA', 'r+') as f:
	tam = f.read()
	f.seek(0)
	f.write(tam * 20)
	f.truncate()
