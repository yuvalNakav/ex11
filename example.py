import ex11_utils as utils
board = [
    ["D", "C", "B", "A"],

    ["G", "A", "D", "E"],

    ["T", "J", "Y", "T"],

    ["N", "M", "F", "I"]]
# path = [(3, 2), (3, 3), (2, 3)]
words = []
with open("boggle_dict.txt", "r") as txt_file:
    words = [word.split("\n")[0] for word in txt_file.readlines()]

# print(len(words), words)
# print("final",utils.is_valid_path(board, path, ["bed", "fit", "day", "did", "dad", "bad", "dcd"]))
# paths = utils.find_length_n_paths(3, board, words)
paths = utils.find_length_n_words(3, board, words)
# paths = utils.find_length_n_paths(5, board, [word.upper() for word in ["bed", "fit", "day"]])
print("final", len(paths), paths)