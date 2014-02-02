__module_name__ = 'Chuck Norris'
__module_version__ = '0.2'
__module_description__ = 'Prints a chuck norris fact in chat.'
__module_author__ = 'Jacob with help from Liam Stanley'

import xchat
import json
import urllib2
import HTMLParser

c = '\x0312'
help = 'To use, type \x0312/cn\x0f.'
h = HTMLParser.HTMLParser()

def cn(word, word_eol, userdata):
        try:
            a = urllib2.urlopen('http://api.icndb.com/jokes/random').read()
        except:
            return xchat.prnt(help)
        data = json.loads(a)
        xchat.command('say %s' % h.unescape(data['value']['joke']))

def onUnload(userdata):
        xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))

xchat.hook_command('cn',cn,help=help)
xchat.hook_unload(onUnload)
print('%s%s has been loaded.' % (c, __module_name__))
