from markov_chain import MarkovChain

import random
import mido

class Generator:
    """
    This class generates new song with given markov chain with to & from note information
    and their given frequencies.
    """
    def __init__(self, markov_chain):
        self.markov_chain = markov_chain

    @staticmethod
    def load(markov_chain):
        assert isinstance(markov_chain, MarkovChain)
        return Generator(markov_chain)

    def _note_to_information(self, note):
        """
        new note with its duration getting converted into their
        required format.
        """
        return [
            mido.Message('note_on', note=note.note, velocity=127,
                         time=0),
            mido.Message('note_off', note=note.note, velocity=0,
                         time=note.duration)
        ]

    def generate(self, filename):
        """
        Given fixed number of notes are appended and new track is
        generated with markov chains.
        """
        with mido.midifiles.MidiFile() as midi:
            track = mido.MidiTrack()
            last_note = None
            for i in range(100):
                new_note = self.markov_chain.get_next(last_note)
                track.extend(self._note_to_information(new_note))
            midi.tracks.append(track)
            midi.save(filename)

########################################################################
##   Main : Run "generator.py in.mid out.mid" for getting the track.  ##
########################################################################


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        from parser import Parser
        chain = Parser(sys.argv[1]).get_chain()
        Generator.load(chain).generate(sys.argv[2])
        print("Generated markov chain")
