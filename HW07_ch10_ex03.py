# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def cumulative_sum(list):
	total = 0
	new_list = []
	for item in list:
		total += item
		new_list.append(total)
	return new_list

def main():
	list1 = [1,2,3]
	list2 = [2,4,6,8]
	list3 = [1,3,5,7,9]

	print("Cumulative sum of [1, 2, 3]: " + str(cumulative_sum(list1)))
	print("Cumulative sum of [2, 4, 6, 8]: " + str(cumulative_sum(list2)))
	print("Cumulative sum of [1, 3, 5, 7, 9]: " + str(cumulative_sum(list3)))


if __name__ == '__main__':
	main()