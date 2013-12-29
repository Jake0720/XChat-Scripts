__module_name__ = 'Color Text'
__module_version__ = '0.2'
__module_description__ = 'Another way to type in colors, if you find it more difficult with Ctrl + K. (Only works for one color)'
__module_author__ = 'Jake0720 with help from the Herpderp monster.'

import xchat

# Color abbreviations
c = {
        'b': ['01', 'Black'], 'nb': ['02', 'Navy Blue'],
        'g': ['03', 'Green'], 'r': ['04', 'Red'],
        'br': ['05', 'Brown'], 'v': ['06', 'Violet/Purple'],
        'o': ['07', 'Olive/Gold'], 'y': ['08', 'Yellow'],
        'lmg': ['09', 'Lime Green'], 't': ['10', 'Teal'],
        'a': ['11', 'Aqua'], 'rb': ['12', 'Royal Blue'],
        'p': ['13', 'Pink'], 'dg': ['14', 'Dark Grey'],
        'lg': ['15', 'Light Grey'], 'w': ['16', 'White']
    }
loadc = '\x03%s' % c['v'][0]
help = 'To use, type \x03%s/c <color abbreviation> <message>\x0f.\nColor abbreviations:\n' % c['rb'][0]
# Here, loop through and make a list
abbr, count = [], 0
for key, value in c.iteritems():
    count += 1
    if count == 4:
        count, ismax = 0, '\n'
    else: ismax = ''
    code, name = value
    abbr.append('{ismax}\x02\x03{code}{key} = {name}'.format(code=code,key=key,name=name,ismax=ismax))
help += ' \x0f| '.join(abbr)


def coloredChat(word, word_eol, userdata):
    # Intead of doing each one manually, we can use try/except to our advantage!
    try:
        if len(word) < 2:
            return xchat.prnt(help)
        color = word[1].lower()
        return xchat.command('say \x03{color}{msg}'.format(color=c[color][0], msg=word_eol[2]))
    except:
        return xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (loadc, __module_name__))

xchat.hook_command('c', coloredChat, help=help)
xchat.hook_unload(onUnload)
print('%s%s has been loaded.' % (loadc, __module_name__))