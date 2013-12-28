__module_name__ = 'Flip Text'
__module_version__ = '0.1'
__module_description__ = 'Inverts your text!'
__module_author__ = 'Jake0720, with a little help from Liam Stanley'

import xchat

help = '\x02\x0303Type /flip <message> then press enter to make it backwards.'

print('\x02\x0303%s has been loaded.' % __module_name__)

def flip(word, word_eol, userdata):
    try:
        xchat.command('say %s' % word_eol[1][::-1])
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('\x02\x0303%s has been unloaded.' % __module_name__)

xchat.hook_command('flip', flip, help=help)
xchat.hook_unload(onUnload)
