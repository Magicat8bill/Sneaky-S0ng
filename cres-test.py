from music21 import *
s = stream.Stream()
c4 = note.Note("C4", quarterLength=1)
d4 = note.Note("D4", quarterLength=2)
s.append(c4)
s.append(d4)
s.show()
s.write('musicxml', 'my_music.xml')
