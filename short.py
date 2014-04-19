__module_name__ = 'Short'
__module_version__ = '1.0'
__module_description__ = 'Auto link shortener with http://links.ml'
__module_author__ = 'Liam Stanley'

import xchat
import urllib, re

c = '\x0304'
help = ("/short <url|enable|disable>\n"
        " - url: url/link that you would like to be shortened. E.g, http://liamstanley.io\n"
        " - enable: Enable the auto conversion of links that you enter in the input box.\n"
        "           Remember, only correct URLs will be converted, and links in commands\n"
        "           will be ignored.\n"
        " - disable: Disable the auto conversion of URLs that are entered in the input box.\n"
        " [NOTE]: Use your notepad enter key to sent text without conversion, temporarily.")

def post(query):
    data = urllib.urlencode(query)
    u = urllib.urlopen('http://links.ml/submit', data)
    bytes = u.read()
    u.close()
    return bytes

def shorten(url):
    try:
        data = post({'api': True, 'link': url})
        if 'bad request' in data.lower(): return
        return data
    except: return

def send_message(word, word_eol, userdata):
    """Gets the inputbox's text, replace URL's with shortened URLs.

    This function is called every time a key is pressed. It will stop if that
    key isn't Enter or if the input box is empty.

    KP_Return (keypad Enter key) is ignored, and can be used if you don't want
    a URL to be shortened.
    """
    if not prefs('get'):
        return
    if not(word[0] == "65293"): return
    msg = xchat.get_info('inputbox')
    if msg is None: return
    if msg.startswith('/'): return
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg)
    if not urls: return
    for url in urls:
        try:
            data = shorten(url)
            if not data: continue
            msg = msg.replace(url, str(data))
        except: continue
    xchat.command("settext %s" % msg)
    
    return xchat.EAT_ALL

def short(word, word_eol, userdata):
    """shortens the url passed as an arguement."""
    try:
        if len(word) == 1:
            return xchat.prnt(help)
        if word_eol[1].lower() in ['on', 'enable', 'true']:
            prefs('put', 'on')
            return
        elif word_eol[1].lower() in ['off', 'disable', 'false']:
            prefs('put', 'off')
            return
        else:
            url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word_eol[1])
            if not url: return xchat.prnt(help)
            url = url[0]
            data = shorten(url)
            if not data: return xchat.prnt(help)
            new = word_eol[1].replace(url, str(data))
            xchat.command('say %s' % new)
    except:
        xchat.prnt(help)
        
    return xchat.EAT_ALL

def prefs(job, args=None):
    """Saves|Gets preferences."""
    if job == 'get':
        status = xchat.get_pluginpref("shorten_status")

        # Get data from database
        if not status: return True
        else:
            if status == 'on': return True
            else: return False
    if job == 'put' and args:
        xchat.set_pluginpref("shorten_status", args)
        xchat.prnt("Preferences saved.")

def onUnload(userdata):
        xchat.prnt('%s%s has been unloaded.' % (c, __module_name__))


xchat.hook_print('Key Press', send_message)
xchat.hook_command("short", short, help=help)
xchat.hook_unload(onUnload)
print('%s%s Version %s has been loaded.' % (c, __module_name__, __module_version__))
