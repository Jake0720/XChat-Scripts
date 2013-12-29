__module_name__ = 'Date and Time'
__module_version__ = '0.1'
__module_description__ = 'Tells you what the current date and time is.'
__module_author__ = 'Jake0720'

import xchat
from datetime import datetime

c = '\x02\x0312'
datehelp = '~DATE HELP:\n~To see the date, type %s/date\x0f.\n~To announce the date, type %s/date say\x0f.' % (c, c)
timehelp = '*TIME HELP:\n*To see the time, type %s/time\x0f.\n*To announce the time, type %s/time say\x0f.' % (c, c)

def get(type):
    now = datetime.now()
    if type == 'date':
        return str(now.month), str(now.day), str(now.year)
    else:
        # Assume time
        return str(now.hour), str(now.minute)
def date(word, word_eol, userdata):
    month, day, year = get('date')
    
    if len(word) == 1:
        return xchat.prnt('The current date is: %s%s/%s/%s' % (c, month, day, year))
    else:# Assume len() is >=2
        if word[1].lower() == 'say':
            return xchat.command('say The current date is: %s%s/%s/%s' % (c, month, day, year))
        return xchat.prnt(datehelp)

def time(word, word_eol, userdata):
    hour, minute = get('time')
    
    if len(word) == 1:
        return xchat.prnt('The current time is: %s%s:%s' % (c, hour, minute))
    else:
        if word[1].lower() == 'say':
            return xchat.command('say The current time is: %s%s:%s' % (c, hour, minute))
        return xchat.prnt(timehelp)

def onUnload(userdata):
    xchat.prnt('%s%s, Version: %s has been unloaded.' % (c, __module_name__, __module_version__))

xchat.hook_command('time', time, help=timehelp)
xchat.hook_command('date', date, help=datehelp)
xchat.hook_unload(onUnload)
xchat.prnt('%s%s, Version: %s has been loaded.' % (c, __module_name__, __module_version__))