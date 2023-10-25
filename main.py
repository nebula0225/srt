import random
import time
import json
import os
import winsound
from SRT import SRT

def open_json(locate, file_name):
    file_path = os.path.join(locate, file_name)
    with open(file_path, 'r', encoding="UTF-8") as j:
        json_file = json.loads(j.read())
    return json_file

def beepsound():
    fr = 1000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    while True:
        winsound.Beep(fr, du) # winsound.Beep(frequency, duration)
        time.sleep(1)
        
setting_file = open_json(os.path.join(""), "setting.json")

dep = '수서'
arr = '동대구'
date = '20231027'
hm = '223000'

trains = []
total_time = 0
srt = SRT(setting_file["id"], setting_file["pwd"], verbose=False)
while True:
    # search schedule
    trains = srt.search_train(dep, arr, date, hm)
    
    # check find schedule
    if trains:
        print(f"FIND : {trains}")
    else:
        sl = random.randint(1, 5)
        print(f"NOT FIND start sleep : {sl}")
        total_time += sl
        time.sleep(sl)
        continue

    # start reservation
    reservation = srt.reserve(trains[0])
    
    # [SRT] 09월 30일, 수서~부산(15:30~18:06) 53700원(1석), 구입기한 09월 20일 23:38
    if reservation:
        print(f"success : {reservation} / total_time second : {total_time}")
        print("https://etk.srail.kr/hpg/hra/02/selectReservationList.do?pageId=TK0102010000")
        break
beepsound()
