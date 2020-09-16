def collatz(n):
	d = {}
	for i in range(1 ,n+1):
		d[str(i)] = 1
	for i in range(1 , n+1):
		if d[str(i)] != 1:
			pass
		else:
			varin = n
			orig = i
			fake = {}
			fake[str(orig)] = 1
			while i != 1:
				if i %2 == 0:
					i = int(i/2)
					if i > varin:
						for k in range(varin+1 , i+1):
							d[str(k)] = 1
						varin = i
					if (d[str(i)] != 1) or (orig ==2) :
						for x in list(fake.keys()):
							fake[str(x)] = fake[str(x)] + d[str(i)]
						i = 1
					else:
						for x in list(fake.keys()):
							if str(i) not in list(fake.keys()):
								fake[str(i)] = 1
							fake[x] = fake[x] + 1
				else:
					i = 3*i + 1
					if i > varin:
						for k in range(varin+1 , i+1):
							d[str(k)] = 1
						varin = i
					if (d[str(i)] != 1) or (orig ==2) :
						for x in list(fake.keys()):
							fake[str(x)] = fake[str(x)] + d[str(i)]
						i = 1
					else:
						for x in list(fake.keys()):
							if str(i) not in list(fake.keys()):
								fake[str(i)] = 1
							fake[x] = fake[x] + 1
			for x in list(fake.keys()):
				d[x] = fake[x]
	return(d)

def num(n):
	d={}
	for i in range(3, n+1):
		d[str(i)] = 1
	d[str(1)] = 1
	d[str(2)] = 2
	for i in range(3 , n+1):
		count = 0
		orig = i
		while i > 1:
			if i < orig:
				d[str(orig)] = count + d[str(i)] 
				i = 1
			else:
				if i % 2 ==0 :
					i = int(i/2)
					count = count + 1
				else:
					i = 3*i + 1
					count = count + 1
	print(d.values().index(max(d.values()))+1)
