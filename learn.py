import numpy as np
	import math
	a = [np.array([[0, 1, 1], [1, 1, 1],[1,0,1]]),np.array([[0, 1, 1], [1, 1, 1],[1,0,1]]),np.array([[0, 1, 1], [1, 1, 1],[1,0,1]])]
	print type(a[0][1])
	k=[]
	n=3
	x=np.array([1,2,3])
	pixlist=[]
	pixavg=0
	b=np.zeros(shape=(n,n))
	for i in xrange(n):
	b+=a[i]
	c = np.eye(n)
	b*=c
	for i in xrange(n):
	up=-0.5 * np.dot(np.dot(x.transpose() , a[i]), x)
	up=math.exp(up)
	rank=np.linalg.matrix_rank(a[i])
	pix=(2*math.pi) ** (-rank)
	pix*= (abs(np.linalg.det(a[i])) ** 0.5)
	pix*= math.exp(-0.5*np.dot(np.dot(x.transpose() , a[i]), x)) #x-meu
	pixavg+=pix
	pixlist.append(pix)
	left=pix/up
	left=math.log(left) / (float(n-1)/2)
	left=math.exp(left)
	k.append(left)
	pix/=3
	print k
	kmax=sorted(k)[-1]
	pikavg=0
	for i in xrange(n):
	pixkhere=-0.5 * np.dot(np.dot(x.transpose() , a[i]), x)
	pixkhere=math.exp(pixkhere)
	uphere=pixkhere
	pixkhere=kmax**(float(n-1)/2)
	expr=math.exp(n*math.log(pixkhere))*math.sqrt(2*math.pi*k[i]*k[i]/n)
	expr/=n
	expr/=uphere
	pikavg+=expr
	pikavg/=n
	kr=math.exp(math.log(pikavg)/(float(n-1)/2))
	print kr
