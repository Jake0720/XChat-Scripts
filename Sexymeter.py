__module_name__ = 'Sexymeter Plugin'
__module_version__ = '0.3'
__module_description__ = 'Detects your sexiness on a scale from 0 to 100.'
__module_author__ = 'Jake0720 with help from Liam Stanley'

import xchat
from random import randint as rand

c = '\x02\x0303'
help = '%sType /sm to see your sexiness on a scale from 0 to 100.' % c
print('%s%s has been loaded.' % (c, __module_name__))


def sexymeter(word, word_eol, userdata):
    sexyness = rand(0,100)
    if len(word) == 2:
        # Assume a username as args
        user = word[1]
    else:
        # Assume only the command, use their name!
        user = xchat.get_info('nick')
    
    # Start comparing!
    if sexyness == 100: r = 'Damn, you\'re so gorgeous you\'re fuckable'
    elif sexyness >= 95: r = 'Damn, you\'re super sexy'
    elif sexyness >= 80: r = 'Pretty sexy'
    elif sexyness == 69: r = 'The ultimate sexiness, '
    elif sexyness >= 65: r = 'Not bad'
    elif sexyness >= 50: r = 'Could be better..'
    elif sexyness >= 35: r = 'Eh..'
    elif sexyness >= 20: r = 'Not soo sexy..'
    elif sexyness >= 5: r = 'Mirrors have been shattered'
    else: r = 'Holy shit, you\'re ugly'
    return xchat.command('say \x02SEXYMETER:\x02 \x0306%s \x0304\x02%s %s' % (str(sexyness) + '%', r, user))
    
    return xchat.EAT_ALL

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('sm', sexymeter, help=help)
xchat.hook_unload(onUnload)
