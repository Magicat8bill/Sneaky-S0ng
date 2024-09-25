def split_word(word):
    length = len(word)
    #floors the odd words so the second half will be longer
    mid = length // 2  
    first_half = word[:mid]
    second_half = word[mid:]
    return first_half, second_half
word = "suppercalafragilisticexpealedoshous"
first_half, second_half = split_word(word)
print("First half:", first_half)
print("Second half:", second_half)