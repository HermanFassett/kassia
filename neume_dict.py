#!/usr/bin/python
import re

def translate(text):
    splitText = text.split(" ")
    tmpText = [ezPsaltica[t] if ezPsaltica.has_key(t) else t for t in splitText]
    # might need to add in a str replace for two vareia in a row
    return u''.join(tmpText)
     
def takesLyric(neume):
    if neume in neumesWithLyrics:
        return True
    else:
        return False
        
def standAlone(neume):
    if neume in standAloneNeumes:
        return True
    else:
        return False

def chunkNeumes(neumeText):
    """Breaks neumeArray into logical chunks based on whether a linebreak
    can occur between them"""
    neumeArray = neumeText.split(' ')
    chunkArray = []   
    i = 0
    while(i < len(neumeArray)):
        # Grab next neume
        chunk = neumeArray[i]
        # Add more neumes to chunk like fthora, ison, etc
        j = 1
        if (i+1) < len(neumeArray):
            while((not standAlone(neumeArray[i+j])) and (neumeArray[i+j] != "\\")):
                chunk += " " + neumeArray[i+j]
                j += 1
                if (i+j >= len(neumeArray)):
                    print "At the end!"
                    break
        i += j
        chunkArray.append(chunk)
        # Check if we're at the end of the array
        if i >= len(neumeArray):
            break
        
        
    return chunkArray
     
ezPsaltica = {
    #' ' : u'\uF020',
    '0' : u'\uF030',
    'p' : u'\uF070',
    '1' : u'\uF031',
    '2' : u'\uF032',
    '3' : u'\uF033',
    '4' : u'\uF034',
    '5' : u'\uF035',
    '6' : u'\uF036',
    '7' : u'\uF037',
    '8' : u'\uF038',
    '9' : u'\uF039',
    '`' : u'\uF060',
    '~' : u'\uF07E',
    '=' : u'\uF03D',
    'q' : u'\uF071',
    'w' : u'\uF077',
    'e' : u'\uF065',
    'r' : u'\uF072',
    't' : u'\uF074',
    'y' : u'\uF079',
    'u' : u'\uF075',
    'i' : u'\uF069',
    '!' : u'\uF021',
    '@' : u'\uF040',
    '_' : u'\uF05F',
    ')' : u'\uF029',
    '-' : u'\uF02D',
    '#' : u'\uF023',
    '$' : u'\uF024',
    '%' : u'\uF025',
    '^' : u'\uF05E',
    '&' : u'\uF026',
    '*' : u'\uF02A',
    '(' : u'\uF028',
    'Q' : u'\uF051',
    'W' : u'\uF057',
    'E' : u'\uF045',
    'O' : u'\uF04F',
    'o' : u'\uF0CE',
    'l' : u'\uF06C',
    'L' : u'\uF04C',
    'P' : u'\uF050',
    'I' : u'\uF049',
    'U' : u'\uF055',
    'Y' : u'\uF059',
    'T' : u'\uF054',
    'R' : u'\uF052',
    'S' : u'\uF053',
    's' : u'\uF073',
    'x' : u'\uF078',
    'X' : u'\uF058',
    'h' : u'\uF068',
    'H' : u'\uF048',
    'd' : u'\uF064',
    'D' : u'\uF044',
    'f' : u'\uF066',
    'F' : u'\uF046',
    'g' : u'\uF067',
    'G' : u'\uF047',
    ';' : u'\uF03B',
    ':' : u'\uF03A',
    'k' : u'\uF06B',
    'K' : u'\uF04B',
    'a' : u'\uF061',
    'A' : u'\uF041',
    'z' : u'\uF091',
    'Z' : u'\uF07A', # or maybe \uf091
    '\\' : u'\uF05C',
    '\'' : u'\uF027',
    '"' : u'\uF022',
    '}' : u'\uF07D',
    '[' : u'\uF07B', # this and next could be switched
    '{' : u'\uF05B',
    ']' : u'\uF05D',
    'J' : u'\uF04A',
    'j' : u'\uF06A',
 #   '' : u'', # place holder for CtrlAlt-C character
    'c' : u'\uF063',
    'v' : u'\uF076',
    'b' : u'\uF062',
    'n' : u'\uF06E',
    'm' : u'\uF06D',
    ',' : u'\uF02C',
    '.' : u'\uF02E',
    '/' : u'\uF02F',
    '+' : u'\uF02B',
#    '' : u'', # Place holder for Alt 0186
    '|' : u'\uF07C',
    'C' : u'\uF043',
    'V' : u'\uF056',
    'B' : u'\uF042',
    'N' : u'\uF04E',
    'M' : u'\uF04D',
    '>' : u'\uF03E',
    '?' : u'\uF03F',
    '<' : u'\uF03C'}
    
neumesWithLyrics = ['0','p','1','2','3','4','5','6','7','8','9','`','=','q','w','e','r',
              't','y','u','i','!','@','_',')','-','#','#','%','^','&','*','(','Q',
              'W','E','O','o','l','L','P','I','U','Y','T','R']
              
standAloneNeumes = ['0','p','1','2','3','4','5','6','7','8','9','`','=','q','w','e','r',
              't','y','u','i','!','@','_',')','-','#','#','%','^','&','*','(','Q','\\'
              'W','E','O','o','l','L','P','I','U','Y','T','R','|','c','v','b','n','m',',','.']