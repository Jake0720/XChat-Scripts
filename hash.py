__module_name__ = "Hash"
__module_version__ = "0.1"
__module_description__ = "Hash items and messages with Md5, Sha1, Sha256, and Sha512."
__author__ = "Jake0720"

import xchat, hashlib

c = '\x0312'
help = ('%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' % (c) +
        'To type in MD5 hash, type %s/md5 <message>\x0f\n' % (c) +
        'To type in SHA1 hash, type %s/sha1 <message>\x0f\n' % (c) +
        'To type in SHA256 hash, type %s/sha256 <message>\x0f\n' % (c) +
        'To type in SHA512 hash, type %s/sha512 <message>\x0f\n' % (c) +
        '%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' % (c))

def md5(word, word_eol, userdata):
    try:
        md5 = hashlib.md5(word_eol[1]).hexdigest()
        if len(word) == 1:
            xchat.prnt(help)
        xchat.command('say %s' % md5)
    except:
        xchat.prnt(help)
    
    return xchat.EAT_ALL
        
def sha1(word, word_eol, userdata):
    try:
        sha1 = hashlib.sha1(word_eol[1]).hexdigest()
        if len(word) == 1:
            xchat.prnt(help)
        xchat.command('say %s' % sha1)
    except:
        xchat.prnt(help)
        
    return xchat.EAT_ALL

def sha256(word, word_eol, userdata):
    try:
        sha256 = hashlib.sha256(word_eol[1]).hexdigest()
        if len(word) == 1:
            xchat.prnt(help)
        xchat.command('say %s' % sha256)
    except:
        xchat.prnt(help)
        
    return xchat.EAT_ALL

def sha512(word, word_eol, userdata):
    try:
        sha512 = hashlib.sha512(word_eol[1]).hexdigest()
        if len(word) == 1:
            xchat.prnt(help)
        xchat.command('say %s' % sha512)
    except:
        xchat.prnt(help)
        
    return xchat.EAT_ALL

def onUnload(userdata):
    xchat.prnt('%s%s, Version %s has been unloaded.' % (c, __module_name__, __module_version__))
    
xchat.hook_command("md5", md5, help=help)
xchat.hook_command("sha1", sha1, help=help)
xchat.hook_command("sha256", sha256, help=help)
xchat.hook_command("sha512", sha512, help=help)
xchat.hook_unload(onUnload)
print('%s%s Version %s has been loaded.' % (c, __module_name__, __module_version__))
