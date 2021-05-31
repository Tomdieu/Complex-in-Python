import math

class Complex(object):
	"""docstring for Complex"""
	def __init__(self, re=0,im=0):
		super(Complex, self).__init__()
		self.re = re
		self.im = im

	def __str__(self):
		if self.im>=0:
			return f'{self.re}+{self.im}i'
		else:
			return f'{self.re}-{-self.im}i'

	def __sub__(self,other,/):
		"used to subtract two complex number"
		try:
			return Complex(self.re-other.re,self.im-other.im)
		except :
			return Complex(self.re-other,self.im)
	def __add__(self,other,/):
		"""used to add two complexe number"""
		try:
			return Complex(self.re+other.re,self.im+other.im)
		except:
			return Complex(self.re+other,self.im)
	def __mul__(self,other,/):
		"""used to multiply two complex number """
		try:
			return Complex(((self.re*other.re)+(-1*(self.im*other.im))),((self.re*other.im)+(other.re*self.im)))
		except :
			return Complex(other*self.re,other*self.im)
	def __truediv__(self,other,/):
		"""used to divide two complex number"""
		c=Complex(self.re,self.im)
		try:
			c1=c*(~other)
			a=other.re**2
			b=other.im**2
			d=a+b
			return Complex(c1.re/d,c1.im/d)
		except :
			return Complex(self.re/other,self.im/other)
	def __invert__(self):
		"""
		used to find the conjugate of a complex number 
		
		to find the conjugate used the symbole ~

		The conjugate of Comlex(4,5)

		which is ~Complexe(4,5)
		
		will be 4-5i
		"""
		return Complex(self.re,-self.im)
	def conjugate(self):
		return self.__invert__()
	def __xor__(self,other):#used for ^ but i will used it as power here
		"""
		used to raised a complex number to a certaion power
		
		using the symbol ^

		"""
		c=Complex(self.re,self.im)
		try:
			other.re
		except:
			for i in range(other-1):
				c*=Complex(self.re,self.im)
			return c
	def __eq__(self,other):#used for ==
		"""
		used to test if two complex number are equal
		for example
		Complex(1,2)==Complex(1,2)
		will return true"""

		try:
			if self.re==other.re and self.im==other.im:
				return True
		except :
			return False
	def __gt__(self):#used for greater than
		'used for testing if a complex number is greater than the other'
		pass
	def __pow__(self,other):#used for **
		"""
		used to raise a complex number to a certaion power
		
		using the symbol **

		"""
		c=Complex(self.re,self.im)
		try:
			other.re
		except:
			for i in range(other-1):
				c*=Complex(self.re,self.im)
			return c
	def arg(self,n=2):
		"""
			used to find the angle of a complex number



		"""
		if self.re>=0 and self.im>=0:
			return round(math.degrees(math.atan(self.im/self.re)),n)
		if self.re<0 and self.im>=0:
			return round(math.degrees(math.pi-math.atan(self.im/-self.re)),n)
		if self.re<0 and self.im<0:
			return round(math.degrees(math.atan(-self.im/-self.re)-math.pi),n)
		if self.re>=0 and self.im<0:
			return round(math.degrees(math.atan(self.im/self.re)),n)

	def mod(self):
		'used to find the modulo of a complex number'
		return round(math.sqrt((self.re**2)+(self.im**2)),9)
	@property
	def polar(self):
		'returns a complex number in polar form'
		m=self.mod()
		o=self.arg()
		return f'{m}(cos {o} + sin {o}i)'
	@property
	def exponential(self):
		'returns a complex number in the exponential form'
		m=self.mod()
		o=self.arg()
		return f'{m}e^i{o}'

class Re(object):
	"""Re(Complex(a,b)) -> a"""
	"""docstring for Re"""
	def __init__(self, re=Complex(0,0)):
		super().__init__()
		self.re = re.re
	def __add__(self,other,/):
		return Re(self.re+other)
	def __str__(self):
		return f'{self.re}'
	def __mul__(self,other,/):
		if isinstance(other,Re):
			return Re(self.re*other.re)
	def __sub__(self):
		if type(Re())==type(other):
			return Re(self.re-other.re)
	def __truediv__(self,other,/):
		"""Return self/other"""
		if type(Re())==type(other):
			return Re(self.re/other.re)
	def __pow__(self,other):
		if type(Re())==type(other):
			return Re(self.re**other*re)
		else:
			return Re(self.re**other)


class Im(object):
	"""docstring for Im"""
	def __init__(self, im=Complex(0,0)):
		super().__init__()
		self.im = im
	def __str__(self):
		return f'{self.im}i'
	def __add__(self,other,/):
		if type(Im())==type(other):
			""""""
			return Im(self.im+other.im)
	def __mul__(self,other,/):
		"""Return a real number because ai*bi=(ab)i² and i²=-1
		so ai*bi=-ab"""
		d=Im()
		if type(other)==type(d):
			return -(other.im*self.im)
	def __Im__(self,/):
		print('hello')
		Im(self.im)
	def __eq__(self,other):
		if type(Im())==type(other):
			return self.im==other.im
	def __truediv__(self):
		if type(Im())==type(other):
			return self.im/other.im
	def __sub__(self,other):
		if type(Im())==type(other):
			return self.im-other.im
		

cv=Complex(5,7)
ak=Im(5)
hf=ak-Im(5)
print("1=",hf)
print(ak,isinstance(ak,Re))
print(Re(cv))

if __name__ == '__main__':
	
	c=Complex(1,2)
	c1=c*2
	print(c)

	print("c1=",c1)

	#----------------------------------
	a=Complex(3,-2)
	b=Complex(2,1)
	print("z1=",a)
	print("z2=",b)
	print("z1/z2=",a/b)

	print(Complex(3,-2).arg())

	print(Complex(4,4)==Complex(4,4))

	print(Complex(math.sqrt(2))^7)

	f=Complex(2,3)
	print(f.mod(),f.re)
	print(f.exponential)
	print(~Complex(4,0))
