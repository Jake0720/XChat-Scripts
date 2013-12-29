__module_name__ = 'Flip Text Plugin'
__module_version__ = '0.2'
__module_description__ = 'Inverts your text!'
__module_author__ = 'Jake0720, with a little help from Liam Stanley'

import xchat

c = '\x02\x0303'
help = '%sType /flip <message> then press enter to make it backwards.' % c

print('%s%s has been loaded.' % (c, __module_name__))

def flip(word, word_eol, userdata):
    try:
        xchat.command('say %s' % word_eol[1][::-1])
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('flip', flip, help=help)
xchat.hook_unload(onUnload)