__module_name__ = 'Color List'
__module_version__ = '0.1'
__module_description__ = 'Lists the available colors.'
__module_author__ = 'Jake0720'

import xchat

c = '\x02\x0303'
help = 'Type /colors to see a list of colors.'

def color_list(word, word_eol, userdata):
    colors = {'Black':'01',
              'Navy Blue':'02',
              'Green':'03',
              'Red':'04',
              'Brown':'05',
              'Purple':'06',
              'Olive':'07',
              'Yellow':'08',
              'Lime Green':'09',
              'Teal':'10',
              'Aqua':'11',
              'Royal Blue':'12',
              'Pink':'13',
              'Dark Gray':'14',
              'Light Gray':'15',
              'White':'16'}
    try:
        xchat.prnt('%s~~~~~~~~~~~~~~~~~' % c)
        
        for key, value in colors.iteritems():
            xchat.prnt('\x02\x03{id}{key}\x03 | {id}'.format(id=value, key=key))
            
        xchat.prnt('%s~~~~~~~~~~~~~~~~~' % c)
    except:
        xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('colors', color_list, help=help)
xchat.hook_unload(onUnload)

print('%s%s has been loaded.' % (c, __module_name__))
