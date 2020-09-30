import sched, time, webbrowser, locale
from datetime import datetime
from connectBrowser import hangoutsMeet

class Tuesday:
    def __init__(self):
        self.initTime = datetime.now()
        self.scheduler = sched.scheduler(time.time,time.sleep)
        locale.setlocale(locale.LC_ALL,'en_US')

    def openMeetCN(self):
        str = 'https://meet.google.com/ofs-wezh-che'
        hangoutsMeet(str)
    
    def openMeetIOT(self):
        str = 'https://meet.google.com/crs-qvyh-jtx'
        hangoutsMeet(str)
    
    def openMeetSE(self):
        str = 'https://meet.google.com/kgh-hwtg-vus'
        hangoutsMeet(str)

    def schedule(self):
        initTime = self.initTime
        scheduler = self.scheduler

        time_str_CN = '07:55:00'
        time_object_CN = datetime.strptime(time_str_CN, '%H:%M:%S').time()
        time_rem_CN = (time_object_CN.hour-initTime.hour)*60*60 + (time_object_CN.minute-initTime.minute)*60 + (time_object_CN.second-initTime.second)

        time_str_IOT = '08:58:00'
        time_object_IOT = datetime.strptime(time_str_IOT, '%H:%M:%S').time()
        time_rem_IOT = (time_object_IOT.hour-initTime.hour)*60*60 + (time_object_IOT.minute-initTime.minute)*60 + (time_object_IOT.second-initTime.second)

        time_str_SE = '11:10:00'
        time_object_SE = datetime.strptime(time_str_SE, '%H:%M:%S').time()
        time_rem_SE = (time_object_SE.hour-initTime.hour)*60*60 + (time_object_SE.minute-initTime.minute)*60 + (time_object_SE.second-initTime.second)

        count = 0
        if time_rem_CN >= 0:
            scheduler.enterabs(time.time()+time_rem_CN,2,self.openMeetCN)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            count += 1

        if time_rem_IOT >= 0:
            scheduler.enterabs(time.time()+time_rem_IOT,1,self.openMeetIOT)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            else:
                print("You piece of shit!! you are always late!! fuck off")
            count += 1

        if time_rem_SE >= 0:
            scheduler.enterabs(time.time()+time_rem_SE,2,self.openMeetSE)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            else:
                print("You piece of shit!! you are always late!! fuck off")
            count += 1

        scheduler.run()