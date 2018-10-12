import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

#Main program

rate,data1 = wavfile.read('hello.wav')
#wavfile.write('test.wav',44100,data1) 
print(data1)

#Fourier Transform
df =np.fft.fft(data1)

#Removing frquencies
K1 = int(len(df)/44100*130)
K2 = int(len(df)/44100*400)
df[K1:K2]=0
df[len(df)-K2:len(df)-K1] = 0

#Inverse Fourier Transform
idf = np.fft.ifft(df)
clean = np.int16(idf)
wavfile.write('testsimple.wav', 44100, clean)

#Vaules for time and frequency axis
f_axis = np.linspace(0,44100,len(df))
t_axis = np.linspace(0,len(idf)/44100 ,len(idf)) #Time axis

#Plots
    #Original
plt.figure(100)
plt.plot(t_axis,data1)
plt.title("Orignal Signal")
    #Fourier Transform
plt.figure(10)
plt.plot(f_axis,abs(np.real(df)))
plt.title("Frequency Domain")
plt.xlim(130,3000)
    #Inverser Fourier Transform
plt.figure(3)
plt.plot(t_axis,idf)
plt.title("Time Domain")
