#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things"""

DAY = raw_input('What day is it? ')
DIGITS = raw_input ('What time is it? ' )

DIGITS = int(DIGITS)

SNOOZE = True if DAY == 'Sat' or DAY == 'Sun' or DIGITS < 600 else False

if SNOOZE is False: 
	print 'Beep! Beep! Beep! Beep! Beep!'