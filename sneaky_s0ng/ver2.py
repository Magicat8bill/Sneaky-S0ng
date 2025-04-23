L={"a":"A-- C Gb","b":"Cb G A Fb G##","c":"G B C# A","d":"Fb A# Cb","e":"G## F#","f":"D E F A","g":"Bb A# C","h":"Bb Cb C A","i":"Db C# A# Fb A#","j":"F# D B#","k":"Cb G--","l":"E## F# A B--","m":"Fb E## G#","n":"A-- Fb G##","o":"Cb Db D#","p":"D# G# E##","q":"Ab A A# Gb G G#","r":"G# F# Eb","s":"D## D# D Db D--","t":"Db E A# Gb F Gb","u":"C## B B##","v":"Fb G A F## E Db","w":"Ab E F Db","x":"A# Db G## E#","y":"C# Bb Eb A--","z":"B## D E F A##"," ":"A F G-- G E Fb F-- D#",",":"A D## Fb F--",".":"Fb C E Db A##"}
B={"a":"8 16 16","b":"w q 16 8 16","c":"h q 16 16 8 16","d":"8 16 w","e":"16 16","f":"16 16 h 8 16","g":"16 16 16 16 q h","h":"h q 16 8","i":"h 16 16 w q","j":"h 16 q","k":"w w","l":"16 8 q 8","m":"8 16 q","n":"h h q","o":"8 16 h","p":"w q 16","q":"16 8 q q 16 8","r":"h w 8","s":"16 8 16 h q q","t":"w h q q 16 8","u":"h 16 16","v":"w q q h 16 8","w":"q q h q","x":"w q h 16","y":"16 8 16 q","z":"h w 8 16 q"," ":"q w 16 8 w h w .",",":"q h 16 .",".":"8 16 8 8 ."}
def m(l):
    try:
        return [' '.join(x.split() + [x.split()[-1]]*2) for x in l if x.strip()]
    except IndexError:
        return []
def v(s):
    if not isinstance(s, str):
        return '', ''
    p, r = [], []
    for c in s:
        c = c.lower()
        try:
            p.append(L.get(c, ''))
            r.append(B.get(c, ''))
        except AttributeError:
            continue
    return ' '.join(m(p)), ' '.join(m(r))