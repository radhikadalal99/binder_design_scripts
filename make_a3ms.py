#!/usr/bin/env python
# This script takes an MPNN output and makes the first half of the needed A3M file

import os
import sys

def get_chain_seq(inputfile, targetseq):
    seqdict = {}
    index = 0
    title = inputfile.split('.')[0]
    with open(inputfile) as f:
        for line in f:
            if not line.startswith(">"):
                seq = line.strip()
                title_new = f"/wynton/scratch/rdalal/241008_mpnn_redes/mpnn_submit/a3ms/{title}_{index}.a3m"
                seqdict[title_new] = (seq + targetseq, seq)
                index += 1
    return seqdict

def makenewfastafile(seqdict):
    dashes = "-" * 300
    for filename, (seq_combined, original_seq) in seqdict.items():
        with open(filename, 'w') as f:
            f.write("#87,256\t1,1\n>101\t102\n")
            f.write(seq_combined + "\n")
            f.write(">101\n")
            f.write(original_seq + dashes + "\n")
            for k in range(1, 6):
                f.write(f">{k}\n")
                f.write(original_seq + dashes + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: script.py <inputfile> <targetseq>")
        sys.exit(1)

    inputfile = sys.argv[1]
    targetseq = sys.argv[2]
    
    seqdict = get_chain_seq(inputfile, targetseq)
    makenewfastafile(seqdict)

if __name__ == "__main__":
    main()
