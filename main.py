import pandas as pd


with open("nato_phonetic_alphabet.csv") as npa_file:
    npa = pd.read_csv(npa_file)


npa_dictionary = {}
pa_list = []

for(index, row) in npa.iterrows():
    npa_dictionary.update({row.letter: row.code})

content = input("Insert a word:\n")

content_list = [letter for letter in content.upper()]

for element in content_list:
    if element in npa_dictionary:
        pa_list.append(npa_dictionary[element])



print(content)
print(pa_list)