import cProfile
import random

def f1(lIn):
	l1 = sorted(lIn)
	l2 = [i for i in l1 if i<0.5]
	return [i*i for i in l2]

lIn = [random.random() for i in range(100000)]

cProfile.run('f1(lIn)')