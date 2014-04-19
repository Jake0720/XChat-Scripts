__module_name__ = 'Rock Paper Scissors'
__module_version__ = '0.1'
__module_description__ = 'Play the classic game Rock, Paper, and Scissors.'
__module_author__ = 'Jake0720'

import xchat
from random import randint

c = '\x0312'
print('%s%s has been loaded.' % (c, __module_name__))
help = '-To play, type \x0312/rps (rock/paper/scissors)\x0f.\n-Example:  \x0304/rps rock'

def rps(word, word_eol, userdata):
    a = randint(0,100)
    if a >= 66:
        randomChoice = 'rock'
    elif a >= 33:
        randomChoice = 'scissors'
    elif a >= 0:
        randomChoice = 'paper'
    else:
        return xchat.prnt(help)
    
    answer = 'You chose \x0304%s\x0f and your opponent chose \x0304%s\x0f. ' % (word[1], randomChoice)
    if word[1].lower() == randomChoice: print('%s%sTie!' % (answer, c))
    elif word[1].lower() == 'rock' and randomChoice == 'scissors': print('%s%sYou won!' % (answer, c))
    elif word[1].lower() == 'rock' and randomChoice == 'paper': print('%s%sYou lose!' % (answer, c))
    elif word[1].lower() == 'scissors' and randomChoice == 'paper': print('%s%sYou win!' % (answer, c))
    elif word[1].lower() == 'scissors' and randomChoice == 'rock': print('%s%sYou lose!' % (answer, c))
    elif word[1].lower() == 'paper' and randomChoice == 'rock': print('%s%sYou won!' % (answer, c))
    elif word[1].lower() == 'paper' and randomChoice == 'scissors': print('%s%sYou lose!' % (answer, c))
    else: return xchat.prnt(help)
    
    return xchat.EAT_ALL

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('rps', rps, help=help)
xchat.hook_unload(onUnload)
