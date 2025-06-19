#!/usr/bin/python3

import sys

def extract_uniq_ids(filename):
    """Reads the file line by line and returns a list of lines."""
    
    uniqids = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split(',')
                action = words[2].split('=')
                s_action = action[1].rstrip()
                uniqids.append(s_action)
        return(uniqids)

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None

if __name__ == "__main__":
    action_dict = {}
    l_filename = sys.argv[1]

    unique_ids = extract_uniq_ids(l_filename)
 
    for f in unique_ids:
         if f in action_dict:
             action_dict[f] = action_dict[f] + 1
         else:
             action_dict[f] = 1
    
    sorted_items = sorted(action_dict.items(), key=lambda item: item[1], reverse=True)
    i = 0
    for key,val in sorted_items:
        print (key,val)
        i = i+1
        if (i > 1):
            break

        
