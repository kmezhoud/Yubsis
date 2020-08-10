#!/usr/bin/env python3

from collections import Counter as cntr 
import pandas as pd

def allRepeatedMotifs(dna, minimum, maximum):
  """
     * Description: Find all repeated motifs
     * dna: DNA sequence
     * minimum: minimum length of motifs
     * maximum: maximum length for motifs
  """
 
    # insure that DNA in upper cases
    dna = dna.upper()
    maximum = maximum # longest motif with at less two repeats 
    minimum = minimum  # the minimum length of motif is 9 bp
    start = timeit.default_timer()
    substrs = cntr() 
    for n in range(minimum,maximum): # look from 9 to 41 bp
      for i in range(0,len(dna)-n):  # loop for counter
        substrs[dna[i:i+n]] += 1 
    motifs = substrs#.most_common

    stop = timeit.default_timer()
    print('> Get all repeated substring: ', round(stop - start, 3), "s") 

    # Convert to dict
    d = dict(motifs)
    start = timeit.default_timer()
    # filter only repeats at less twice
    # sort by motif length decreasing
    d = dict((k, v) for k, v in sorted(d.items(), key=lambda item: len(item[0]),reverse = True) if v >= 2)
    # Sort by value decreasing
    #d = dict((k, v) for k, v in sorted(d.items(), key=lambda item: item[1],reverse = True) if v >= 2)
    stop = timeit.default_timer()
    print('> Filter and sort motifs with at less two repeats: ', round(stop - start, 3), "s") 


    start = timeit.default_timer()

    ls = []
    # reformat output
    #for key, value in d.items():
    #    print(key, len(str(key)) ,value)

    for key, value in d.items():
        temp = [key,len(str(key))]
        ls.append(temp)

    stop = timeit.default_timer()
    print('> Reformating dictionary to list, include length of motifs (bp): ', round(stop - start,3), "s") 
    print("> At all there are: ", len(ls), " motifs, with at less two repeats.")
    #print("> Print motifs, length , repeats: ", *ls[1:20], sep = "\n")

    return(ls)
