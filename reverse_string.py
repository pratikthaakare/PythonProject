def reverse_words_in_string(s):
    words = s.split()  # Split the string into words
    reversed_words = ' '.join(reversed(words))  # Reverse the list of words and join them with a space
    return reversed_words

# Example usage
input_string = "this is string for sure"
reversed_string = reverse_words_in_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)