import sounddivice
from scipy.io.wavfile import write

fs = 44100  #simple_rate
second = int(input("Enter the time duration in second: "))   #enter your required time ...
print("Recording ...\n")

record_voice = sounddivice.rec(int(second * fs), samplerate=fs, channels=2)
sounddivice.wait()
write("out.wav", fs, record_voice)
print("Finished ... \n Please check it ...")
