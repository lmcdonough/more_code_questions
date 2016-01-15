#! /usr/bin/python

'''These are the solutions to the coding questions provided by
Site Comply.'''



def question_2(list_of_ints):
	
	if any([num < 0 for num in list_of_ints]):
		return 'List must contain only positive integers.'

	contigous_list = [(0, list_of_ints[0])]
	starting_indexes = []

	for index, num in enumerate(list_of_ints[1:], 1):
		if len(contigous_list) == 1:
			if abs(num - contigous_list[0][1]) == 1:
				direction_val = num - contigous_list[0][1]
				contigous_list.append((index, num))
			else:
				contigous_list = [(index, num)]
		else:
			if num - contigous_list[-1][1] == direction_val:
				contigous_list.append((index, num))
			else:
				starting_indexes.append(contigous_list[0][0])
				contigous_list = [(index, num)]
	else:
		if len(contigous_list) > 1:
			starting_indexes.append(contigous_list[0][0])

	return starting_indexes or None


def question_3():
	pass




