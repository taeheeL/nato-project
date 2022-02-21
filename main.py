import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def converter():
    user_name = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[word] for word in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        converter()
    else:
        print(output_list)

converter()