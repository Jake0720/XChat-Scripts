__module_name__ = 'Random Kick Plugin'
__module_version__ = '0.2'
__module_description__ = 'Kicks the designated user with a random kick reason, or a random user and kick reason.'
__module_author__ = 'Jake0720 with help from Liam Stanley'

import xchat
from random import choice as select

c = '\x02\x0303'
help = '%sType /rkick [nick] - to kick [user] with a random reason. ' % c + \
       'Exclude the user to kick a random user, with a reason!'

print('%s%s has been loaded.' % (c, __module_name__))

def rkick(word, word_eol, userdata):
    #try:
    reason = select((
                     'Goodbye!','See you later.','Cya.','Bye.','Later!',
                     'Kindergarden is elsewhere!','Ugh. BYE!','G\'day',
                     'Seeya later!','Be gone!','This is awkward. Bye.',
                     'I didn\'t do it!'
                    ))
    if len(word) == 2:
        # Assume they supplied a username
        return xchat.command('kick %s %s' % (word[1], reason))
    elif len(word) == 1:
        # Assume they want a random user
        list = xchat.get_list("users") 
        if not list:
            return xchat.prnt(help)
        user = select((list))
        return xchat.command('kick %s %s' % (user.nick, reason))
    else:
        # Assume they entered some weird stuff
        return xchat.prnt(help)
    #except:
    #    xchat.prnt(help)
    
    return xchat.EAT_ALL

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('rkick', rkick, help=help)
xchat.hook_unload(onUnload)
