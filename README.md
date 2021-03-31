# WebRTC Audio Processing for Python
    - Please refer to https://pypi.org/project/webrtc-audio-processing/
    - Python binding of WebRTC Audio Processing.
        - only modified for windows

## Requirements
+ swig
+ compile toolchain
+ python

## Build
$ python setup.py install

## Usage
```python
from webrtc_audio_processing import AudioProcessingModule as AP

ap = AP(enable_vad=True, enable_ns=True)
ap.set_stream_format(16000, 1)      # set sample rate and channels
ap.set_ns_level(1)                  # NS level from 0 to 3
ap.set_vad_level(1)                 # VAD level from 0 to 3

audio_10ms = '\0' * 160 * 2         # 10ms, 16000 sample rate, 16 bits, 1 channel

# only support processing 10ms audio data each time
audio_out = ap.process_stream(audio_10ms)
print('voice: {}'.format(ap.has_voice()))
```
