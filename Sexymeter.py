__module_name__ = "Sexymeter"
__module_version__ = "0.1"
__module_description__ = "Detects your sexiness on a scale from 0 to 100."
__module_author__ = "Jake0720"

import xchat
import random

xchat.prnt(__module_name__+' has been loaded.')

smhelp = 'Type /sm to see your sexiness on a scale from 0 to 100.'

def sm(word, word_eol, userdata):
    sexyness = random.randint(0,100)
    me = word[1]
    if sexyness == 100:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+' \x0309\x02Damn, you\'re so gorgeous you\'re fuckable, '+me+'!'))
    elif sexyness >= 95 and sexyness < 99:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+' \x0309\x02Damn, you\'re super sexy, '+me+'.'))
    elif sexyness >= 80 and sexyness < 95:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Pretty sexy, '+me+'!'))
    elif sexyness >= 65 and sexyness < 80:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Not bad, '+me+'!'))
    elif sexyness >= 50 and sexyness < 65:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Could be better... \x0302@'+me))
    elif sexyness >= 35 and sexyness < 50:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Eh... \x0302@'+me))
    elif sexyness >= 20 and sexyness < 35:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Not so sexy... \x0302@'+me))
    elif sexyness >= 5 and sexyness < 20:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Mirrors have been shattered, '+me+'!'))
    elif sexyness >= 0 and sexyness < 5:
        xchat.command('say '+('\x02SEXY METER: '+'\x0306\x02'+str(sexyness)+'\x034\x02'+' Holy shit, you\'re ugly, '+me+'!'))
    else:
        return

def onUnload(unload):
    xchat.prnt('\x034'+__module_name__+' has been unloaded.')

xchat.hook_command('sm', sm, help=smhelp)
xchat.hook_unload(onUnload)
