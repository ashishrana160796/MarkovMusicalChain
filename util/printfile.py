import mido

def inspect(file_name):
    """
    This method displays all the information like notes, velocity etc.
    about the midi file that is passed in as argument according to
    different tracks that are part of the soundtrack. 
    """
    mid = mido.MidiFile(file_name)
    for i, track in enumerate(mid.tracks):
        print ('Track {}: {}'.format(i, track.name))
        for info in track:
            print(info)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        inspect(sys.argv[1])
