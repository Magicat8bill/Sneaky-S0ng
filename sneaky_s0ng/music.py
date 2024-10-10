from music21 import *
from sneaky_s0ng import ver2

def create_musicxml(pitches, rhythms, output_file):
    reader = input("Do you have a musicxml reader? Y or N: ")
    if reader.upper() == "Y":
            config = input("Do you want to configure your musicxml reader? Y or N: ")
            if config.upper() == "Y":
                configure.run()

    """
    Create a MusicXML file from given pitches and rhythms.

    Args:
        pitches (str): Space-separated string of pitches (e.g., "Db4 Bb4 A4 D##4 C4 A4 D##4 C4 Cb4 A4 G#4 C4 D##4 D#4 D4 Db4 D#4 D4 G4 D#4 Fb4").
        rhythms (str): Space-separated string of rhythms (e.g., "h q h 16 16 h 16 16 w h w 16 16 h 8 h h 8 w h 16").
        output_file (str): Output file name for the MusicXML file.
    """
    rhythm_map = {
        'q': 1.0,
        'h': 2.0,
        '8': 0.5,
        'r': 'rest',
        'w': 4.0,
        '16': 0.25,
        '.': 1.5
    }
    
    score = stream.Score()
    part = stream.Part()
    score.append(part)

    score.insert(0, metadata.Metadata())
    score.metadata.title = 'Cypher'
    score.metadata.composer = '$neaky $0ng'
    
    measure = stream.Measure()
    measure.timeSignature = meter.TimeSignature('4/4')
    part.append(measure)
    
    for pitch, rhythm in zip(pitches.split(), rhythms.split()):
        dur = rhythm_map.get(rhythm)
        if dur is None:
            print(f"Invalid rhythm: {rhythm}")
            exit()
        
        if dur == 'rest':
            n = note.Rest()
            n.quarterLength = 1.0  # Default rest duration
            measure.append(n)
        else:
            if len(pitch) == 1:
                pitch += '4'  # Default to octave 4 if not specified
            n = note.Note(pitch)
            n.quarterLength = dur
            while n.quarterLength > 0:
                remaining_in_measure = 4.0 - measure.duration.quarterLength
                if remaining_in_measure <= 0:
                    measure = stream.Measure()
                    part.append(measure)
                    remaining_in_measure = 4.0
                
                if n.quarterLength > remaining_in_measure:
                    tie_note = note.Note(pitch)
                    tie_note.quarterLength = remaining_in_measure
                    tie_note.tie = tie.Tie('start')
                    measure.append(tie_note)
                    
                    n.quarterLength -= remaining_in_measure
                    measure = stream.Measure()
                    part.append(measure)
                    
                    tie_note = note.Note(pitch)
                    tie_note.quarterLength = n.quarterLength
                    tie_note.tie = tie.Tie('stop')
                    measure.append(tie_note)
                    break
                else:
                    measure.append(n)
                    break
    
    score.write('musicxml', fp=output_file)
    if reader.upper() == "Y":
        score.show()

def musicxml_writer(sentence):
    '''
    Takes a sentence and encrypts it to music notation 
    and writes it to musicxml
    >>> m = music.musicxml_writer('input')
    '''
    # pitches = input("Enter pitches (e.g., Db Bb A): ")
    # rhythms = input("Enter rhythms (e.g., q h 8 r): ")
    p, r = ver2.version_2(sentence)
    pitches = p
    rhythms = r
    # print(r)
    # print(p)
    output_file = "output.xml"
    create_musicxml(pitches, rhythms, output_file)
    print(f"MusicXML file created: {output_file}")


