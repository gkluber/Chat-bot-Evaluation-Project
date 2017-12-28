import math
import random
import sys
import re
import numpy as np
'''
Usage: roll.py [sample_dialogue | sample_judges]
'''


def draw_without_replacement(names, number):
	result = []
	while number > 0:
		rand_index = random_draw(names)
		result.append(names[rand_index])
		#removes the name so that it is not drawn again
		del names[rand_index]
		number -= 1
	return result

#randomly returns the index of the randomly selected element. the truncate function is used to ensure that there is no bias towards neither 
#the head of the array nor the end of the array
def random_draw(array):
	#random number between zero and one
	rand = random.random()
	#randomly samples a single index from the array of names
	rand_index = math.trunc(rand*len(array))
	return rand_index
	
def sample_from(array):
	index = random_draw(array)
	return array[index]
	
def statified_random_sample(arr, per_stratum):
	#randomly sample <per_stratum> responses from each array
	result = []
	for x in range(len(arr)):
		
		samples = draw_without_replacement(arr[x], per_stratum)
		for sample in samples:
			result.append(sample)
	return result

if __name__ == "__main__":
	args = sys.argv
	with open("class.txt","rb") as f:
		names = f.readlines()
	names = [x.strip() for x in names] 
	#results in the array names containing each name from the class assigned to a unique index
	print(names)
	
	if len(args) == 2 and args[1] == "sample_ground":
		print(draw_without_replacement(names,5))
	
	if len(args) == 2 and args[1] == "sample_judges":
		print(draw_without_replacement(names,4))
	
	if len(args) == 2 and args[1] == "sample_dialogue":
		#the number of dialogues in the Ubuntu corpus is 350
		#this code randomly samples from an array containing the numbers 1-350
		indices = [x for x in range(1,350)]
		print(sample_from(indices))
	
	if len(args) == 2 and args[1] == "sample_questions":
		paths = ["deep.txt", "get_to_know.txt", "good_questions.txt", "philosophical.txt", "starters.txt"]
		questions = []
		for path in paths:
			with open(path, 'rb') as f:
				lines = f.readlines()[::2]
				print(lines)
				#removes questions that are imcompatable with the chatbot's architecture and network parameters
				x = len(lines) - 1
				while x > -1:
					line = lines[x].decode('utf-8')
					if len(line)==0 or len(re.split('\W+', line)) > 10:
						del lines[x]
					x -= 1
					
				questions.append(lines)
		
		print(questions)
		sample = statified_random_sample(questions, 8)
		
		with open("question_sample.txt",'wb') as out:
			for question in sample:
				out.write(question+"\n".encode('utf-8'))
		
	if len(args) == 2 and args[1] == "shuffle_ground":
		
		with open("ground_truth.txt", 'rb') as f:
			names = np.array(list(filter(lambda x: len(x.decode('utf-8')) != 0, f.readlines())))
			np.random.shuffle(names)
			print(names)
		