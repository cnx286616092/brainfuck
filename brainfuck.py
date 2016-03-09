
class brainfuck(object):

	def __init__(self):
		self.syb_list = list(r'><+-.,[]')
		self.length = 200
		self.dptr = 0
		self.run_list = [0] * self.length
	
	def check_vail(self,string):
		for i in string:
			if self.syb_list.count(i) == 0:
				return False
		return True
		
	char_index = 0
	char_str = ''
	def getchar(self):
		if self.char_index == 0:
			self.char_str = raw_input()
		
		if len(self.char_str) == 0:
			return 10
			
		t = self.char_str[self.char_index]
		self.char_index += 1	
			
		if self.char_index == len(self.char_str):
			self.char_index = 0
		
		return ord(t)
	
	def getjump(self,string):
		dic = {}
		stack = []
		i = 0
		for i in xrange(len(string)):
			if string[i] is '[':
				stack.append(i)
			
			if string[i] is ']':
				t = stack.pop()
				dic[i] = t
				dic[t] = i
			i += 1
		return dic
		
	def run_line(self,string):
		fptr = 0
		dic  = self.getjump(string)
		while fptr < len(string):
			if string[fptr] == '>':
				self.dptr += 1
				fptr += 1
				if self.dptr >= self.length:
					run_list.extend([0]*100)
					length +=100
					
			elif string[fptr] == '<':
				self.dptr -= 1
				fptr += 1
				if self.dptr < 0:
					print 'index error'
			
			elif string[fptr] == '+':
				self.run_list[self.dptr] += 1
				fptr += 1
			elif string[fptr] == '-':
				self.run_list[self.dptr] -= 1
				fptr += 1
			elif string[fptr] == '.':
				print chr(self.run_list[self.dptr]),
				fptr += 1
			elif string[fptr] == ',':
				t = self.getchar()
				self.run_list[self.dptr] = t
				fptr += 1
			elif string[fptr] == '[': 
				if self.run_list[self.dptr] == 0:
					fptr = dic[fptr]
				else:
					fptr += 1
			
			elif string[fptr] == ']':
				if self.run_list[self.dptr] != 0:
					fptr = dic[fptr]
				else:
					fptr += 1
			else:
				print 'error symble'

	def run(self):
		while True:
			line = raw_input(">>>").strip()
			if not self.check_vail(line):
				print 'error symble'
				continue
			self.run_line(line)
			
if __name__ == '__main__':
	a = brainfuck()
	a.run()
	

	
	
	
	