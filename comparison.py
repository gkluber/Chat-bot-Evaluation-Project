import math
import random
import sys
import re
import numpy as np
import tkinter
import sys, os, errno
from tkinter import ttk
import time
from datetime import datetime

def load_questions():
	return getLines("question_sample.txt")

def load_chatbot_responses():
	return getLines("reformatted_chatbot_answers.txt")
	
def load_ground_responses():
	return getLines("reformatted_ground_answers.txt")
	
def getLines(path):
	with open(path) as f:
		return [x for x in list(f)]

'''
Boilerplate template borrowed from
http://www.datadependence.com/2016/04/how-to-build-gui-in-python-3/
'''
class Viewer(ttk.Frame):
	def __init__(self, parent, *args, **kwargs):
		ttk.Frame.__init__(self, parent, *args, **kwargs)
		self.root = parent
		self.init_gui()
 
	def on_quit(self):
		"""Exits program."""
		quit()
 
	def calculate(self):
		"""Calculates the sum of the two inputted numbers."""
		num1 = int(self.num1_entry.get())
		num2 = int(self.num2_entry.get())
		num3 = num1 + num2
		self.answer_label['text'] = num3
 
	def init_gui(self):
		"""Builds GUI."""
		self.root.title('Number Adder')
		self.root.option_add('*tearOff', 'FALSE')
 
		self.grid(column=0, row=0, sticky='nsew')
 
		self.menubar = tkinter.Menu(self.root)
 
		self.menu_file = tkinter.Menu(self.menubar)
		self.menu_file.add_command(label='Exit', command=self.on_quit)
 
		self.menu_edit = tkinter.Menu(self.menubar)
 
		self.menubar.add_cascade(menu=self.menu_file, label='File')
		self.menubar.add_cascade(menu=self.menu_edit, label='Edit')
 
		self.root.config(menu=self.menubar)
 
		self.num1_entry = ttk.Entry(self, width=5)
		self.num1_entry.grid(column=1, row = 2)
 
		self.num2_entry = ttk.Entry(self, width=5)
		self.num2_entry.grid(column=3, row=2)
 
		self.calc_button = ttk.Button(self, text='Calculate',
				command=self.calculate)
		self.calc_button.grid(column=0, row=3, columnspan=4)
 
		self.answer_frame = ttk.LabelFrame(self, text='Answer',
				height=100)
		self.answer_frame.grid(column=0, row=4, columnspan=4, sticky='nesw')
 
		self.answer_label = ttk.Label(self.answer_frame, text='')
		self.answer_label.grid(column=0, row=0)
 
		# Labels that remain constant throughout execution.
		ttk.Label(self, text='Number Adder').grid(column=0, row=0,
				columnspan=4)
		ttk.Label(self, text='Number one').grid(column=0, row=2,
				sticky='w')
		ttk.Label(self, text='Number two').grid(column=2, row=2,
				sticky='w')
 
		ttk.Separator(self, orient='horizontal').grid(column=0,
				row=1, columnspan=4, sticky='ew')
 
		for child in self.winfo_children():
			child.grid_configure(padx=5, pady=5)

			
if __name__ == "__main__":
	args = sys.argv
	questions = load_questions()
	true_responses = load_ground_responses()
	false_responses = load_chatbot_responses()
	num_questions = len(questions)
	#generates a random order to present the questions in
	random_indices = np.random.permutation(range(num_questions))
	temp_true = [None]*num_questions
	temp_false = [None]*num_questions
	temp_questions = [None]*num_questions
	
	#maps all of the original indices to new random indices
	for (question, true, false, destination) in zip(questions, true_responses, false_responses, random_indices):
		temp_questions[destination] = question
		temp_true[destination] = true
		temp_false[destination] = false
	
	true_responses = temp_true
	false_responses = temp_false
	questions = temp_questions
	
	#collect data
	results = []; #array of scores tupled with the question
	
	#clear command prompt
	print("\n\n\n\n\n\n\n\n\n")
	for (question, true, false) in zip(questions, true_responses, false_responses):
		while True:
			#random number between 0 and 1 (0 inclusive and 1 exclusive)
			rand = random.random()
			#randomly rearranges the answers
			if rand > 0.5:
				answer1 = true
				answer2 = false
			else:
				answer1 = false
				answer2 = true
			
			answers = [answer1,answer2]
			
			print(question+"\n")
			print("Answer 1: "+answer1+"\n")
			print("Answer 2: "+answer2+"\n")
			
			result = input("Choice: ")
			'''
			Key:
			0 -> The judges cannot decide on one answer.
			1+ -> All four judges agree on answer 1
			1 -> The judges agree on answer 1, but there is some disagreement
			2+ -> All four judges agree on answer 2
			2 -> The judges agree on answer 2, but there is some disagreement
			'''
			if result=='0':
				results.append((0,question))
			elif result=='1+' or result == '2+':
				results.append((2 if answers[int(result[:1]) - 1] == true else -2,question))
			elif result=='1' or result=='2':
				results.append((1 if answers[int(result) - 1] == true else -1, question))
			else:
				continue #restarts the loop because the input wasn't recognized
			
			break
			
	#write the results into a file
	cur_time = time.time()
	folder_name = datetime.fromtimestamp(cur_time).strftime('%m.%d.%Y %H.%M.%S')
	
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
	
	with open(folder_name+"\\"+"results.txt",'wb') as output:
		for (score, question) in results:
			output.write((question[:-1]+" "+str(score)+"\n").encode('utf-8'))
