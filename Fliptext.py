__module_name__ = 'Backwards Text'
__module_version__ = '0.1'
__module_description__ = 'Turns your text backwards.'
__module_author__ = 'Jake0720, with a little help from Liam Stanley'

import xchat
import utils

help = utils.bold('Type /btext <message> then press enter to make it backwards.')
print('%s has been loaded.' % utils.bold(__module_name__))

def flip(word, word_eol, userdata):
    try:
        xchat.command('say %s' % word_eol[1][::-1])
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s has been unloaded.' % utils.bold(__module_name__))

xchat.hook_command('btext', flip, help=help)
xchat.hook_unload(onUnload)
