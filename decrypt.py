from music21 import *

pitch = []
rhythm = []

def vertion_1(sentance):
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
        if letter.upper() == "A":
            pitch.append(a)
        elif letter.upper() == "B":
            pitch.append(b)
        elif letter.upper() == "C":
            pitch.append(c)
        elif letter.upper() == "D":
            pitch.append(d)
        elif letter.upper() == "E":
            pitch.append(e)
        elif letter.upper() == "F":
            pitch.append(f)
        elif letter.upper() == "G":
            pitch.append(g)
        elif letter.upper() == "H":
            pitch.append(h)
        elif letter.upper() == "I":
            pitch.append(i)
        elif letter.upper() == "J":
            pitch.append(j)
        elif letter.upper() == "K":
            pitch.append(k)
        elif letter.upper() == "L":
            pitch.append(l)
        elif letter.upper() == "M":
            pitch.append(m)
        elif letter.upper() == "N":
            pitch.append(n)
        elif letter.upper() == "O":
            pitch.append(o)
        elif letter.upper() == "P":
            pitch.append(p)
        elif letter.upper() == "Q":
            pitch.append(q)
        elif letter.upper() == "R":
            pitch.append(r)
        elif letter.upper() == "S":
            pitch.append(s)
        elif letter.upper() == "T":
            pitch.append(t)
        elif letter.upper() == "U":
            pitch.append(u)
        elif letter.upper() == "V":
            pitch.append(v)
        elif letter.upper() == "W":
            pitch.append(w)
        elif letter.upper() == "X":
            pitch.append(x)
        elif letter.upper() == "Y":
            pitch.append(y)
        elif letter.upper() == "Z":
            pitch.append(z)
        # Numbers
        elif letter == "0":
            pitch.append(zero)
        elif letter == "1":
            pitch.append(one)
        elif letter == "2":
            pitch.append(two)
        elif letter == "3":
            pitch.append(three)
        elif letter == "4":
            pitch.append(four)
        elif letter == "5":
            pitch.append(five)
        elif letter == "6":
            pitch.append(six)
        elif letter == "7":
            pitch.append(seven)
        elif letter == "8":
            pitch.append(eight)
        elif letter == "9":
            pitch.append(nine)
        # Other
            pitch.append(space)
        elif letter == ".":
            pitch.append(period)
        elif letter == "?":
            pitch.append(questionmark)
        elif letter == "-":
            pitch.append(dash)
        elif letter == "!":
            pitch.append(exclamation)
        elif letter == ":":
            pitch.append(colon)
        elif letter == ";":
            pitch.append(semicolon)
        elif letter == ",":
            pitch.append(comma)
        elif letter == "'":
            pitch.append(apostrophy)

        return pitch

        
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

pitch = []
rhythm = []

def vertion_1(sentance):
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
            pitch.append("A")
        elif letter.upper() == b:
            pitch.append("B")
        elif letter.upper() == c:
            pitch.append("C")
        elif letter.upper() == d:
            pitch.append("D")
        elif letter.upper() == e:
            pitch.append("E")
        elif letter.upper() == f:
            pitch.append("F")
        elif letter.upper() == g:
            pitch.append("G")
        elif letter.upper() == h:
            pitch.append("H")
        elif letter.upper() == i:
            pitch.append("I")
        elif letter.upper() == j:
            pitch.append("J")
        elif letter.upper() == k:
            pitch.append("K")
        elif letter.upper() == l:
            pitch.append("L")
        elif letter.upper() == m:
            pitch.append("M")
        elif letter.upper() == n:
            pitch.append("N")
        elif letter.upper() == o:
            pitch.append("O")
        elif letter.upper() == p:
            pitch.append("P")
        elif letter.upper() == q:
            pitch.append("Q")
        elif letter.upper() == r:
            pitch.append("R")
        elif letter.upper() == s:
            pitch.append("S")
        elif letter.upper() == t:
            pitch.append("T")
        elif letter.upper() == u:
            pitch.append("U")
        elif letter.upper() == v:
            pitch.append("V")
        elif letter.upper() == w:
            pitch.append("W")
        elif letter.upper() == x:
            pitch.append("X")
        elif letter.upper() == y:
            pitch.append("Y")
        elif letter.upper() == z:
            pitch.append("Z")
        # Numbers
        elif letter == zero:
            pitch.append("0")
        elif letter == one:
            pitch.append("1")
        elif letter == two:
            pitch.append("2")
        elif letter == three:
            pitch.append("3")
        elif letter == four:
            pitch.append("4")
        elif letter == five:
            pitch.append("5")
        elif letter == six:
            pitch.append("6")
        elif letter == seven:
            pitch.append("7")
        elif letter == eight:
            pitch.append("8")
        elif letter == nine:
            pitch.append("9")
        # Other
        elif letter == space:
            pitch.append(" ")
        elif letter == period:
            pitch.append(".")
        elif letter == questionmark:
            pitch.append("?")
        elif letter == dash:
            pitch.append("-")
        elif letter == exclamation:
            pitch.append("!")
        elif letter == colon:
            pitch.append(":")
        elif letter == semicolon:
            pitch.append(";")
        elif letter == comma:
            pitch.append(",")
        elif letter == apostrophy:
            pitch.append("'")

        return pitch


        
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

        if letter.upper() == a:
            rhythm.append("A")
        elif letter.upper() == b:
            rhythm.append("B")
        elif letter.upper() == c:
            rhythm.append("C")
        elif letter.upper() == d:
            rhythm.append("D")
        elif letter.upper() == e:
            rhythm.append("E")
        elif letter.upper() == f:
            rhythm.append("F")
        elif letter.upper() == g:
            rhythm.append("G")
        elif letter.upper() == h:
            rhythm.append("H")
        elif letter.upper() == i:
            rhythm.append("I")
        elif letter.upper() == j:
            rhythm.append("J")
        elif letter.upper() == k:
            rhythm.append("K")
        elif letter.upper() == l:
            rhythm.append("L")
        elif letter.upper() == m:
            rhythm.append("M")
        elif letter.upper() == n:
            rhythm.append("N")
        elif letter.upper() == o:
            rhythm.append("O")
        elif letter.upper() == p:
            rhythm.append("P")
        elif letter.upper() == q:
            rhythm.append("Q")
        elif letter.upper() == r:
            rhythm.append("R")
        elif letter.upper() == s:
            rhythm.append("S")
        elif letter.upper() == t:
            rhythm.append("T")
        elif letter.upper() == u:
            rhythm.append("U")
        elif letter.upper() == v:
            rhythm.append("V")
        elif letter.upper() == w:
            rhythm.append("W")
        elif letter.upper() == x:
            rhythm.append("X")
        elif letter.upper() == y:
            rhythm.append("Y")
        elif letter.upper() == z:
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


        
    length = len(sentance.split(" "))
    for i in sentance:
        pitches(i)
        beat(i)
    p = ' '.join(pitch)
    # print("Pitches:", p)
    r = ' '.join(rhythm)
    # print("Rhythms:", r)
    print(p)
    return p, r

# print(vertion_1())

c = converter.parse('C:\Users\BilyeuC\Cypher\output.xml', format='musicxml')
sAlt = converter.parse(c)
sAlt.show() # show first 5 measures