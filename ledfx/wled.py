import requests
from ledfx.config import save_config
from collections import namedtuple

#Get 'ip_address' C:\Users\Matt\AppData\Roaming\.ledfx\config.yaml 
# of current device and use as a str so line 143 correctly works

#Below is based on: https://github.com/Aircoookie/WLED/wiki/HTTP-request-API

#Need to find out how to get tickbox 'Power LED' data 
# from directory ledfx.wled.py for the below url requests

#Also Need to figure out upon clicking 'Set Effect', that does not enable E1.31

def powerState(value):
    requests.get('http://192.168.1.102/win&', params={'T': 1 if value else 0})
powerState(False)

WLEDEffects = {
    'Solid': 'FX=0',
    'Blink': 'FX=1',
    'Breathe': 'FX=2',
    'Wipe': 'FX=3',
    'Wipe Random': 'FX=4',
    'Random Colors': 'FX=5',
    'Sweep': 'FX=6',
    'Dynamic': 'FX=7',
    'Colorloop': 'FX=8',
    'Rainbow': 'FX=9',
    'Scan': 'FX=10',
    'Dual Scan': 'FX=11',
    'Fade': 'FX=12',
    'Chase': 'FX=13',
    'Chase Rainbow': 'FX=14',
    'Running': 'FX=15',
    'Saw': 'FX=16',
    'Twinkle': 'FX=17',
    'Dissolve': 'FX=18',
    'Dissolve Rnd': 'FX=19',
    'Sparkle': 'FX=20',
    'Dark Sparkle': 'FX=21',
    'Sparkle+': 'FX=22',
    'Strobe': 'FX=23',
    'Strobe Rainbow': 'FX=24',
    'Mega Strobe': 'FX=25',
    'Blink Rainbow': 'FX=26',
    'Android': 'FX=27',
    'Chase': 'FX=28',
    'Chase Random': 'FX=29',
    'Chase Rainbow': 'FX=30',
    'Chase Flash': 'FX=31',
    'Chase Flash Rnd': 'FX=32',
    'Rainbow Runner': 'FX=33',
    'Colorful': 'FX=34',
    'Traffic Light': 'FX=35',
    'Sweep Random': 'FX=36',
    'Running 2': 'FX=37',
    'Red & Blue': 'FX=38',
    'Stream': 'FX=39',
    'Scanner': 'FX=40',
    'Lighthouse': 'FX=41',
    'Fireworks': 'FX=42',
    'Rain': 'FX=43',
    'Merry Christmas': 'FX=44',
    'Fire Flicker': 'FX=45',
    'Gradient': 'FX=46',
    'Loading': 'FX=47',
    'In Out': 'FX=48',
    'In In': 'FX=49',
    'Out Out': 'FX=50',
    'Out In': 'FX=51',
    'Circus': 'FX=52',
    'Halloween': 'FX=53',
    'Tri Chase': 'FX=54',
    'Tri Wipe': 'FX=55',
    'Tri Fade': 'FX=56',
    'Lightning': 'FX=57',
    'ICU': 'FX=58',
    'Multi Comet': 'FX=59',
    'Dual Scanner': 'FX=60',
    'Stream 2': 'FX=61',
    'Oscillate': 'FX=62',
    'Pride 2015': 'FX=63',
    'Juggle': 'FX=64',
    'Palette': 'FX=65',
    'Fire 2012': 'FX=66',
    'Colorwaves': 'FX=67',
    'BPM': 'FX=68',
    'Fill Noise': 'FX=69',
    'Noise 1': 'FX=70',
    'Noise 2': 'FX=71',
    'Noise 3': 'FX=72',
    'Noise 4': 'FX=73',
    'Colortwinkle': 'FX=74',
    'Lake': 'FX=75',
    'Meteor': 'FX=76',
    'Smooth Meteor': 'FX=77',
    'Railway': 'FX=78',
    'Ripple': 'FX=79',
    }

WLEDPalette = {
    'Default': 'FP=0',
    'Random Cycle': 'FP=1',
    'Primary color': 'FP=2',
    'Based on primary': 'FP=3',
    'Set colors': 'FP=4',
    'Based on set': 'FP=5',
    'Party': 'FP=6',
    'Cloud': 'FP=7',
    'Lava': 'FP=8',
    'Ocean': 'FP=9',
    'Forest': 'FP=10',
    'Rainbow': 'FP=10',
    'Rainbow bands': 'FP=10',
    'Sunset': 'FP=10',
    'Rivendell': 'FP=10',
    'Breeze': 'FP=10',
    'Red & Blue': 'FP=10',
    'Yellowout': 'FP=10',
    'Analoguous': 'FP=10',
    'Splash': 'FP=10',
    'Pastel': 'FP=10',
    'Sunset 2': 'FP=20',
    'Beech': 'FP=20',
    'Vintage': 'FP=20',
    'Departure': 'FP=20',
    'Landscape': 'FP=20',
    'Beach': 'FP=20',
    'Android': 'FP=20',
    'Sherbet': 'FP=20',
    'Hult': 'FP=20',
    'Hult 64': 'FP=20',
    'Drywet': 'FP=30',
    'Jul': 'FP=30',
    'Grintage': 'FP=30',
    'Rewhi': 'FP=30',
    'Fire': 'FP=30',
    'Icefire':'FP=30',
    'Cyane': 'FP=30',
    'Light Pink': 'FP=30',
    'Autumn': 'FP=30',
    'Magenta': 'FP=30',
    'Magred': 'FP=40',
    'Yelmag': 'FP=40',
    'Yelblu': 'FP=40',
    'Orange & Teal': 'FP=40',
    'Tiamat': 'FP=40',
    'April Night': 'FP=40',
}

WLEDSpeed = {
    'Slow': 'SX=1',
    'Med-Slow': 'SX=1',
    'Med': 'SX=1',
    'Med-Fast': 'SX=1',
    'Fast': 'SX=1',
    'Fastest': 'SX=1',
}

WLEDIntensity = {
    'Slow': 'IX=1',
    'Med-Slow': 'IX=1',
    'Med': 'IX=1',
    'Med-Fast': 'IX=1',
    'Fast': 'IX=1',
    'Fastest': 'IX=1',
}

WLEDBrightness = {
    'Low - 10 Percent': 'A=1',
    'A Little- 25 Percent': 'A=1',
    'Med - 50 Percent': 'A=1',
    'Bright - 80 Percent': 'A=1',
    'Brightest - 100 Percent': 'A=1',
}

WLEDHueColor = {
    'Red': 'HU=1',
    'Blue': 'HU=255',
    'Green': 'HU=255',
}

#For testing
http = 'http://'
WLEDAPI = '/win&'

#variables
ip_address = '192.168.1.102'
WLEDEffects = 'FX=0&'
wledand = '&'

url = http + ip_address + WLEDAPI + WLEDEffects + WLEDPalette + WLEDSpeed + WLEDIntensity + WLEDBrightness + WLEDHueColor
wled = requests.get(url)
print(wled.text)