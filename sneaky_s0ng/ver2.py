pitch = []
rhythm = []

def version_2(sentance):
    '''
    Translates a sentence to music notation
    >>> p, r = ver2.version_2('input')
    '''
    def pitches(letter):
        # Letters
        letters = {"a": "A-- C Gb",
        "b": "Cb G A Fb G##",
        "c": "G B C# A",
        "d": "Fb A# Cb",
        "e": "G## F#",
        "f": "D E F A",
        "g": "Bb A# C",
        "h": "Bb Cb C A",
        "i": "Db C# A# Fb A#",
        "j": "F# D B#",
        "k": "Cb G--",
        "l": "E## F# A B--",
        "m": "Fb E## G#",
        "n": "A-- Fb G##",
        "o": "Cb Db D#",
        "p": "D# G# E## ",
        "q": "Ab A A# Gb G G#",
        "r": "G#  F# Eb",
        "s": "D## D# D Db D--",
        "t": "Db E A# Gb F Gb",
        "u": "C## B B##",
        "v": "Fb G A F## E Db",
        "w": "Ab E F Db",
        "x": "A# Db G## E#",
        "y": "C# Bb Eb A--",
        "z": "B## D E F A##",
        "ä": "F# Bb D-- F##",
        "ö": "A C# B-- Fb D##",
        "ü": "A Bb E-- E##",
        "ß": "A B G E# G--",
        # Numbers
        "0": "Db D## Fb A--",
        "1": "Fb G## A D B",
        "2": "C Db B-- ",
        "3": "B# C F A##" ,
        "4": "D F Gb C D#",
        "5": "A B C#  G-- A--",
        "6": "B A G E",
        "7": "A Fb Db E G## " ,
        "8": "E Fb G-- A##",
        "9": "F-- E# A D## B",
        # Punctuation/Spaces
        " ": "A F G-- G E Fb F-- D#",
        ",": "A D## Fb F--",
        ".": "Fb C E Db A##",
        "?": "B D F## Eb",
        "-": "G# Db F-- A B",
        "!": "E F A-- B# Gb",
        ":": "C# C Db F# G#",
        "'": "F D F G-- Ab E#",
        ";": "Ab Fb C## E-- G",
        "(": "G F D A## A B",
        ")": "Eb E B F A G##",
        "/": "Bb A Bb D E##",
        "%": "G## G E D F##",
        '"': "D G E-- F# B--",
        "~": "E## F-- G A# Bb",
        "`": "D F-- G# A# E",
        "@": "D B E## Ab",
        "#": "A D-- Gb E#",
        "$": "G-- Bb Db A# E",
        "^": "Db Gb E# A--",
        "*": "E Fb G A--",
        "_": "D Bb E Fb",
        "{": "D# A B-- F Gb",
        "}": "E F-- D## Bb A",
        "[": "E Gb A-- D#",
        "]": "A G Eb F## E#",
        "<": "A B F-- Bb",
        ">": "E G# B-- A E C",
        "|": "C E F-- C#",
        "=": "E F-- G# C##",
        "+": "A F E-- C##",
        "&": "A# Db E F G--"}
        


        # Leters
        if letter.isAlpha():
            pitch.append(letter.lower())
        else:
            pitch.append(letter)


        

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






