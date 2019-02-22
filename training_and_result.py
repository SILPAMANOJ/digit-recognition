import numpy as np
import progress_bar as prb

def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))


def func(a1, output, arr, brr):
	a1 = a1/255

	for j in range(1):

		a2 = nonlin(np.dot(a1, arr))
		a3 = nonlin(np.dot(a2, brr))
		#sys.exit(0)

		op = np.zeros((10, 1))
		op[output] = 1.0
		op = np.resize(op, (1, 10))

		derivative = op-a3
		derivative = derivative * nonlin(a3, True)

		derivative1 = derivative.dot(np.transpose(brr))
		derivative1 = derivative1 * nonlin(a2, True)

		brr += np.dot(np.transpose(a2), derivative)
		arr += np.dot(np.transpose(a1), derivative1)

	return arr, brr

def training(inputt, output):
	np.random.seed(1)

	# Weight Holder. IMPORTANT/TRAINEE/FUTURE
	arr = np.random.uniform(-1.0, 1.0, (len(inputt[0]), 20)) #transpose
	brr = np.random.uniform(-1.0, 1.0, (20, 10))	#same, duh!

	print ("Network training:")

	for i in range(len(inputt)):
		a1 = np.resize(inputt[i], (1, len(inputt[i])))
		arr, brr = func(a1, output[i], arr, brr)

		if(i%1000 == 0):
			prb.progress(i, len(inputt))
	prb.progress(len(inputt), len(inputt), cond=True)
	print()

	return arr, brr

def judgement(inputt, output, arr, brr):
	
	co = 0
	print ("Network testing:")
	for i in range(len(inputt)):
		st = np.resize(inputt[i], (1, len(inputt[i])))
		st = st/255
		mid = nonlin(np.dot(st, arr))
		end = nonlin(np.dot(mid, brr))

		ind = np.argmax(end)
		if(ind == output[i]):
			co += 1
		if(i%1000 == 0):
			prb.progress(i, len(inputt))
	prb.progress(len(inputt), len(inputt), cond=True)
	print('\n')

	print (inputt)
	print ("Accuracy : ", ((co/ len(inputt)) * 100), '%')
	print (output)
