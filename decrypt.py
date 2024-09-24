from music21 import *

pitc = []
rhythm = []

def vertion_1(lete, ryth):
    def pitches(letter):
        # Letters
        a = "A--"
        b = "Cb"
        c = "G"
        d = "Fb"
        e = "D#"
        f = "D"
        g = "B"
        h = "Bb"
        i = "A"
        j = "F#"
        k = "E"
        l = "E"
        m = "Eb"
        n = "D"
        o = "Cb"
        p = "D"
        q = "C"
        r = "G#"
        s = "D##"
        t = "Db"
        u = "A"
        v = "Fb"
        w = "Ab"
        x = "A#"
        y = "C"
        z = "B##"
        # Numbers
        zero = "A"
        one = "D--"
        two = "Eb"
        three = "Gb" 
        four = "A#"
        five = "Db"
        six = "Cb"
        seven = "Bb" 
        eight = "E"
        nine = "F"
        # Punctuation/Spaces
        space = "C"
        comma = "A"
        period = "Fb"
        questionmark = "B"
        dash = "G#"
        exclamation = "E"
        colon = "C#"
        apostrophy = "F"
        semicolon = "Ab"
        open_pern = "G"
        close_pern = "Eb"
        slash = "Bb"
        doller_sign = "G--"
        percent = "G##"
        quotes = "D"

        # Leters
        if letter.upper() == a:
            pitc.append("A")
        elif letter.upper() == b:
            pitc.append("B")
        elif letter.upper() == c:
            pitc.append("C")
        elif letter.upper() == d:
            pitc.append("D")
        elif letter.upper() == e:
            pitc.append("E")
        elif letter.upper() == f:
            pitc.append("F")
        elif letter.upper() == g:
            pitc.append("G")
        elif letter.upper() == h:
            pitc.append("H")
        elif letter.upper() == i:
            pitc.append("I")
        elif letter.upper() == j:
            pitc.append("J")
        elif letter.upper() == k:
            pitc.append("K")
        elif letter.upper() == l:
            pitc.append("L")
        elif letter.upper() == m:
            pitc.append("M")
        elif letter.upper() == n:
            pitc.append("N")
        elif letter.upper() == o:
            pitc.append("O")
        elif letter.upper() == p:
            pitc.append("P")
        elif letter.upper() == q:
            pitc.append("Q")
        elif letter.upper() == r:
            pitc.append("R")
        elif letter.upper() == s:
            pitc.append("S")
        elif letter.upper() == t:
            pitc.append("T")
        elif letter.upper() == u:
            pitc.append("U")
        elif letter.upper() == v:
            pitc.append("V")
        elif letter.upper() == w:
            pitc.append("W")
        elif letter.upper() == x:
            pitc.append("X")
        elif letter.upper() == y:
            pitc.append("Y")
        elif letter.upper() == z:
            pitc.append("Z")
        # Numbers
        elif letter == zero:
            pitc.append("0")
        elif letter == one:
            pitc.append("1")
        elif letter == two:
            pitc.append("2")
        elif letter == three:
            pitc.append("3")
        elif letter == four:
            pitc.append("4")
        elif letter == five:
            pitc.append("5")
        elif letter == six:
            pitc.append("6")
        elif letter == seven:
            pitc.append("7")
        elif letter == eight:
            pitc.append("8")
        elif letter == nine:
            pitc.append("9")
        # Other
        elif letter == space:
            pitc.append(" ")
        elif letter == period:
            pitc.append(".")
        elif letter == questionmark:
            pitc.append("?")
        elif letter == dash:
            pitc.append("-")
        elif letter == exclamation:
            pitc.append("!")
        elif letter == colon:
            pitc.append(":")
        elif letter == semicolon:
            pitc.append(";")
        elif letter == comma:
            pitc.append(",")
        elif letter == apostrophy:
            pitc.append("'")

        return pitc


        
    def beat(letter):
        # Letters
        a = "8"
        b = "q"
        c = "w"
        d = "16"
        e = "h"
        f = "h"
        g = "16"
        h = "q"
        i = "h"
        j = "q"
        k = "q"
        l = "h"
        m = "16"
        n = "8"
        o = "w"
        p = "q"
        q = "8"
        r = "w"
        s = "16"
        t = "h"
        u = "h"
        v = "w"
        w = "q"
        x = "h"
        y = "w"
        z = "16"
        # Numbers
        zero = "8"
        one = "8"
        two = "8"
        three = "8" 
        four = "8"
        five = "8"
        six = "8"
        seven = "8" 
        eight = "8"
        nine = "8"
        # Punctuation/Spaces
        space = "."
        comma = "."
        period = "."
        questionmark = "."
        dash = "."
        exclamation = "."
        colon = "."
        apostrophy = "."
        semicolon = "."
        open_pern = "."
        close_pern = "."
        slash = "."
        doller_sign = "."
        percent = "."
        quotes = "."   

        if letter == a:
            rhythm.append("A")
        elif letter == b:
            rhythm.append("B")
        elif letter == c:
            rhythm.append("C")
        elif letter == d:
            rhythm.append("D")
        elif letter == e:
            rhythm.append("E")
        elif letter == f:
            rhythm.append("F")
        elif letter == g:
            rhythm.append("G")
        elif letter == h:
            rhythm.append("H")
        elif letter == i:
            rhythm.append("I")
        elif letter == j:
            rhythm.append("J")
        elif letter == k:
            rhythm.append("K")
        elif letter == l:
            rhythm.append("L")
        elif letter == m:
            rhythm.append("M")
        elif letter == n:
            rhythm.append("N")
        elif letter == o:
            rhythm.append("O")
        elif letter == p:
            rhythm.append("P")
        elif letter == q:
            rhythm.append("Q")
        elif letter == r:
            rhythm.append("R")
        elif letter == s:
            rhythm.append("S")
        elif letter == t:
            rhythm.append("T")
        elif letter == u:
            rhythm.append("U")
        elif letter == v:
            rhythm.append("V")
        elif letter == w:
            rhythm.append("W")
        elif letter == x:
            rhythm.append("X")
        elif letter == y:
            rhythm.append("Y")
        elif letter == z:
            rhythm.append("Z")
        # Numbers
        elif letter == zero:
            rhythm.append("0")
        elif letter == one:
            rhythm.append("1")
        elif letter == two:
            rhythm.append("2")
        elif letter == three:
            rhythm.append("3")
        elif letter == four:
            rhythm.append("4")
        elif letter == five:
            rhythm.append("5")
        elif letter == six:
            rhythm.append("6")
        elif letter == seven:
            rhythm.append("7")
        elif letter == eight:
            rhythm.append("8")
        elif letter == nine:
            rhythm.append("9")
        # Other
        elif letter == space:
            rhythm.append(" ")
        elif letter == period:
            rhythm.append(".")
        elif letter == questionmark:
            rhythm.append("?")
        elif letter == dash:
            rhythm.append("-")
        elif letter == exclamation:
            rhythm.append("!")
        elif letter == colon:
            rhythm.append(":")
        elif letter == semicolon:
            rhythm.append(";")
        elif letter == comma:
            rhythm.append(",")
        elif letter == apostrophy:
            rhythm.append("'")


        return rhythm

    length = len(lete.split(" "))
    for i in lete:
        pitches(i)
    length = len(ryth.split(" "))
    for i in ryth:
        beat(i)
    p = ' '.join(pitc)
    # print("Pitches:", p)
    r = ' '.join(rhythm)
    # print("Rhythms:", r)
    print(p)
    print(r)
    return p, r

# print(vertion_1())

s = converter.parse('output.xml')
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
# print(p1)
# print(r1)
original_string = p1
words = original_string.split()
modified_words = [word.replace('4', '') for word in words]
modified_string = ' '.join(modified_words)

# print("Modified string:", modified_string)

rhythm_map = {
    'q': 1.0,
    'h': 2.0,
    '8': 0.5,
    'r': 'rest',
    'w': 4.0,
    '16': 0.25,
    '.': 1.5
}
loop = r1.split()
lis = []
# print(loop)
for i in r1:
    if i == '1':
        lis.append('q')
    if i == '2':
        lis.append('h')
    if i == '0.5':
        lis.append('8')
    if i == '4':
        lis.append('w')
    if i == '0.25':
        lis.append('16')
    if i == '1.5':
        lis.append('.')
r1 = ' '.join(lis)
r1 = 'h h . q w w q 16'
l = r1.split()
print(l)
vertion_1(modified_string, r1)