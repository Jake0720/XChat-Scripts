__module_name__ = "Hexchat Hug Plugin"
__module_version__ = "0.2"
__module_description__ = "Hug command"
__module_author__ = "Jake0720"

import xchat as XC
import random

def hugs(word, word_eol, userdata):
    x = (("a nice warm hug","a nice warm cuddle","Don't forget to add more!"))
    try:
        XC.command('me ' + 'gives ' + '\002'+word[1]+'\002 ' + random.choice(x))
    except:
        print 'error'

XC.hook_command("hug", hugs)
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
