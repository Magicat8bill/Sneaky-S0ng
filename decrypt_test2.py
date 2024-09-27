from music21 import *

pitc = []
rhythm = []

def vertion_1(lete, ryth):
    print('temp')

# print(vertion_1())

s = converter.parse('output.xml')
# s.show('text')
p = []
r = []

for tN in s.recurse().notes:
    # Extract the pitch name (e.g., 'A4' instead of <music21.pitch.Pitch A4>)
    pitch_name = str(tN.pitches[0])
    p.append(f"{pitch_name}")
    r.append(f"{tN.duration.quarterLength}")
    # print(f"{pitch_name}, {tN.duration.quarterLength}")

p1 = " ".join(p)
r1 = " ".join(r)

original_string = p1
words = original_string.split()
modified_words = [word.replace('4', '') for word in words]
modified_string = ' '.join(modified_words)

# lis = []
# for i in r1:
#     if i == '1':
#         lis.append('q')
#     if i == '2':
#         lis.append('h')
#     if i == '0.5':
#         lis.append('8')
#     if i == '4':
#         lis.append('w')
#     if i == '0.25':
#         lis.append('16')
#     if i == '1.5':
#         lis.append('.')
# r1 = ' '.join(lis)

# print(modified_string)
# print(r1)
r1 = (['h', 'h', '.', 'q', 'w', 'w', 'q', '16'])

z = list(zip(modified_string, r1))
print(z)
# y = str(z)
# print(y)
# x = ", ".join(y)
# print(x)
# print(type(x))

pitch_data = [
    ("A--", 8), ("Cb", "q"), ("G", "w"), ("Fb", 16), ("D#", "h"), ("D", "h"), ("B", 16),
    ("Bb", "q"), ("A", "h"), ("F#", "q"), ("E", "q"), ("Eb", "h"), ("D", 16), ("Cb", 8),
    ("D", "w"), ("C", "q"), ("G#", 8), ("D##", "w"), ("Db", 16), ("A", "h"), ("Fb", "w"),
    ("Ab", "w"), ("A#", "q"), ("C", "h"), ("B##", "w"), ("A", "w"), ("D--", 16),
    ("Eb", 16), ("Gb", "h"), ("A#", 16), ("Db", 16), ("Cb", "w"), ("Bb", 8), ("E", "."),
    ("F", "."), ("C", "."), ("A", "."), ("Fb", "."), ("B", "."), ("G#", "."), ("E", "."),
    ("C#", "."), ("F", "."), ("Ab", "."), ("G", "."), ("Eb", "."), ("Bb", "."), ("G--", "."),
    ("G##", ".")
]

# Create separate lists for pitches and durations


# Print the lists
# print(pitch_data[1])


work = []
num = 0
for i in z:
    if i == pitch_data[num] and num == 0:
        work.append('a')
    elif i == pitch_data[num] and num == 1:
        work.append('b')
    elif i == pitch_data[num] and num == 2:
        work.append('c')
    num += 1