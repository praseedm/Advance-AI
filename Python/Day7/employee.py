#!/usr/bin/env python
class employee:
	slno=200

	def __init__(self):
		self.empno = employee.slno
		employee.slno += 1
	
	def store(self):
		self.name=raw_input("name?")
		self.salary=raw_input("salary")
		print "...stored..."
	
	def display(self):
		print "Emp no:%d , Name:%s , Salary:%s"%(self.empno,self.name,self.salary)

s1=employee()
s1.store()
s1.display()			
