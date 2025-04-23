pitch = []
rhythm = []

def version_2(sentance):
    '''
    Translates a sentence to music notation
    >>> p, r = ver2.version_2('input')
    '''
    def pitches(letter):
        # Letters
        letters = {"a": "A-- C G-",
        "b": "C- G A F- G##",
        "c": "G B C# A G--",
        "d": "F- A# C-",
        "e": "G## F#",
        "f": "D E F A C##",
        "g": "B- A# C",
        "h": "B- C- C A",
        "i": "D- C# A# F- A#",
        "j": "F# D B#",
        "k": "C- G--",
        "l": "E## F# A B--",
        "m": "F- E## G#",
        "n": "A-- F- G##",
        "o": "C- D- D#",
        "p": "D# G# E##",
        "q": "A- A A# G- G G#",
        "r": "G#  F# E-",
        "s": "D## D# D D- D--",
        "t": "D- E A# G- F G-",
        "u": "C## B B##",
        "v": "F- G A F## E D-",
        "w": "A- E F D-",
        "x": "A# D- G## E#",
        "y": "C# B- E- A--",
        "z": "B## D E F A##",
        "ä": "F# B- D-- F##",
        "ö": "A C# B-- F- D##",
        "ü": "A B- E-- E##",
        "ß": "A B G E# G--",
        # Numbers
        "0": "D- D## F- A--",
        "1": "F- G## A D B",
        "2": "C D- B--",
        "3": "B# C F A##" ,
        "4": "D F G- C D#",
        "5": "A B C#  G-- A--",
        "6": "B A G E",
        "7": "A F- D- E G##" ,
        "8": "E F- G-- A##",
        "9": "F-- E# A D## B",
        # Punctuation/Spaces
        " ": "A F G-- G E F- F-- D#",
        ",": "A D## F- F--",
        ".": "F- C E D- A##",
        "?": "B D F## E-",
        "-": "G# D- F-- A B",
        "!": "E F A-- B# G-",
        ":": "C# C D- F# G#",
        "'": "F D F G-- A- E#",
        ";": "A- F- C## E-- G",
        "(": "G F D A## A B",
        ")": "E- E B F A G##",
        "/": "B- A B- D E##",
        "%": "G## G E D F##",
        '"': "D G E-- F# B--",
        "~": "E## F-- G A# B-",
        "`": "D F-- G# A# E",
        "@": "D B E## A-",
        "#": "A D-- G- E#",
        "$": "G-- B- D- A# E",
        "^": "D- G- E# A--",
        "*": "E F- G A--",
        "_": "D Bb- E F-",
        "{": "D# A B-- F G-",
        "}": "E F-- D## B- A",
        "[": "E G- A-- D#",
        "]": "A G E- F## E#",
        "<": "A B F-- B-",
        ">": "E G# B-- A E C",
        "|": "E G# B-- A E C",
        "=": "E F-- G# C##",
        "+": "A F E-- C##",
        "&": "A# D- E F G--"}
        


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
        "c": "h q 16 16 8",
        "d": "8 16 w",
        "e": "16 16",
        "f": "16 16 h 8 16",
        "g": "16 q h",
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
        "s": "16 8 16 h q",
        "t": "w h q q 16 8",
        "u": "h 16 16",
        "v": "w q q h 16 8",
        "w": "q q h q",
        "x": "w q h 16",
        "y": "16 8 16 q",
        "z": "h w 8 16 q",
        "ä": "w h 16 h",
        "ö": "q w h 16 16",
        "ü": "8 8 16 h",
        "ß": "q w h 16",

        # Numbers
        "0": "8 q w .",
        "1": "h q 16 16 .",
        "2": "w w .",
        "3": "w 8 16 .",
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
        "?": "w h q .",
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
        "@": "w h q .",
        "#": "16 q 8 .",
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
        "|": "q q 8 w h .",
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






