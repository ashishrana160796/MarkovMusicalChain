# MarkovMusicalChain

#### Markov chain being used to make music i.e. an example of Grapheme to Phoneme

---

#### Requirements

* Mido library
* Python 3.5.2 or any 3.x

---
#### Introduction

The order of this Markov chain is not fixed, it varies according to file that is under analysis. Midi files are used  as input and for music generation considering the simplicity. For each note the duration is rounded and grouped with every note that is played at the same time. This will result in a 2D matrix storing from_notes and to_notes:time. Which will help us to get resultant markov chain. This project is using different Classical Indian Music(Raga) styles as input. Limitation of markov chains is that hidden information like HMM model cannot be utilized only probabilites from previous state can be utilized.

---
#### FReference and Resources
* [Automatic Music Generation for Indian Classical Music](http://home.iitk.ac.in/~aawasthi/cs365/project/report.pdf).
* [Hackernoon Arcticle : Markov Chains](https://hackernoon.com/generating-music-using-markov-chains-40c3f3f46405). 

* [Music Resources - Raga](https://www.cse.iitk.ac.in/users/tvp/music/). 
* [Mido Library Documentation](https://mido.readthedocs.io/en/latest/midi_files.html).
