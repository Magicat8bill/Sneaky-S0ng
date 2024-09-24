from music21 import *
s = stream.Stream()
c4 = note.Note("C4", quarterLength=1)
d4 = note.Note("D4", quarterLength=2)
e4 = note.Note('E4', quarterLength=3)
d = dynamics.Crescendo()
d.spread = 2
d.placement = 'above'
s.insert(0, note.Note('C4', quarterLength=1))
s.insert(2, note.Note('D4', quarterLength=2))
s.insert(4, note.Note('E4', quarterLength=3))
s.insert(1, d)
s.show()
# s.write('musicxml', 'my_music.xml')
