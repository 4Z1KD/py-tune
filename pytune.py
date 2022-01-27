import win32com.client, time, pythoncom
import pygame, pygame.sndarray
import pygame._sdl2 as sdl2
import numpy

sample_rate = 48000

PM_UNKNOWN =    1
PM_FREQ =       2
PM_FREQA =      4
PM_FREQB =      8
PM_PITCH =      16
PM_RITOFFSET =  32
PM_RIT0 =       64
PM_VFOAA =      128
PM_VFOAB =      256
PM_VFOBA =      512
PM_VFOBB =      1024
PM_VFOA =       2048
PM_VFOB =       4096
PM_VFOEQUAL =   8192
PM_VFOSWAP =    16384
PM_SPLITON =    32768
PM_SPLITOFF =   65536
PM_RITON =      131072
PM_RITOFF =     262144
PM_XITON =      524288
PM_XITOFF =     1048576
PM_RX =         2097152
PM_TX =         4194304
PM_CW_U =       8388608
PM_CW_L =       16777216
PM_SSB_U =      33554432
PM_SSB_L =      67108864
PM_DIG_U =      134217728
PM_DIG_L =      268435456
PM_AM =         536870912
PM_FM =         1073741824


pygame.init()   #initialize pygame
my_devicename = sdl2.get_audio_device_names(0)[1] #get the audio device name (this is where the radio gets the audio from) - it must be obtained prior to 'pre_init'
pygame.quit()   #quit this instance of pygame

pygame.mixer.pre_init(sample_rate, -16, 1, 1024, devicename = my_devicename) #set the device info
pygame.init()   #initialize pygame


#### sine_wave - prepare a sine wave ####
def sine_wave(hz, peak, n_samples=sample_rate):
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,2,)).astype(numpy.int16)

#### audio_freq - make the sound object ####
def audio_freq(freq = 800):
    global sound
    sample_wave = sine_wave(freq, 4096)
    sound = pygame.sndarray.make_sound(sample_wave)

w = win32com.client.gencache.EnsureDispatch("Omnirig.OmnirigX") #get the handle of omnirig

mode = int(w.Rig1.Mode) #save the current mode
w.Rig1.Mode = PM_DIG_U  #set the mode to digi
audio_freq()            #start the audio generator
sound.play(5)           #play the tone
w.Rig1.Tx = PM_TX       #ptt - on
time.sleep(5)           #wait 5 seconds to let the tuner finish
w.Rig1.Tx = PM_RX       #ptt - off
sound.stop()            #stop the tone
w.Rig1.Mode = mode      #change the mode back

#pythoncom.PumpWaitingMessages()