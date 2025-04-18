pitch = []
rhythm = []

def version_1(sentance):
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
        one = "h"
        two = "w"
        three = "16" 
        four = "q"
        five = "16"
        six = "h"
        seven = "16" 
        eight = "w"
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

        if letter.upper() == "A":
            rhythm.append(a)
        elif letter.upper() == "B":
            rhythm.append(b)
        elif letter.upper() == "C":
            rhythm.append(c)
        elif letter.upper() == "D":
            rhythm.append(d)
        elif letter.upper() == "E":
            rhythm.append(e)
        elif letter.upper() == "F":
            rhythm.append(f)
        elif letter.upper() == "G":
            rhythm.append(g)
        elif letter.upper() == "H":
            rhythm.append(h)
        elif letter.upper() == "I":
            rhythm.append(i)
        elif letter.upper() == "J":
            rhythm.append(j)
        elif letter.upper() == "K":
            rhythm.append(k)
        elif letter.upper() == "L":
            rhythm.append(l)
        elif letter.upper() == "M":
            rhythm.append(m)
        elif letter.upper() == "N":
            rhythm.append(n)
        elif letter.upper() == "O":
            rhythm.append(o)
        elif letter.upper() == "P":
            rhythm.append(p)
        elif letter.upper() == "Q":
            rhythm.append(q)
        elif letter.upper() == "R":
            rhythm.append(r)
        elif letter.upper() == "S":
            rhythm.append(s)
        elif letter.upper() == "T":
            rhythm.append(t)
        elif letter.upper() == "U":
            rhythm.append(u)
        elif letter.upper() == "V":
            rhythm.append(v)
        elif letter.upper() == "W":
            rhythm.append(w)
        elif letter.upper() == "X":
            rhythm.append(x)
        elif letter.upper() == "Y":
            rhythm.append(y)
        elif letter.upper() == "Z":
            rhythm.append(z)
        # Numbers
        elif letter == "0":
            rhythm.append(zero)
        elif letter == "1":
            rhythm.append(one)
        elif letter == "2":
            rhythm.append(two)
        elif letter == "3":
            rhythm.append(three)
        elif letter == "4":
            rhythm.append(four)
        elif letter == "5":
            rhythm.append(five)
        elif letter == "6":
            rhythm.append(six)
        elif letter == "7":
            rhythm.append(seven)
        elif letter == "8":
            rhythm.append(eight)
        elif letter == "9":
            rhythm.append(nine)
        # Other
        elif letter == " ":
            rhythm.append(space)
        elif letter == ".":
            rhythm.append(period)
        elif letter == "?":
            rhythm.append(questionmark)
        elif letter == "-":
            rhythm.append(dash)
        elif letter == "!":
            rhythm.append(exclamation)
        elif letter == ":":
            rhythm.append(colon)
        elif letter == ";":
            rhythm.append(semicolon)
        elif letter == ",":
            rhythm.append(comma)
        elif letter == "'":
            rhythm.append(apostrophy)

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
