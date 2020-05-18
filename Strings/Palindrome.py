#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.


def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string = input_string.lower()
        # Traverse through each letter of the input string
	for x in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
                	if x != " ":
			new_string = new_string + x
			reverse_string = x + reverse_string
                        	# Compare the strings
	if new_string == reverse_string:
		return True
	return False
    
