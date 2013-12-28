__module_name__ = 'Random Kick Reason'
__module_version__ = '0.1'
__module_description__ = 'Kicks the designated player with a random kick reason.'
__module_author__ = 'Jake0720'

rkickhelp = '\x02USAGE:  /rk <nick>'

import xchat
import random

def rk(word, word_eol, userdata):
    rkicks = (('Goodbye','See you later','Cya','Bye','Later!'))
    try:
        xchat.command('kick ' + word[1] + ' ' + random.choice(rkicks))
    except:
        xchat.prnt('\x0304Error!')

def onUnload(userdata):
    xchat.prnt('\x0304 %s has been unloaded.' % __module_name__)

xchat.hook_command('rk', rk, help=rkickhelp)
xchat.hook_unload(onUnload)
xchat.prnt('\x0304 %s has been loaded.' % __module_name__)
