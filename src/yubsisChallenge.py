#!/usr/bin/env python3

def yubsisChallenge(dna, minimum = 9):

  longest_motif = longestMotif(dna)
  print("> Longest motif: " + str(longest_motif))
  print("> Number of repeated longest motif WITHOUT overlapping: " + str(dna.upper().count(longest_motif)) + str(" With: " +   str(len(longest_motif)) + " bp"))
  print("> Number of repeated longest motif WITH overlapping: " + str(count_substring(dna,longest_motif)))
  
  motifs = allRepeatedMotifs(dna=dna ,minimum=minimum, maximum=len(longest_motif)+1)
  return(motifs)
  
  # Driver Code 
  if __name__ == "__main__":
     random.seed(10)
     dna = generate_DNA(1000).upper()
     return(yubsisChallenge(dna, minimum = 9))
