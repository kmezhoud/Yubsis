#!/usr/bin/env python3
  # """
  #     * Description: Count occurence with overlapping
  #     * string: alphabetic sequence with upper and/or lower cases
  #     * sub_string: alphabetic motif with upper cases
  #     
  # """


def count_substring(string,sub_string):
    # Insure if string and sub_string are in upper cases
    string = string.upper()
    sub_string = sub_string.upper()
    
    l=len(sub_string)
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):
            count+=1
    return count
