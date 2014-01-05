__module_name__ = 'Greeting'
__module_version__ = '0.1'
__module_description__ = 'Greets a user that has currently joined the designated channels.'
__module_author__ = 'Jake0720'

import xchat

c = '\x0312'
def on_join(word, word_eol, userdata):
    #Add the channels you want to greet people in here, inbetween the ' marks. Example: channels = ['#Jake','#Example']
    #You can add as many channels that you'd like by adding a comma then another set of quotes
    channels = ['','',''] 
    nick, channel = word[0], word[1]
    destination = xchat.get_context()
    if channel in channels:
        destination.command('say Hello %s, welcome to %s!' % (nick, channel))
    else:
        return

def onUnload(userdata):
    xchat.prnt('%s%s, version: %s, has been unloaded.' % (c, __module_name__, __module_version__))
    
xchat.hook_print('Join', on_join)
xchat.hook_unload(onUnload)
print('%s%s, version: %s, has been loaded.' % (c, __module_name__, __module_version__))
