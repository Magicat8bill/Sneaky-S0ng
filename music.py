from music21 import *
import ver2
import time
import sys
import argparse

reader = input("Do you have a musicxml reader? Y or N: ")

file = open("config.txt", "r+") 
lines = file.readline().strip()
if reader.upper() == "Y":
    if lines != "1":
        configure.run()
        file.write("1")

def create_musicxml(pitches, rhythms, output_file):
    """
    Create a MusicXML file from given pitches and rhythms.
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sneaky S0ng - Music Encryption Tool")
    parser.add_argument("sentence", help="The sentence you want to encrypt")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output (time to encrypt)")

    args = parser.parse_args()

    p, r = ver2.vertion_2(args.sentence)
    pitches = p
    rhythms = r
    print(r)

    output_file = "output.xml"

    start_time = time.time()  # Start timing
    exit_code = create_musicxml(pitches, rhythms, output_file)
    end_time = time.time()  # End timing

    if args.verbose:
        print(f"Time taken to create MusicXML: {end_time - start_time:.4f} seconds")

    print(f"MusicXML file created: {output_file}")
    sys.exit(exit_code)
