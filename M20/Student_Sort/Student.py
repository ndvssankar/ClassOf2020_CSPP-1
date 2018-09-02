class Student(object):
	def __init__(self, Id, name, mm, mp, mc):
		self.Id = Id
		self.name = name
		self.mm = mm
		self.mp = mp
		self.mc = mc
	def get_name(self):
		return self.name
	def get_mm(self):
		return self.mm
	def get_mp(self):
		return self.mp
	def get_mc(self):
		return self.mc
	def get_Id(self):
		return self.Id

	def set_Id(self, Id):
		self.Id = Id
	def set_name(self, name):
		self.name = name
	def set_mp(self, mp):
		self.mp = mp
	def set_mm(self, mm):
		self.mm = mm
	def set_mc(self, mc):
		self.mc = mc

	def __str__(self):
		return str(self.Id) + ", " + self.name + ", " + str(self.mm) + ", " + str(self.mp) + ", " + str(self.mc)

import sys

def main():
	students = []
	for line in sys.stdin:
		print(line)
		values = line.split(",")
		students.append(Student(int(values[0]), values[1], int(values[2]), int(values[3]), int(values[4])))

	students.sort(key=lambda x: (x.mm, x.mp, x.mc), reverse = True)

	for student in students:
		print(student)


if __name__ == "__main__":
	main()