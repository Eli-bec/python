https://realpython.com/python-speech-recognition/

I am running all of the following in a virtual environment (python38-64), but it should work properly in other computers.
### install Speech Recognition with pip
 `pip install SpeechRecognition`

Now it should be able to import speech_recognition in python

### install pyaudio with pip
`pip install pyaudio`

Ideally it can directly install the right version of pyaudio via pip.  
But in my case, it will show an error  
My solution is to download a wheel file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and install it by
`pip install <filename>`  
### test the installation
`python -m speech_recognition`
