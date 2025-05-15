import random

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
numb = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "0"]
tmp = []
for notes, numb in zip(notes, numb):
    tmp.append((notes, numb))

random.shuffle(tmp)

print(tmp)
