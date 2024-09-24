from music21 import *
# s = stream.Stream()
# c4 = note.Note("C4", quarterLength=1)
# d4 = note.Note("D4", quarterLength=2)

# s.append(c4)
# s.append(d4)
# s.show()
# s.write('musicxml', 'my_music.xml')



n1 = note.Note('C4')
n2 = note.Note('D4')
n3 = note.Note('E4')
n4 = note.Note('F4')
n5 = note.Note('G4')
n6 = note.Note('A4')
slur1 = spanner.Slur([n2, n3])
slur2 = spanner.Slur()
slur2.addSpannedElements([n5, n6])
part1 = stream.Part()
part1.append([n1, n2, n3, n4, n5, n6])
part1.insert(0, slur1)
part1.insert(0, slur2)