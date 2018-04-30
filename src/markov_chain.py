# This class handles the storage and manipulation of a markov chain of notes.

from collections import Counter, defaultdict, namedtuple

import random

Note = namedtuple('Note', ['note', 'duration'])

class MarkovChain:
    """
    Markov chained is created, stored and manipulated by this class.
    """
    def __init__(self):
        self.chain = defaultdict(Counter)
        self.sums = defaultdict(int)

    @staticmethod
    def create_from_dict(dict):
        """
        Dictionay is created via Markov chain assumption that to_notes depend only on from_notes.
        It stores from_notes, to_notes and duration. Limitation, if no such direct dependency exist
        b/w to_notes and from_notes then empty will be generated. Here, in this case using HMM model 
        will provide suitable soundtrack but it is not covered in this project.
        """
        m = MarkovChain()
        for from_note, to_notes in dict.items():
            for k, v in to_notes.items():
                m.add(from_note, k, v)
        return m


    def _serialize(self, note, duration):
        return Note(note, duration)

    def __str__(self):
        return str(self.get_chain())

    def add(self, from_note, to_note, duration):
        self.chain[from_note][self._serialize(to_note, duration)] += 1
        self.sums[from_note] += 1

    def get_next(self, seed_note):
        """
        From given seed_note next note is selected in two ways either seed_note is not part
        of the chain, in that case return a random note. Otherwise, select a node that first
        matches or greater than its frequency while iterating through chain. 
        """
        if seed_note is None or seed_note not in self.chain:
            try :
                random_chain = self.chain[random.choice(list(self.chain.keys()))]
                return random.choice(list(random_chain.keys()))
            except :
                print ('File not compatible with current implementation !!')
            
        next_note_counter = random.randint(0, self.sums[seed_note])
        for note, frequency in self.chain[seed_note].items():
            next_note_counter -= frequency
            if next_note_counter <= 0:
                return note

    def merge(self, other):
        """
        It merges notes and their frequencies to current chain if from_notes
        are part of other chain being merged.
        """
        assert isinstance(other, MarkovChain)
        self.sums = defaultdict(int)
        for from_note, to_notes in other.chain.items():
            self.chain[from_note].update(to_notes)
        for from_note, to_notes in self.chain.items():
            self.sums[from_note] = sum(self.chain[from_note].values())

    def get_chain(self):
        """
        It returns a set of chain keys which are notes & its values in dictionary form
        which are to_notes and their durations.
        """
        return {k: dict(v) for k, v in self.chain.items()}

############################################################################
##   Demo : Dictionaries being represented as adjacency matrix of graph.  ##
############################################################################

    def print_as_matrix(self, limit=10):
        columns = []
        for from_note, to_notes in self.chain.items():
            for note in to_notes:
                if note not in columns:
                    columns.append(note)
        _col = lambda string: '{:<8}'.format(string)
        _note = lambda note: '{}:{}'.format(note.note, note.duration)
        out = _col('')
        out += ''.join([_col(_note(note)) for note in columns[:limit]]) + '\n'
        for from_note, to_notes in self.chain.items():
            out += _col(from_note)
            for note in columns[:limit]:
                out += _col(to_notes[note])
            out += '\n'
        print(out)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == 'demo':
        m = MarkovChain()
        m.add(12, 14, 225)
        m.add(12, 15, 210)
        m.add(14, 25, 240)
        m.add(12, 14, 226)
        n = MarkovChain()
        n.add(10, 13, 101)
        n.add(12, 14, 210)
        m.merge(n)
        print(m)
        m.print_as_matrix()
        
