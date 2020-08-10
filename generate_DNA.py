#!/usr/bin/env python3

import random

repeat4 = 'atca'  
repeat10 =  'tcatg' * 2 
repeat12 = 'tatg' * 3

def generate_DNA(N, alphabet=['A','C','G','T',repeat4,repeat10, repeat12]):
   """
        * Description: generate DNA sequence from ATCG and reapeats
        * N: Is the number of random sampling
        * alphabet: is a list of ['A','C','G','T',repeat4,repeat10, repeat12]
        * return: DNA sequence with upper and lower cases
   """
  return(''.join([random.choice(alphabet) for i in range(N)]))
