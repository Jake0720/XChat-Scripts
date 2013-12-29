__module_name__ = 'Random Ping'
__module_version__ = '0.1'
__module_description__ = 'Pings someone in the channel randomly.'
__module_author__ = 'Jake0720'

import xchat
from random import choice

c = '\x0312'
help = 'Type /rping to ping someone in your current channel randomly.'
print('%s%s has been loaded.' % (c, __module_name__))

def random_ping(word, word_eol, userdata):
    users = xchat.get_list('users')
    nicks = choice((users))
    try:
        return xchat.command('say %s' % nicks.nick)
    except:
        return xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('rping', random_ping, help=help)
xchat.hook_unload(onUnload)
