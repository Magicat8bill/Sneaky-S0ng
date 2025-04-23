import time
from music21 import *
from sneaky_s0ng import *
def cm(p,r,o):
    s=stream.Score();part=stream.Part();s.append(part);s.insert(0,metadata.Metadata());s.metadata.title='Cypher';s.metadata.composer='$neaky $0ng';m=stream.Measure();m.timeSignature=meter.TimeSignature('4/4');part.append(m)
    rm={'q':1,'h':2,'8':.5,'r':'rest','w':4,'16':.25,'.':1.5}
    for P,R in zip(p.split(),r.split()):
        d=rm.get(R)
        if not d:print(f"Invalid rhythm: {R}");exit()
        if d=='rest':n=note.Rest();n.quarterLength=1;m.append(n)
        else:
            if len(P)==1:P+='4'
            n=note.Note(P);n.quarterLength=d
            while n.quarterLength>0:
                rem=4-m.duration.quarterLength
                if rem<=0:m=stream.Measure();part.append(m);rem=4
                if n.quarterLength>rem:
                    tn=note.Note(P);tn.quarterLength=rem;tn.tie=tie.Tie('start');m.append(tn);n.quarterLength-=rem;m=stream.Measure();part.append(m);tn=note.Note(P);tn.quarterLength=n.quarterLength;tn.tie=tie.Tie('stop');m.append(tn);break
                else:m.append(n);break
    s.write('musicxml',fp=o);return True
def mw(s,v=False):
    p,r=ver2.version_2(s);o="output.xml";t=time.time();
    suc=cm(p,r,o);end=time.time()
    if v:print(f"Time: {end - t:.4f}s")
    if suc:
        print(f"MusicXML file created: {o}")
        if input("MusicXML reader? (y/n): ").lower() == 'y':return o
        else:print("Install a MusicXML reader.");return None
    return None
mw('test')