import subprocess
import numpy as np
import codecs
import pandas as pd
import os





def write__output2(data):
	file = codecs.open("output2.txt", "a", "utf-8")
	file.write(data)
	file.close()


#Extracting and parsing the header of the table
def create_header():
	head1 = []

	f = open('output.txt','r', encoding='utf-8')
	for i in range(0,4):
		line = f.readline()

	#LINE 1

	array = line.split(" ")
	array = [item for item in array if item != '']
	header1 = array[0]
	header4 = array[2]
	str1 = ' '.join(array)

	#LINE 2
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header1 += " " + array[0]
	header2 = array[1]
	header3 = array[2]
	header4 += " " + array[3]
	header7 = array[9]

	#LINE 3
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header2 += " " + array[0]
	header3 += " " + array[1]
	header4 += " " + array[2]
	header5 = array[3]
	header6 = array[4]
	header7 += " " + array[5]

	#LINE4
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header4 += " " + array[0]
	header5 += " " + array[1]
	header6 += " " + array[2]
	header7 += " " + array[3]

	#LINE 5
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header4 += " " + array[0]
	header7 += " " + array[1]

	#LINE6
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header4 += " " + array[0]
	header7 += " " + array[1]

	#LINE7
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header4 += " " + array[0]
	header7 += " " + array[1]

	#LINE8
	line = f.readline()
	array = line.split(" ")
	array = [item for item in array if item != '']
	header7 += " " + array[0]
	header7 = str.join(" ", header7.splitlines()) # Remove /n

	header = ',' + header1 + ',' + header2 + ',' + header3 + ',' + header4 + ',' + header5 + ',' + header6 + ',' + header7 + '\n'
	return header



def extract_rows_data():

	# Clear output2.txt
	file = codecs.open("output2.txt", "w", "utf-8")
	file.write('')
	file.close()

	f = open('output.txt','r', encoding='utf-8')

	k = []
	flag2 = 0
	row = 0
	while row < 48: # Skip the footer lines
		if row < 11: # Skip the first lines of the file
			string = f.readline()
			row += 1
			continue

		row += 1
		str2 = ''
		flag = 0
		arr = []
		count = 0
		i = 0
		string = f.readline()

		for char in string:
			i += 1
			if char != ' ':
				count = 0

			if char == '\n':  
				char = ''

			if i == len(string):
				str2 += char
				arr.append(str2)
			while i == len(string) and len(arr) < 8:
				arr.append('empty')

			if flag == 1 and char == ' ':
				continue
			if flag == 1 and char != ' ':
				flag = 0	
			str2 += char
			if char == ' ':
				if count == 0:
					str2 += '<SP3>'
				count += 1
			if count > 1:
				if flag2 == 0: #Si leyenda incompleta
					arr.append(str2)
				if flag2 == 1:
					arr.append(k[0]+ '<SP>' + str2)
					flag2 = 0	
				str2 = ''
				count = 0
				flag = 1
			if i > 	49 and len(arr) < 2: # Adjusting each column manually, because the table is not structured
				arr.append('empty')
			if i > 	61 and len(arr) < 3:
				arr.append('empty')
			if i > 	74 and len(arr) < 4:
				arr.append('empty')
			if i > 	85 and len(arr) < 5:
				arr.append('empty')
			if i > 	97 and len(arr) < 6:
				arr.append('empty')
			if i > 	108 and len(arr) < 7:
				arr.append('empty')


		k = []
		for l in arr:
		    j = l.replace(' ','')
		    k.append(j)


		phrase_beginning = ''
		if k[1] == k[2] == k[3] == k[4] == k[5] == k[6] == k[7] == 'empty':
			# print('funciona')
			phrase_beginning = k[0]
			flag2 = 1
			continue


		str1 = 'SEPARATOR'.join(k)

		# Replace separators ';' by ',' to be formated as a csv
		str1 = str1.replace(',','.')

		if row == 20:
			str1 = str1.replace('SEPARATOR','',1)
		if row == 27:
			file = codecs.open("temp.txt", "w", "utf-8")
			str1 = str1[9:19]
			file.write(str1)
			file.close()
			flag = 1
			k[0] = str1
			continue
			

		str1 = str1.replace('SEPARATOR',',').replace('<SP>',' ').replace('<SP3>',' ')
		str1 = str1.replace('0)','').replace('1)','').replace('2)','').replace('3)','').replace('4)','').replace('5)','').replace('6)','').replace('7)','').replace('8)','').replace('9)','')

		# Write in text file output2.txt
		write__output2(str1)
		write__output2('\n')


	f = open('output2.txt','r', encoding='utf-8')
	f = f.readlines()
	str1 = ''.join(f)
	parsed_data = str1


	# write__output2(str1)
	return parsed_data	




if __name__ == "__main__":

	#Extract text from pdf using pdftotext
	subprocess.call('/usr/local/bin/pdftotext -enc UTF-8 -layout -f 4 -l 4 oper.pdf output.txt', shell=True)


	parsed_data = extract_rows_data()

	file = codecs.open("parsed_table.csv", "w", "utf-8")
	file.close()

	file = codecs.open("parsed_table.csv", "a", "utf-8")
	header = create_header()
	file.write(header)
	file.write(parsed_data)
	file.close()

	os.remove('temp.txt')

	print('Ready, the parsed data is in parsed_table.csv')

