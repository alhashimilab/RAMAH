#!/usr/bin/python

from pdblib.base import *

mol = Mol('A2DNA_bform.pdb')

reses = getreses(mol)
for res in reses:
    if res.name == 'DA':
        res.name = 'ADE'
    elif res.name == 'DT':
        res.name = 'THY'
    elif res.name == 'DC':
        res.name = 'CYT'
    elif res.name == 'DG':
        res.name = 'GUA'
   # elif res.name == 'RG5'
   #     res.name = 'G'
   # elif res.name == 'RC3'
   #     res.name = 'C'

mol.renumber(1, 1)
mol.segs[0].chid = ' '
#mol.segs[1].chid = ' '
mol.write('A2DNA_bform_new.pdb')
