# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:10:17 2020

@author: Eier
"""



 #!python
 # -*- coding: utf-8 -*-
# passord:Aas19922020IaKh
 
__author__ = 'Ilham Daher Ahmad'
__email__ = 'ilham.daher.ahmad@nmbu.no'



def letter_freq(txt):
    txt=txt.lower()
    i = list(txt)
 
    d= {}
    for n in i:
        if n not in d.keys():
            d[n]= 0
        d[n]= d[n]+1
    return d

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
