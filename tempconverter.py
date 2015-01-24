__module_name__ = 'Temperature Converter'
__module_version__ = '0.1'
__module_description__ = 'This script is used to convert Fahrenheit to Celsius, and vise versa.'
__module_author__ = 'Jake0720'

import hexchat

help = 'Syntax: \x0304/convert <f or c> <integer>\x0f, or to announce it, \x0304/convert <f or c> announce <integer>.'

def Converter(word, word_eol, userdata):
    if word < 3:
        hexchat.prnt(help)
    elif word[2] == 'announce':
        if word[1] == 'c':
            x = float(word[3])
            y = ((x-32)*.5556)
            hexchat.command(u'say \x0312{0}\u00B0F\x0f to \x0312Celsius\x0f: \x0304{1}'.encode('utf-8').format(word[3], y))
        elif word[1] == 'f':
            x = float(word[3])
            y = ((x/.5556)+32)
            hexchat.command(u'say \x0312{0}\u00B0C\x0f to \x0312Fahrenheit\x0f: \x0304{1}'.encode('utf-8').format(word[3], y))
        else:
            return 'Error'
    elif word[2] != 'announce':
        if word[1] == 'c':
            x = float(word[2])
            y = ((x - 32)*.5556)
            hexchat.prnt(u'\x0312{0}\u00B0F\x0f to \x0312Celsius\x0f: \x0304{1}'.encode('utf-8').format(word[2], y))
        elif word[1] == 'f':
            x = float(word[2])
            y = ((x/.5556)+32)
            hexchat.prnt(u'\x0312{0}\u00B0C\x0f to \x0312Fahrenheit\x0f: \x0304{1}'.encode('utf-8').format(word[2], y))
        else:
            return 'Error'
    else:
        return 'Error'
    return hexchat.EAT_ALL

def unload(userdata):
    hexchat.prnt('\x0304{0} has been unloaded.'.format(__module_name__))

hexchat.hook_command('convert', Converter, help)
hexchat.hook_unload(unload)
print '\x0312{0} has been loaded.'.format(__module_name__)
