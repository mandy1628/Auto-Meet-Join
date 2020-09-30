from Monday import Monday
from Tuesday import Tuesday
from Wednesday import Wednesday
from Thursday import Thursday
from Friday import Friday
from datetime import datetime

def holiday():
    print('Go to bed again you idiot!! You wake up on wrong day bastard')

mon = Monday()
tue = Tuesday()
wed = Wednesday()
thr = Thursday()
fri = Friday()
today = datetime.today().strftime('%A')
days = {'Monday':mon,'Tuesday':tue,'Wednesday':wed,'Thursday':thr,'Friday':fri}
if today in days.keys():
    days.get(today).schedule()
else:
    holiday()