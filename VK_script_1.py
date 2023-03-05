import configparser as cfgp
from screeninfo import get_monitors
import subprocess
import re
import ctypes

scr_res = []

user32 = ctypes.windll.user32
scr_width = user32.GetSystemMetrics(0)
scr_height = user32.GetSystemMetrics(1)

cfg_strings = []

with open(r'C:\Program Files (x86)\SteamCore\steamapps\common\Underlords\game\dac\cfg\video.txt', encoding='utf8') as f:
    for line in f:
        if "setting.defaultres" in line:
            cfg_strings.append(re.findall(r'\d+', line))
print(cfg_strings[1][0])

with open(r'C:\Program Files (x86)\SteamCore\steamapps\common\Underlords\game\dac\cfg\video.txt', 'r', encoding='utf8') as file :
    filedata = file.read()

filedata = filedata.replace(str(cfg_strings[0][0]), str(scr_width))
filedata = filedata.replace(str(cfg_strings[1][0]), str(scr_height))

with open('file.txt', 'w') as file:
    file.write(filedata)

subprocess.call(r"C:\Program Files (x86)\SteamCore\Steam.exe -applaunch 1046930")
