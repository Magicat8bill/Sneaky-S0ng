pitch = []
rhythm = []

def version_2(sentance):
    '''
    Translates a sentence to music notation
    >>> p, r = ver2.version_2('input')
    '''
    def pitches(letter):
        # Letters
        a = "A-- C Gb"
        b = "Cb G A Fb G##"
        c = "G B C# A"
        d = "Fb A# Cb"
        e = "G## F#"
        f = "D E F A"
        g = "Bb A# C"
        h = "Bb Cb C A"
        i = "Db C# A# Fb A#"
        j = "F# D B#"
        k = "Cb G--"
        l = "E## F# A B--"
        m = "Fb E## G#"
        n = "A-- Fb G##"
        o = "Cb Db D#"
        p = "D# G# E## "
        q = "Ab A A# Gb G G#"
        r = "G#  F# Eb"
        s = "D## D# D Db D--"
        t = "Db E A# Gb F Gb"
        u = "C## B B##"
        v = "Fb G A F## E Db"
        w = "Ab E F Db"
        x = "A# Db G## E#"
        y = "C# Bb Eb A--"
        z = "B## D E F A##"
        ä = "F# Bb D-- F##"
        ö = "A C# B-- Fb D##"
        ü = "A Bb E-- E##"
        ß = "A B G E# G--"
        # Numbers
        zero = "Db D## Fb A--"
        one = "Fb G## A D B"
        two = "C Db B-- "
        three = "B# C F A##" 
        four = "D F Gb C D#"
        five = "A B C#  G-- A--"
        six = "B A G E"
        seven = "A Fb Db E G## " 
        eight = "E Fb G-- A##"
        nine = "F-- E# A D## B"
        # Punctuation/Spaces
        space = "A F G-- G E Fb F-- D#"
        comma = "A D## Fb F--"
        period = "Fb C E Db A##"
        questionmark = "B D F## Eb"
        dash = "G# Db F-- A B"
        exclamation = "E F A-- B# Gb"
        colon = "C# C Db F# G#"
        apostrophy = "F D F G-- Ab E#"
        semicolon = "Ab Fb C## E-- G"
        open_pern = "G F D A## A B"
        closed_pern = "Eb E B F A G##"
        slash = "Bb A Bb D E##"
        percent = "G## G E D F##"
        quotes = "D G E-- F# B--"
        tilda = "E## F-- G A# Bb"
        back_tick = "D F-- G# A# E"
        at = "D B E## Ab"
        pound = "A D-- Gb E#"
        dollar = "G-- Bb Db A# E"
        carrot = "Db Gb E# A--"
        star = "E Fb G A--"
        underscore = "D Bb E Fb"
        open_curley_bracket = "D# A B-- F Gb"
        closed_curley_bracket = "E F-- D## Bb A"
        open_bracket = "E Gb A-- D#"
        closed_bracket = "A G Eb F## E#"
        less_than = "A B F-- Bb"
        greater_than = "E G# B-- A E C"
        vert_bar = "C E F-- C#"
        equals = "E F-- G# C##"
        plus = "A F E-- C##"
        and_symbol = "A# Db E F G--"


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
        elif letter == "ä":
            pitch.append(ä)
        elif letter == "ö":
            pitch.append(ö)
        elif letter == "ü ":
            pitch.append(ü)
        elif letter == "ß":
            pitch.append(ß)
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
        elif letter == " ":
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
        elif letter == '"':
            pitch.append(quotes)
        elif letter == "(":
            pitch.append(open_pern)
        elif letter == ")":
            pitch.append(closed_pern)
        elif letter == "/":
            pitch.append(slash)
        elif letter == "$":
            pitch.append(dollar)
        elif letter == "%":
            pitch.append(percent)
        elif letter == "~":
            pitch.append(tilda)
        elif letter == "`":
            pitch.append(back_tick)
        elif letter == "@":
            pitch.append(at)
        elif letter == "#":
            pitch.append(pound)
        elif letter == "^":
            pitch.append(carrot)
        elif letter == "&":
            pitch.append(and_symbol)
        elif letter == "*":
            pitch.append(star)
        elif letter == "_":
            pitch.append(underscore)
        elif letter == "{":
            pitch.append(open_curley_bracket)
        elif letter == "}":
            pitch.append(closed_curley_bracket)
        elif letter == "[":
            pitch.append(open_bracket)
        elif letter == "]":
            pitch.append(closed_bracket)
        elif letter == "<":
            pitch.append(less_than)
        elif letter == ">":
            pitch.append(greater_than)
        elif letter == "|":
            pitch.append(vert_bar)
        elif letter == "=":
            pitch.append(equals)
        elif letter == "+":
            pitch.append(plus)

        return pitch

        
    def beat(letter):
        # Letters
        a = "8 16 16"
        b = "w q 16 8 16"
        c = "h q 16 16 8 16"
        d = "8 16 w"
        e = "16 16"
        f = "16 16 h 8 16"
        g = "16 16 16 16 q h"
        h = "h q 16 8"
        i = "h 16 16 w q"
        j = "h 16 q"
        k = "w w"
        l = "16 8 q 8"
        m = "8 16 q"
        n = "h h q"
        o = "8 16 h"
        p = "w q 16"
        q = "16 8 q q 16 8"
        r = "h w 8"
        s = "16 8 16 h q q"
        t = "w h q q 16 8"
        u = "h 16 16"
        v = "w q q h 16 8"
        w = "q q h q"
        x = "w q  h 16"
        y = "16 8 16 q"
        z = "h w 8 16 q"
        ä = "w h 16 h"
        ö = "q w h 16 16"
        ü = "8 8 16 h q"
        ß = "q w h 16"

        # Numbers
        zero = "16 8 q w ."
        one = "h q 16 16 ."
        two = "w w ."
        three = "w 8 16 ." 
        four = "h q 8 w ."
        five = "h w 16 q ."
        six = "w 16 16 ."
        seven = "16 8 q h ." 
        eight = "h w 8 ."
        nine = "q w h 16 ."
        # Punctuation/Spaces
        space = "q w 16 8 w h w ."
        comma = "q h 16 ."
        period = "8 16 8 8 ."
        questionmark = "w h q 8 ."
        dash = "h q w 16 ."
        exclamation = "16 8 q q ."
        colon = "16 16 8 q ."
        apostrophy = "w q 16 16 8 . "
        semicolon = "q h 8 w ."
        open_pern = "16 w q 16 h ."
        closed_pern = "h h 8 8 16 ."
        slash = "w q h h ."
        dollar = "q w h h ."
        percent = "q h h 8 ."
        quotes = "8 w h 8 ."
        tilda = "w w w w ."
        back_tick = "q h h q ."
        at = "w h q ."  
        pound = "16 q 8 ." 
        carrot = "8 h 8 ."
        and_symbol = "q q h 16 ."
        star = "q 16 h ."
        underscore = "w h h ."
        open_curley_bracket = "q w h 8 ."
        closed_curley_bracket = "q q h h ."
        open_bracket = "8 16 h ."
        closed_bracket = "q h 16 8 ."
        less_than = "w w q ."
        greater_than = "q w h 16 16 ."
        vert_bar = "q q 8 ."
        equals = "q 16 8 ."
        plus = " h h h ."


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
        elif letter == "ä":
            rhythm.append(ä)
        elif letter == "ö":
            rhythm.append(ö)
        elif letter == "ü ":
            rhythm.append(ü)
        elif letter == "ß":
            rhythm.append(ß)    
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
        elif letter == "(":
            rhythm.append(open_pern)
        elif letter == ")":
            rhythm.append(closed_pern)
        elif letter == "/":
            rhythm.append(slash)
        elif letter == "$":
            rhythm.append(dollar)
        elif letter == "%":
            rhythm.append(percent)
        elif letter == '"':
            rhythm.append(quotes)
        elif letter == "~":
            rhythm.append(tilda)
        elif letter == "`":
            rhythm.append(back_tick)
        elif letter == "@":
            rhythm.append(at)
        elif letter == "#":
            rhythm.append(pound)
        elif letter == "^":
            rhythm.append(carrot)
        elif letter == "&":
            rhythm.append(and_symbol)
        elif letter == "*":
            rhythm.append(star)
        elif letter == "_":
            rhythm.append(underscore)
        elif letter == "{":
            rhythm.append(open_curley_bracket)
        elif letter == "}":
            rhythm.append(closed_curley_bracket)
        elif letter == "[":
            rhythm.append(open_bracket)
        elif letter == "]":
            rhythm.append(closed_bracket)
        elif letter == "<":
            rhythm.append(less_than)
        elif letter == ">":
            rhythm.append(greater_than)
        elif letter == "|":
            rhythm.append(vert_bar)
        elif letter == "=":
            rhythm.append(equals)
        elif letter == "+":
            rhythm.append(plus)

        return rhythm

    def modify_list_of_strings(input_list):
        modified_list = []
        
        # Iterate through each string in the list
        for string in input_list:
            notes = string.split()  # Split the string into individual elements
            last_note = notes[-1]   # Get the last element
            
            # Append the last note two more times
            notes.append(last_note)
            notes.append(last_note)
            
            # Join the modified list back into a string
            modified_string = ' '.join(notes)
            modified_list.append(modified_string)
        
        return modified_list


        
    length = len(sentance.split(" "))
    for i in sentance:
        pitches(i)
        beat(i)
    result = modify_list_of_strings(pitch)
    p = ' '.join(result)
    # print("Pitches:", p)
    result = modify_list_of_strings(rhythm)
    r = ' '.join(result)
    print(p)
    print(r)
    return p, r


# vertion_2('it works')






