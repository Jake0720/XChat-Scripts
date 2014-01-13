__module_name__ = 'Color List'
__module_version__ = '0.2'
__module_description__ = 'Lists the available colors.'
__module_author__ = 'Jake0720'

import xchat

c = '\x02\x0303'
help = 'Type /colors to see a list of colors.'

def bar(max,colors,sign=False):
    if not sign:
        symbol = '#'
    else:
        symbol = sign
    bar = max*symbol
    print bar
    # Now, loop over each item in the list, and pad accordingly
    sort_colors = [x for x in colors.iteritems()]
    sort_colors.sort(key=lambda x: x[1])
    for key, id in sort_colors:
        data = str.center('\x02\x03{id}{color}\x03 | {id}\x02'.format(color=key, id=id), max+4)
        print '%s%s%s' % (symbol, data, symbol)
    print bar



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
    #try:
    bar(20, colors,'+') # Keep in mind, first integer needs to be even
    #except:
    #    xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('colors', color_list, help=help)
xchat.hook_unload(onUnload)

print('%s%s has been loaded.' % (c, __module_name__))
