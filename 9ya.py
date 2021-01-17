import os
import datetime
import time
from digits import zero, one, two, three, four, five, six, seven, eight, nine, razdel

while True:
    ct = datetime.datetime.now()
    str_ct = ct.strftime('%H:%M:%S')
    print(str_ct)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear') 
    
       