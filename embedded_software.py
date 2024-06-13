import machine
import utime
import array
import math
import struct

try:
    import numpy as np
except ImportError:
    import ufft as np 

ADC_PIN = 27
SAMPLE_RATE = 1000 
SAMPLE_SIZE = 1024  
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


adc = machine.ADC(ADC_PIN)

def read_adc(samples, sample_rate):
    buffer = array.array('H', [0] * samples)
    sample_interval = 1 / sample_rate
    for i in range(samples):
        buffer[i] = adc.read_u16()
        utime.sleep(sample_interval)
    return buffer

def compute_fft(data):
    n = len(data)
    fft_result = np.fft.fft(data)
    freqs = np.fft.fftfreq(n, d=1/SAMPLE_RATE)
    magnitudes = np.abs(fft_result)
    return freqs[:n//2], magnitudes[:n//2]

def get_note_from_frequency(freq):
    if freq == 0:
        return None, None
    A4 = 440
    C0 = A4 * math.pow(2, -4.75)
    h = round(12 * math.log2(freq / C0))
    octave = h // 12
    note_index = h % 12
    note = NOTE_NAMES[note_index]
    return note, octave

def main():
    while True:
        data = read_adc(SAMPLE_SIZE, SAMPLE_RATE)
        
        freqs, magnitudes = compute_fft(data)
        
        peak_index = np.argmax(magnitudes)
        peak_freq = freqs[peak_index]
        note, octave = get_note_from_frequency(peak_freq)
        if note:
            print(f"Frequency: {peak_freq:.2f} Hz, Note: {note}{octave}")
        else:
            print("No valid frequency detected.")
        utime.sleep(1)

if __name__ == "__main__":
    main()
