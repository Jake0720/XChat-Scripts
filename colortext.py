__module_name__ = 'Color Text'
__module_version__ = '0.1'
__module_description__ = 'Another way to type in colors, if you find it more difficult with Ctrl + K. (Only works for one color)'
__module_author__ = 'Jake0720'

import xchat

p = '\x0313'
br = '\x0305'
v = '\x0306'
nb = '\x0302'
a = '\x0311'
y = '\x0308'
dg = '\x0314'
rb = '\x0312'
b = '\x0301'
t = '\x0310'
o = '\x0307'
g = '\x0303'
w = '\x0316'
lg = '\x0315'
lmg = '\x0309'
r = '\x0304'
help = ('To use, type %s/c <color abbreviation> <message>\x0f.\n' % rb +
        'The colors are:\n' +
        '%sb = Black\n' % b +
        '%snb = Navy Blue\n' % nb +
        '%sg = Green\n' % g +
        '%sr = Red\n' % r +
        '%sbr = Brown\n' % br +
        '%sv = Violet/Purple\n' % v +
        '%so = Olive/Gold\n' % o +
        '%sy = Yellow\n' % y +
        '%slmg = Lime Green\n' % lmg +
        '%st = Teal\n' % t +
        '%sa = Aqua\n' % a +
        '%srb = Royal Blue\n' % rb +
        '%sp = Pink\n' % p +
        '%sdg = Dark Gray\n' % dg +
        '%slg = Light Gray\n' % lg +
        '%sw = White' % w)

def coloredChat(word, word_eol, userdata):
    if word[1].lower() == 'b':
        return xchat.command('say %s%s' % (b, word_eol[2]))
    elif word[1].lower() == 'nb':
        return xchat.command('say %s%s' % (nb, word_eol[2]))
    elif word[1].lower() == 'g':
        return xchat.command('say %s%s' % (g, word_eol[2]))
    elif word[1].lower() == 'r':
        return xchat.command('say %s%s' % (r, word_eol[2]))
    elif word[1].lower() == 'br':
        return xchat.command('say %s%s' % (br, word_eol[2]))
    elif word[1].lower() == 'v':
        return xchat.command('say %s%s' % (v, word_eol[2]))
    elif word[1].lower() == 'o':
        return xchat.command('say %s%s' % (o, word_eol[2]))
    elif word[1].lower() == 'y':
        return xchat.command('say %s%s' % (y, word_eol[2]))
    elif word[1].lower() == 'lmg':
        return xchat.command('say %s%s' % (lmg, word_eol[2]))
    elif word[1].lower() == 't':
        return xchat.command('say %s%s' % (t, word_eol[2]))
    elif word[1].lower() == 'a':
        return xchat.command('say %s%s' % (a, word_eol[2]))
    elif word[1].lower() == 'rb':
        return xchat.command('say %s%s' % (rb, word_eol[2]))
    elif word[1].lower() == 'p':
        return xchat.command('say %s%s' % (p, word_eol[2]))
    elif word[1].lower() == 'dg':
        return xchat.command('say %s%s' % (dg, word_eol[2]))
    elif word[1].lower() == 'lg':
        return xchat.command('say %s%s' % (lg, word_eol[2]))
    elif word[1].lower()== 'w':
        return xchat.command('say %s%s' % (w, word_eol[2]))
    else:
        return xchat.prnt(help)

def onUnload(userdata):
    xchat.prnt('%s%s has been unloaded.' % (v, __module_name__))

xchat.hook_command('c', coloredChat, help=help)
xchat.hook_unload(onUnload)
print('%s%s has been loaded.' % (v, __module_name__))
