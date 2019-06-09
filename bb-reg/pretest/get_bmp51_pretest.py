#!/usr/bin/python


import numpy as np
pdbs = ['1fep', '2fcp', '1kmo', '1nqe', '1xkw', '2mpr', '1a0s', '2omf', '2por', '1prn', '1e54', '2o4v', '2f1c', '1t16', '1qd6', '1uyn', '1k24', '1i78', '1bxw', '1qj8', '1p4t', '2f1t', '1thq', '1tly', '2erv', '2lhf', '2mlh', '2qdz', '2vqi', '2wjr', '2ynk', '3aeh', '3bs0', '3csl', '3dwo', '3dzm', '3fid', '3kvn', '3rbh', '3rfz', '3syb', '3szv', '3v8x', '3vzt', '4c00', '4e1s', '4gey', '4pr7', '4q35', '4n75']#, '3emn']


import sys

if len(sys.argv)<2:
	print 'Usage :', sys.argv[0], '<max_strand_len>'
	print 'No max_strand_len provided, using default value 12'
	sys.argv.append(12)

maxlen = int(sys.argv[1])
with open('bmp51_len'+str(maxlen).zfill(2)+'.pretest','w') as f:
	for pdb in pdbs:
		f.write(pdb)
		strands = np.loadtxt('../inputs/'+pdb+'/'+pdb+'.strands').astype(int)
		for i in range(len(strands)):
			if i%2==0:
				start = strands[i][0]
				end = start+maxlen-1
				if end > strands[i][1]:
					end = strands[i][1]

			else:
				end = strands[i][1]
				start = end-maxlen+1
				if start < strands[i][0]:
					start = strands[i][0]
			f.write(' '+str(start)+' '+str(end))
		f.write('\n')
