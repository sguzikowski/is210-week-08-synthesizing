#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things"""


import decimal


NAME = raw_input('What is your name? ')
LOAN = raw_input('What is the principal of the loan? ')
YEARS = raw_input('How many years is this loan being borrowed? ')
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

LOAN = int(LOAN)
YEARS = int(YEARS)
 
n = 12
r = None
if 0 <= LOAN <= 199999:
	if QUALIFIED == 'y' or QUALIFIED == 'Yes':
		r = 0.0363 if 1 <= YEARS <= 15 else 0.0404 \
		if 16 <= YEARS <= 20 else 0.0577 if 21 <= YEARS <= 30 else None
	elif QUALIFIED == 'n' or QUALIFIED == 'No':
		r = 0.0465 if 1 <= YEARS <= 15 else 0.0498 \
		if 16 <= YEARS <= 20 else 0.0639 if 21 <= YEARS <= 30 else None
elif 200000 <= LOAN <= 999999:
	if QUALIFIED == 'y' or QUALIFIED == 'Yes':
		r = 0.0302 if 1 <= YEARS <= 15 else 0.0327 \
		if 16 <= YEARS <= 20 else 0.0466 if 21 <= YEARS <= 30 else None
	elif QUALIFIED == 'n' or QUALIFIED == 'No':
		r = 0.0398 if 1 <= YEARS <= 15 else 0.0408 \
		if 16 <= YEARS <= 20 else None
elif LOAN >= 1000000: 
	if QUALIFIED == 'y' or QUALIFIED == 'Yes':
		 r = 0.0205 if 1 <= YEARS <= 15 else 0.0262 \
		 if 16 <= YEARS <= 20 else None
TOTAL = round(LOAN * ((1 + decimal.Decimal(r/12)) ** (12 * YEARS))) \
if r != None else None

TOTAL = '{:,}'.format(TOTAL)
TOTAL = str(TOTAL)
TOTAL = TOTAL[:-2]
TOTAL = '$' + TOTAL

LOAN = '{:,}'.format(LOAN)
LOAN = str(LOAN)
YEARS = str(YEARS)
TOTAL = str(TOTAL)

LOAN = '$' + LOAN
LINE = '-' * 69
ALIST = [(len(LOAN)), (len(YEARS)), (len(QUALIFIED)), (len(TOTAL))]
alignment = max(ALIST)
alignment = int(alignment)

REPORT = (' Loan report for: {} \n'
					+  '{}'  + '\n'
					+ 'Principal:      ' + '{}'.rjust(alignment) + '\n'
					+ 'Duration:             ' + '{}'.rjust(alignment) + '\n' 
					+ 'Pre-Qualified?:        ' + '{}'.rjust(alignment) + '\n' 
					+ '\n' 
					+ 'Total:                ' + TOTAL.rjust(alignment)).format(NAME, LINE, LOAN, YEARS, QUALIFIED)
print REPORT
