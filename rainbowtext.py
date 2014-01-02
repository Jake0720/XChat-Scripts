import xchat as hexchat
import itertools
import re

__module_name__ = 'Rainbows'
__module_version__ = '1.0'
__module_description__ = 'Turns your text into a colorful mess.'

hexchat.prnt('Rainbows script loaded')
fabhelp = 'To use, type \x0309/fab <message>\x0f, and the message will be rainbowfied.'
fab2help = 'To use, type \x0309/fab2 <message>\x0f, and the message will be rainbowfied, but with random background colors. (Hard to read.)'
enfabhelp = 'To use, type \x0309/enfab\x0f. This will make all of your text rainbowfied, without having to type /fab over and over again.'
defabhelp = 'To use, type \x0309/defab\x0f. This turns /enfab off. See: \x0309/help enfab\x0f.'
spoilerhelp = 'To use, type \x0309/spoiler <message>\x0f. This will make your text hidden with random background colors. To reveal your message, highlight the text.'

colors = itertools.cycle((
        ('05', '10'),
        ('04', '12'),
        ('07', '02'),
        ('08', '06'),
        ('09', '13'),
        ('03', '15'),
        ('11', '14'),
        ('10', '05'),
        ('12', '04'),
        ('02', '07'),
        ('06', '08'),
        ('13', '09'),
        ('15', '03'),
        ('14', '11'),
))

fab_hook = None
in_fab_hook = False

color_code_regex = re.compile(r'(?:(?:{0}\d\d?(?:,\d\d?)?))'.format('\003'))
color_code_or_regular_character_regex = re.compile(r'((?:{0}\d\d?(?:,\d\d?)?)|.)'.format('\003'))

def fab_callback(word, word_eol, user_data):
        global in_fab_hook
        
        in_fab_hook = True
        hexchat.command(
                'say {0}'.format(
                        ' '.join(
                                ''.join(
                                        add_color(c) for c in color_code_or_regular_character_regex.split(w) if c
                                ) for w in word_eol[1].split(' ')
                        )
                )
        )
        in_fab_hook = False
        
        return hexchat.EAT_ALL

def fab2_callback(word, word_eol, user_data):
        global in_fab_hook
        
        in_fab_hook = True
        hexchat.command(
                'say {0}'.format(
                        ''.join(
                                add_color_and_background_color(c) for c in color_code_or_regular_character_regex.split(word_eol[1]) if c
                        )
                )
        )
        in_fab_hook = False
        
        return hexchat.EAT_ALL

def spoiler_callback(word, word_eol, user_data):
        hexchat.command(
                'say {0}'.format(
                        ''.join(
                                add_spoiler_color(c) for c in color_code_or_regular_character_regex.split(word_eol[1]) if c
                        )
                )
        )
        
        return hexchat.EAT_ALL

def add_color(character):
        if color_code_regex.match(character):
                return character
        else:
                next_color, _ = next(colors)
                return '\003{0}{1}'.format(next_color, character)

def add_color_and_background_color(character):
        if color_code_regex.match(character):
                return character
        else:
                next_color, next_bg_color = next(colors)
                return '\003{0},{1}{2}'.format(next_color, next_bg_color, character)

def add_spoiler_color(character):
        if color_code_regex.match(character):
                return character
        else:
                next_color, _ = next(colors)
                return '\003{0},{0}{1}'.format(next_color, character)

def enfab_callback(word, word_eol, user_data):
        global fab_hook
        
        if fab_hook is None:
                fab_hook = hexchat.hook_command('', fab_passthru_callback)
                hexchat.prnt('Fabulous mode on')
        
        return hexchat.EAT_ALL

def defab_callback(word, word_eol, user_data):
        global fab_hook
        
        if fab_hook is not None:
                hexchat.unhook(fab_hook)
                fab_hook = None
                hexchat.prnt('Fabulous mode off')
        
        return hexchat.EAT_ALL

def fab_passthru_callback(word, word_eol, user_data):
        global in_fab_hook
        
        if in_fab_hook:
                return hexchat.EAT_NONE
        else:
                hexchat.command('fab {0}'.format(word_eol[0]))
                
                return hexchat.EAT_ALL
def onUnload(userdata):
        hexchat.prnt('%s has been unloaded.' % __module_name__)

hexchat.hook_command('fab', fab_callback, help=fabhelp)
hexchat.hook_command('fab2', fab2_callback, help=fab2help)
hexchat.hook_command('spoiler', spoiler_callback, help=spoilerhelp)
hexchat.hook_command('enfab', enfab_callback, help=enfabhelp)
hexchat.hook_command('defab', defab_callback, help=defabhelp)
hexchat.hook_unload(onUnload)
