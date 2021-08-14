from typing import NamedTuple

import numpy as np
import wavio
# Parameters
rate = 44100    # samples per second
T = 3           # sample duration (seconds)
f = 440.0       # sound frequency (Hz)
# Compute waveform samples
tempo = 12 // 4


class Note(NamedTuple):
    name: str
    frequency: float


MIDDLE_C = Note('C', 261.63)
MIDDLE_C_SHARP = Note('C#', 277.18)
MIDDLE_D = Note('D', 293.66)
MIDDLE_D_SHARP = Note('D#', 311.13)
MIDDLE_E = Note('E', 329.63)
MIDDLE_F = Note('F', 349.23)
MIDDLE_F_SHARP = Note('F', 369.99)
MIDDLE_G = Note('G', 392.00)
MIDDLE_G_SHARP = Note('G#', 415.30)
MIDDLE_A = Note('A', 440.00)
MIDDLE_A_SHARP = Note('A#', 466.16)
MIDDLE_B = Note('B', 493.88)

# MIDDLE_OCTAVE = [
#     MIDDLE_C,
#     MIDDLE_C_SHARP,
#     MIDDLE_D,
#     MIDDLE_D_SHARP,
#     MIDDLE_E,
#     MIDDLE_F,
#     MIDDLE_F_SHARP,
#     MIDDLE_G,
#     MIDDLE_G_SHARP,
#     MIDDLE_A,
#     MIDDLE_A_SHARP,
#     MIDDLE_B
# ]

MIDDLE_OCTAVE = [Note('_', 2**(i / 12) * 440.) for i in range(-9, 3)]

notes_map = {
    'C': 261.63,
    'C#': 277.18,
    'D': 293.66,
    'D#': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99,
    'G': 392.00,
    'G#': 415.30,
    'A': 440.00,
    'A#': 466.16,
    'B': 493.88,
    '^C': 523.25,
}


def create_notes(notes):
    size = rate // tempo
    x = np.empty(size * len(notes))

    for i, note in enumerate(notes):
        t = np.linspace(0, 1 / tempo, size, endpoint=False)
        x[size  * i:size * (i + 1)] = np.sin(2*np.pi * notes_map[note] * t)
        # x[size * 2 * i:size * (2 * i + 1)] = np.sin(2*np.pi * notes_map[note] * t)
        # x[size * (2 * i + 1):size * 2 * (i + 1)] = np.zeros(size)

    return x


def create_octave(time_per_note):
    size = int(rate * time_per_note)
    x = np.empty(size * len(MIDDLE_OCTAVE))

    for i, note in enumerate(MIDDLE_OCTAVE):
        t = np.linspace(0, time_per_note, size, endpoint=False)
        x[size * i:size * (i + 1)] = np.sin(2*np.pi * note.frequency * t)

    return x


if __name__ == '__main__':
    # x = create_notes([
    #     'A', 'G', 'F', 'G', 'A', 'A', 'A',
    #     'G', 'G', 'G', 'A', '^C', '^C',
    #     'A', 'G', 'F', 'G', 'A', 'A', 'A',
    #     'A', 'G', 'G', 'A', 'G', 'F'
    # ])

    x = create_octave(60)
    wavio.write("sine.wav", x, rate, sampwidth=3)