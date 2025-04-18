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
        if letter.isalpha():
            pitch.append(letters[letter.lower()])
        else:
            pitch.append(letters[letter])


        

        return pitch

        
    def beat(letter):
        # Letters
        letters = {"a": "8 16 16",
        "b": "w q 16 8 16",
        "c": "h q 16 16 8 16",
        "d": "8 16 w",
        "e": "16 16",
        "f": "16 16 h 8 16",
        "g": "16 16 16 16 q h",
        "h": "h q 16 8",
        "i": "h 16 16 w q",
        "j": "h 16 q",
        "k": "w w",
        "l": "16 8 q 8",
        "m": "8 16 q",
        "n": "h h q",
        "o": "8 16 h",
        "p": "w q 16",
        "q": "16 8 q q 16 8",
        "r": "h w 8",
        "s": "16 8 16 h q q",
        "t": "w h q q 16 8",
        "u": "h 16 16",
        "v": "w q q h 16 8",
        "w": "q q h q",
        "x": "w q  h 16",
        "y": "16 8 16 q",
        "z": "h w 8 16 q",
        "ä": "w h 16 h",
        "ö": "q w h 16 16",
        "ü": "8 8 16 h q",
        "ß": "q w h 16",

        # Numbers
        "0": "16 8 q w .",
        "1": "h q 16 16 .",
        "2": "w w .",
        "3": "w 8 16 ." ,
        "4": "h q 8 w .",
        "5": "h w 16 q .",
        "6": "w 16 16 .",
        "7": "16 8 q h ." ,
        "8": "h w 8 .",
        "9": "q w h 16 .",
        # Punctuation/Spaces
        " ": "q w 16 8 w h w .",
        ",": "q h 16 .",
        ".": "8 16 8 8 .",
        "?": "w h q 8 .",
        "-": "h q w 16 .",
        "!": "16 8 q q .",
        ":": "16 16 8 q .",
        "'": "w q 16 16 8 . ",
        ";": "q h 8 w .",
        "(": "16 w q 16 h .",
        ")": "h h 8 8 16 .",
        "/": "w q h h .",
        "$": "q w h h .",
        "%": "q h h 8 .",
        '"': "8 w h 8 .",
        "~": "w w w w .",
        "`": "q h h q .",
        "@": "w h q ."  ,
        "#": "16 q 8 ." ,
        "^": "8 h 8 .",
        "&": "q q h 16 .",
        "*": "q 16 h .",
        "_": "w h h .",
        "{": "q w h 8 .",
        "}": "q q h h .",
        "[": "8 16 h .",
        "]": "q h 16 8 .",
        "<": "w w q .",
        ">": "q w h 16 16 .",
        "|": "q q 8 .",
        "=": "q 16 8 .",
        "+": " h h h ."}

        if letter.isalpha():
            rhythm.append(letters[letter.lower()])
        else:
            rhythm.append(letters[letter])


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






