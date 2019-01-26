class A(object):
	def go(self):
		print("Go A go")
	def stop(self):
		print("Stop A stop")
	def pause(self):
		raise Exception("Not implemented")

class B(A):
	def go(self):
		super(B,self).go()
		print("Go B go")

class C(A):
	def go(self):
		super(C,self).go()
		print("Go C go")
	def stop(self):
		super(C,self).stop()
		print("stop C stop")

class D(B,C):
	def go(self):
		super().go()
		print("Go D go")
	def stop(self):
		super().stop()
		print("Stop D stop")
	def pause(self):
		print("Wait D wait")
class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

#a.go()
#b.go()
#c.go()
d.go()
#e.go()

#a.stop()
#b.stop()
#c.stop()
d.stop()
#e.stop()

d.pause()
#e.pause()
#a.pause()
#b.pause()