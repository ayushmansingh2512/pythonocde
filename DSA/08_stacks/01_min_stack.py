class Minstack:
	def __init__(self):
		self.stack = []
	def push(self,x):
		#determine the new minimum value 
		if not self.stack:
			current_min = x
		else:
			current_min = min(x,self.stack[-1][1])
		self.stack.append((x,current_min))
	def pop(self):
		self.stack.pop()
	def top(self):
		return self.stack[-1][0]
	def getMin(self):
		return self.stack[-1][1]

minstack = Minstack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
minstack = Minstack()
minstack.push(-2)
minstack.push(0)
minstack.push(-3)
print(minstack.getMin())  # Output: -3
minstack.pop()
print(minstack.top())     # Output: 0
print(minstack.getMin())  # Output: -2