__module_name__ = 'Hug Plugin'
__module_version__ = '0.2'
__module_description__ = 'Hug someone with a command!'
__module_author__ = 'Jake0720 with help from Liam Stanley'

import xchat
from random import choice as select

c = '\x02\x0303'
help = '%sType /hug <nick> - to hug the user!' % c
print('%s%s has been loaded.' % (c, __module_name__))

def hug(word, word_eol, userdata):
    response = select((
                       'a nice warm hug','a nice warm cuddle','a bear hug',
                       'a snuggly hug','a huge hug','a hug','a small hug',
                       'a weird hug','an awkward hug'
                       ))
    try:
        xchat.command('me gives \x02%s\x02 %s' % (word[1], response))
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('hug', hug, help=help)
xchat.hook_unload(onUnload)