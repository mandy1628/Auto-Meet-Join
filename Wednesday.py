import sched, time, webbrowser, locale
from datetime import datetime
from connectBrowser import hangoutsMeet

class Wednesday:
    def __init__(self):
        self.initTime = datetime.now()
        self.scheduler = sched.scheduler(time.time,time.sleep)
        locale.setlocale(locale.LC_ALL,'en_US')

    def openMeetCloud(self):
        str = 'https://meet.google.com/fcc-ziqq-gdi'
        hangoutsMeet(str)
    
    def openMeetAutomata(self):
        str = 'https://meet.google.com/tgq-njto-gne'
        hangoutsMeet(str)
    
    def openMeetCN(self):
        str = 'https://meet.google.com/ofs-wezh-che'
        hangoutsMeet(str)

    def schedule(self):
        initTime = self.initTime
        scheduler = self.scheduler

        time_str_Automata = '07:59:00'
        time_object_Automata = datetime.strptime(time_str_Automata, '%H:%M:%S').time()
        time_rem_Automata = (time_object_Automata.hour-initTime.hour)*60*60 + (time_object_Automata.minute-initTime.minute)*60 + (time_object_Automata.second-initTime.second)

        time_str_Cloud = '10:10:00'
        time_object_Cloud = datetime.strptime(time_str_Cloud, '%H:%M:%S').time()
        time_rem_Cloud = (time_object_Cloud.hour-initTime.hour)*60*60 + (time_object_Cloud.minute-initTime.minute)*60 + (time_object_Cloud.second-initTime.second)

        time_str_CN = '11:10:00'
        time_object_CN = datetime.strptime(time_str_CN, '%H:%M:%S').time()
        time_rem_CN = (time_object_CN.hour-initTime.hour)*60*60 + (time_object_CN.minute-initTime.minute)*60 + (time_object_CN.second-initTime.second)

        count = 0
        if time_rem_Automata >= 0:
            scheduler.enterabs(time.time()+time_rem_Automata,3,self.openMeetAutomata)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            else:
                print("You piece of shit!! you are always late!! fuck off")
            count += 1

        if time_rem_Cloud >= 0:
            scheduler.enterabs(time.time()+time_rem_Cloud,1,self.openMeetCloud)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            else:
                print("You piece of shit!! you are always late!! fuck off")
            count += 1

        if time_rem_CN >= 0:
            scheduler.enterabs(time.time()+time_rem_CN,2,self.openMeetCN)
        else:
            if count == 0:
                print("You are running late motherfucker")
            elif count == 1:
                print('You are late again asshole')
            else:
                print("You piece of shit!! you are always late!! fuck off")
            count += 1

        scheduler.run()