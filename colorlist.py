__module_name__ = 'Color List'
__module_version__ = '0.1'
__module_description__ = 'Lists the available colors.'
__module_author__ = 'Jake0720'

import xchat

c = '\x02\x0303'
help = 'Type /colors to see a list of colors.'

def color_list(word, word_eol, userdata):
    colors = {'\x0301Black':'01',
              '\x0302Navy Blue':'02',
              '\x0303Green':'03',
              '\x0304Red':'04',
              '\x0305Brown':'05',
              '\x0306Purple':'06',
              '\x0307Olive':'07',
              '\x0308Yellow':'08',
              '\x0309Lime Green':'09',
              '\x0310Teal':'10',
              '\x0311Aqua':'11',
              '\x0312Royal Blue':'12',
              '\x0313Pink':'13',
              '\x0314Dark Gray':'14',
              '\x0315Light Gray':'15',
              '\x0316White':'16'}
    try:
        xchat.prnt('%s~~~~~~~~~~~~~~~~~' % c)
        
        for key, value in colors.iteritems():
            xchat.prnt('%s | %s' % (key, value))
            
        xchat.prnt('%s~~~~~~~~~~~~~~~~~' % c)
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('colors', color_list, help=help)
xchat.hook_unload(onUnload)

print('%s%s has been loaded.' % (c, __module_name__))
