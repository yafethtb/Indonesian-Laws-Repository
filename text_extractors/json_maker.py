# Second change: September 16th, 2022

import json
from sys import argv

# File name
filename = argv[1]

# Initiate dictionaries
uu_dict = dict()
pasal_dict = dict()

# Load text
try:
    with open(filename, 'r', encoding= "utf-8") as raw_file:
        content = raw_file.readlines()
        content_text = ''.join(content)
        split_content_text = content_text.split('~')

    # Initiate dictionaries content variables
    nomor = split_content_text[0].split('|')[0].strip()
    nama = split_content_text[0].split('|')[1].strip()
    isi = pasal_dict

    # Populate Parent Dictionary
    uu_dict['nomor_uu'] = nomor
    uu_dict['tentang'] = nama
    uu_dict['isi'] = pasal_dict

    # Populate Child Dictionary
    for sentences in split_content_text[1:]:
        sentence = sentences.strip()    
        pasal, isi = sentence.split('|')
        ayat = isi.split('#')[1:]
        pasal_dict[pasal] = ayat

    with open(argv[2], 'w') as json_uu:
        json.dump(uu_dict, json_uu, indent= 4) # Add indentation to JSON
        
except ValueError as e:
    print(e)

else:
    # Dump parent dictionary to JSON
        print('DONE!')
