# reverse a sting

def test_reverse_string(string):
    print(string[::-1])
    

test_reverse_string("Hello")


# reverse a sentence (keep word intact)
sentence = "Hello my name is John"
sentence_list = sentence.split() # split the sentence into a list of words using the split() method
print(sentence_list[::-1]) # reverse the list of words using the slicing operator [::-1]
print(" ".join(sentence_list[::-1])) # join the reversed list of words into a sentence using the join() method: 

"""
The "" (empty string) before .join() is the separator used between elements.

If "" (empty string) is used, elements are joined without any space.
If " " (space) is used, elements are joined with spaces.
"""
# reverse each word in a sentence (keep order)
sentence = "Hello my name is John"
sentence_list = sentence.split()
reverse_sentence = []
for word in sentence_list:
    word = word[::-1]
    reverse_sentence.append(word)
reverse_sentence = " ".join(reverse_sentence)
print(reverse_sentence)

print(" ".join(word[::-1]for word in sentence.split())) # using list comprehension


# find the second largest number in a list
numbers = [1,2,3,4,5,6,7,8,9,10]
new_numbers = sorted(numbers, reverse=True)
print(new_numbers[1])

dup_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]

new_dup_numbers = set(dup_numbers)  # Remove duplicates

sorted_numbers = sorted(new_dup_numbers, reverse=True)  # Sort in descending order

sec_largest = sorted_numbers[1]  # Get the second largest element
print(sec_largest)
