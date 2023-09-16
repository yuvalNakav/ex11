with open("boggle_dict.txt", "r") as txt_file:
    words = [word.split("\n")[0] for word in txt_file.readlines()]

# print(len(words))


def check_valid_next_press(curr_cell, next_cell):
    if curr_cell:
        return -1 <= curr_cell.row - next_cell.row <= 1 and -1 <= curr_cell.column - next_cell.column <= 1
    return True


def check_word_validity(word, path):
    if len(path) >= 3:
        print(word.get())
        return word.get() in words
    else:
        return False
