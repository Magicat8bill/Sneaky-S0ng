from music21 import *

pitc = []
rhythm = []

def vertion_1(lete, ryth):
    print('temp')

# Parse XML file
s = converter.parse('output.xml')
p = []
r = []

for tN in s.recurse().notes:
    # Extract the pitch name and rhythm
    pitch_name = str(tN.pitches[0])
    p.append(f'{pitch_name}')
    r.append(f'{tN.duration.quarterLength}')

# Combine pitches and rhythms into strings
p1 = ' '.join(p)
r1 = ' '.join(r)

# Remove '4' from pitch names
original_string = p1
words = original_string.split()
modified_words = [word.replace('4', '') for word in words]
modified_string = ' '.join(modified_words)

def remove_consecutive_duplicates(input_list):
    if not input_list:  # Handle empty list
        return input_list

    result = [input_list[0]]  # Start with the first element
    for i in range(1, len(input_list)):
        if input_list[i] != input_list[i - 1]:  # Check if current element is different from previous
            result.append(input_list[i])
    return result

m_w = remove_consecutive_duplicates(modified_words)

file = open('beats.txt', 'r')

# Manually define rhythm notation (this could be improved with a more scalable method)
r1 = list(file.readline())
print(r1)

# Zip modified pitch names and rhythm notation together
z = list(zip(m_w, r1))
# print(z)

# Initialize variables
work = []
num = 0

# Define a mapping from num to corresponding letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8' , '9', ' ']

# Example pitch_data (modify this based on your actual use case)
pitch_data = [('A--', '8'), ('C-', 'q'), ('G', 'w'), ('F-', '16'), ('D#', 'h'), ('D', 'h'), ('B', '16'), ('B-', 'q'), ('A', 'h'), ('F#', 'q'), ('E', 'q'), ('E', 'h'), ('E-', '16'), ('D', '8'), ('C-', 'w'), ('D', 'q'), ('C', '8'), ('G#', 'w'), ('D##', '16'), ('D-', 'h'), ('A', 'w'), ('F-', 'w'), ('A-', 'q'), ('A#', 'h'), ('C', 'w'), ('B##', '16'), ('A', '8'), ('D--', 'h'), ('E-', 'w'), ('G-', '16'), ('A#', 'q'), ('D-', '16'), ('C-', 'h'), ('B-', '16'), ('E', 'w'), ('F', '8'), ('C', '.'), ('A', '.'), ('F-', '.'), ('B', '.'), ('G#', '.'), ('E', '.'), ('C#', '.'), ('F', '.'), ('A-', '.'), ('G', '.'), ('E-', '.'), ('B-', '.'), ('G--', '.'), ('G##', '.'), ('D', '.')]

# Loop through zipped pitches and rhythms
for i in z:
    # print(i)
    if i in pitch_data:
        y = pitch_data.index(i)
        work.append(letters[y])
    # Increment num
    num += 1


# Print the final result
print(' '.join(work))