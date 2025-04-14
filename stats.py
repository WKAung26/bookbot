def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        num_words = file_content.split()
        char_count = {}
        for word in file_content:
            character = word.lower()
            if(character in char_count):
                char_count[character] = char_count[character] + 1
            else:
                char_count[character] = 1
    print(f"Found {len(num_words)} total words")
    print_dict(char_count)

def print_dict(data):
    dict_alpha = add_alpha(data)
    dict_alpha_list  = list(dict_alpha.items())
    dict_alpha_list.sort(reverse=True, key=sort_on)
    data3 = dict(dict_alpha_list)
    for x in data3:
        print(f"{x}: {data3.get(x)}")

def sort_on(data):
    return data[1]

def add_alpha(data):
    new_data = {}
    for x in data.keys():
        if (x.isalpha()):
            new_data[x] = data.get(x)
    return new_data




