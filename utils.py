#!/usr/bin/env python

'''Python script that must be kept with all of these plugins'''

def color(color, message):
    '''color forground/background encoding IRC messages'''
    
    colors = {'white': '00', 'black': '01', 'blue': '02', 'navy': '02',
              'green': '03', 'red': '04', 'brown': '05', 'maroon': '05',
              'purple': '06', 'orange': '07', 'olive': '07', 'gold': '07',
              'yellow': '08', 'lightgreen': '09', 'lime': '09', 'teal': '10',
              'cyan': '11', 'lightblue': '12', 'royal': '12', 'lightpurple': '13',
              'pink': '13', 'fuchsia': '13', 'grey': '14', 'lightgrey': '0', 'silver': '0'}
    color = str(color).lower()
    message = str(message)
    if '/' in color:
        color = color.split('/')
        message = '\x03' + colors[color[0]] + ',' + colors[color[1]] + message + '\x03'
    else: 
        message = '\x03' + colors[color] + message + '\x03'
        return message

def bold(message):
    '''bold encoding IRC messages'''
    return ('\x02' + str(message) + '\x02')

def italic(message):
    '''italicize encoding IRC messages'''
    return ('\x16' + str(message) + '\x16')

def underline(message):
    '''underlined encoding IRC messages'''
    return ('\x1f' + str(message) + '\x1f')
