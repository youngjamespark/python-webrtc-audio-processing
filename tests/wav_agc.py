
import sys
import wave
from webrtc_audio_processing import AP


if len(sys.argv) < 3:
    print('Usage: {} audio.wav out.wav'.format(sys.argv[0]))
    sys.exit(1)

wav = wave.open(sys.argv[1], 'rb')
rate = wav.getframerate()
width = wav.getsampwidth()
channels = wav.getnchannels()

out = wave.open(sys.argv[2], 'wb')
out.setnchannels(channels)
out.setsampwidth(width)
out.setframerate(rate)

ap = AP(agc_type=1)

# set input/output stream format
ap.set_stream_format(rate, channels, rate, channels)

frames_size = int(rate * 10 / 1000)
frames_bytes = frames_size * width * channels

ap.set_agc_target(-20)


while True:
    data = wav.readframes(frames_size)
    if len(data) != frames_bytes:
        break

    data_out = ap.process_stream(data)

    out.writeframes(data_out)

wav.close()
out.close()