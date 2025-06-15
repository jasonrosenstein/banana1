import math
import wave
import struct

SAMPLE_RATE = 44100
DURATION = 10  # seconds
BASE_FREQ = 200.0  # Hz
DELTA = 0.5  # Epsilon wave difference in Hz

left_freq = BASE_FREQ - DELTA / 2
right_freq = BASE_FREQ + DELTA / 2
frames = []
for i in range(int(SAMPLE_RATE * DURATION)):
    t = i / SAMPLE_RATE
    left_val = math.sin(2 * math.pi * left_freq * t)
    right_val = math.sin(2 * math.pi * right_freq * t)
    frames.append(struct.pack('<hh', int(left_val * 32767), int(right_val * 32767)))

def write_wav(filename):
    with wave.open(filename, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(b''.join(frames))

if __name__ == '__main__':
    write_wav('epsilon_binaural.wav')
    print('Generated epsilon_binaural.wav')
