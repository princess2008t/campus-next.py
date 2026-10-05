class MusicNotes:
    def __init__(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.index = 0
        self.octave = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.octave == 5:
            raise StopIteration
        frequency = self.notes[self.index] * (2 ** self.octave)
        self.index += 1
        if self.index == 7:
            self.index = 0
            self.octave += 1

        return frequency

notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)