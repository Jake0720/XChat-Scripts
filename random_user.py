__module_name__ = 'Random-User'
__module_version__ = '0.1'
__module_description__ = 'Finds a random user in a given channel'
__module_author__ = 'Liam Stanley'

import xchat, random

c = '\x02\x0303'
help = 'Type /ruser then press enter to find a random user in the given channel.'

print('%s%s has been loaded.' % (c, __module_name__))

def get_random(word, word_eol, userdata):
    try:
        list = xchat.get_list("users") 
        if not list:
            xchat.prnt(help)
        selection = random.choice((list))
        print '\x02User found! Username: \x0303%s\x0304%s\x03 (Connected via "\x0304%s\x03")\x02' % (selection.prefix, selection.nick, selection.host)
    except:
        xchat.prnt(help)
        
    return xchat.EAT_ALL

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('ruser', get_random, help=help)
xchat.hook_unload(onUnload)
