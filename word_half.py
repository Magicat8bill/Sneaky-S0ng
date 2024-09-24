"""my_list = ["r", "a", "b", "b", "i", "t"]
chunk_size = 2
split_list = [[] for _ in range(chunck size)]
for index, value in enumerate(my_list):
    sublist_index = index % chunk_size
    split_list[sublist_index].append(value)
print (split_list)"""

def split_word(word):
    length = len(word)
    #floors the odd words so the second half will be longer
    mid = length // 2  
    first_half = word[:mid]
    second_half = word[mid:]
    return first_half, second_half

word = "the"
first_half, second_half = split_word(word)
print("First half:", first_half)
print("Second half:", second_half)