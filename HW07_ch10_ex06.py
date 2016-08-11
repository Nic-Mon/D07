# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(input_list):
	return input_list == sorted(input_list)

def main():
	list1 = [1,2,3,4,5]
	list2 = [4,5,6,1,7]
	list3 = ['all', 'back', 'cat', 'dog']
	list4 = ['zebra', 'horse', 'mule']

	print("[1,2,3,4,5] is sorted: " + str(is_sorted(list1)))
	print("[4,5,6,1,7] is sorted: " + str(is_sorted(list2)))
	print("['all', 'back', 'cat', 'dog'] is sorted: " + str(is_sorted(list3)))
	print("['zebra', 'horse', 'mule'] is sorted: " + str(is_sorted(list4)))

if __name__ == '__main__':
	main()