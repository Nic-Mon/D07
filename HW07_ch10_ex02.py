# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
def capitalize_nested(nested_list):
	new_list = []
	for item in nested_list:
		if isinstance(item, list):
			new_list.append(capitalize_nested(item))
		else:
			new_list.append(item.upper())
	return new_list

def main():
	list1 = ['apple', ['bear'], 'cat']
	list2 = [['nicolas','mon'], ['python', 'bootcamp'], ['loads','of','fun!']]
	list3 = [['super', ['duper', ['nested']]], ['list']]

	print(capitalize_nested(list1))
	print(capitalize_nested(list2))
	print(capitalize_nested(list3))

if __name__ == '__main__':
	main()