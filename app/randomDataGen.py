import os
import csv
import datetime
import random
import string

from logging import getLogger 

LOG = getLogger(__name__)

TEST_DATA_DIR = "./test-data"

class TestDataGenerator:

	'Class containing all functions relevant to generating random data for all three example cases.'

	def __init__(self):
		'Constructor function for the class. When the class is called, the init method runs to call the relevant functions'

		os.makedirs(TEST_DATA_DIR, exist_ok=True)
		self.makeTestData()
	 
	def makeTestData(self):
		self.exampleCase1()
		self.exampleCase2()
		self.exampleCase3()

	def exampleCase1(self):
	
		data = [['data1', 'data2', 'data3']]
		for _ in range(10000000):
			data.append([self.randomText() for x in range(3)])
		
		self.writeCSV(1, data)


	def exampleCase2(self):
		 
		data = [['date', 'data']]
		date_1 = datetime.datetime(2015, 8, 1)
		date_2 = datetime.datetime(2017, 8, 1)

		for _ in range(1800000):
			data.append([date_1, self.randomText()])
			
		for _ in range(1800000, 2000000):
			data.append([date_2, self.randomText()])

		self.writeCSV(2, data)


	def exampleCase3(self):
		
		data = [['name', 'phone']]

		for _ in range(10000):
			data.append([self.randomText(), self.randomPhoneNumber()])
		
		self.writeCSV(3, data)


	@staticmethod
	def randomPhoneNumber(numberLen = 10):
		"""
		Generate a random phone number with specified number of digits. 
		:param numberLen: Number of digits in the number, the default value being 10
		:return: random integer
		:return_type: int
		"""
		
		range_start = 10**(numberLen-1)
		range_end = (10**numberLen)-1
		return random.randint(range_start, range_end)
	

	@staticmethod
	def randomText(stringLen = 10):
		"""
		Generate a random  string with specified string length. 
		:param stringLen: number of chars in the string, the defult value being 10
		:return: random string
		:return_type: string
		"""

		chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
		random_str_list = [random.choice(chars) for _ in range(stringLen)]
		return "".join(random_str_list)

	@staticmethod
	def writeCSV(exampleCase, data):
		"""
		write csv data to the file
		
		:param exampleCase: being 1, 2 or 3
		:param data: data to be written
		"""
		x = random.choice(string.ascii_letters)
		name = "example{}_{}.csv".format(str(exampleCase), x)
	
		try:
			with open(os.path.join(TEST_DATA_DIR, name), 'w+') as CSVFile:
				writer = csv.writer(CSVFile)
				writer.writerows(data)

		except Exception as e:
			LOG.error(e)  


if __name__ == "__main__":
	TestDataGenerator()
