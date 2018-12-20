#!/usr/bin/python

from pdblib.base import *

err = 2.0
mol = Mol('./A2DNA_bform_new.pdb')
dic = {'ADE': [["C1'","H1'"],["C4'","H4'"],["",""],["C2","H2"],["C8","H8"],["",""]],
       'GUA': [["C1'","H1'"],["C4'","H4'"],["",""],["",""],["C8","H8"],["N1","H1"]],
       'CYT': [["C1'","H1'"],["C4'","H4'"],["C5","H5"],["",""],["C6","H6"],["",""]],
       'THY': [["C1'","H1'"],["C4'","H4'"],["",""],["",""],["C6","H6"],["N3","H3"]],
       'URA': [["C1'","H1'"],["C4'","H4'"],["C5","H5"],["",""],["C6","H6"],["N3","H3"]]}

f = open('A2DNA_test.inp','wt')
f.write('SVD Input\n')
f.write('Field:  600\n')

for x in range(0,5):
    for res in getreses(mol):
        resn = res.name
        i = res.resi
        pairs = dic[resn][x]
        if pairs[0] == "":
            continue
        else:
            f.write('%s   %-3s %3d  %-3s %3d %6.1f %3d %4.1f\n'%
                ('D',pairs[0],i,pairs[1],i,0.0,1,err))
f.close()

