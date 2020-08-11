#!/usr/bin/env python3

  # """    
  #        * Description: Find the Longest motif with at less 2 repeats: avoid overlapping motifs 
  #        * dna: a sequence of ATCG bp
  #        * return: string
  # """

def longestMotif(dna):  

    # unsure if DNA is in upper Cases
    dna = dna.upper()
    n = len(dna) 
    motif = [[0 for x in range(n + 1)]  
                for y in range(n + 1)] 
  
    longest_motif = "" # To store result 
    longest_motif_length = 0 # To store length of result 
  
    # building table in bottom-up manner 
    index = 0
    for i in range(1, n + 1): 
        for j in range(i + 1, n + 1): 
              
            # (j-i) > motif[i-1][j-1] to remove 
            # overlapping 
            if (dna[i - 1] == dna[j - 1] and
                motif[i - 1][j - 1] < (j - i)): 
                motif[i][j] = motif[i - 1][j - 1] + 1
  
                # updating maximum length of the 
                # motif and updating the finishing 
                # index of the suffix 
                if (motif[i][j] > longest_motif_length): 
                    longest_motif_length = motif[i][j] 
                    index = max(i, index) 
                  
            else: 
                motif[i][j] = 0
  
    # If we have non-empty motif, then insert  
    # all bps from first bp to  
    # last bpof motif 
    if (longest_motif_length > 0): 
        for i in range(index - longest_motif_length + 1, 
                                    index + 1): 
            longest_motif = longest_motif + dna[i - 1] 
  
    return longest_motif 
