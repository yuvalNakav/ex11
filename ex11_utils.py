from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]

POSSIBLE_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """

    Making sure that the word exists in dict.txt
    :param board:
    :param path:
    :param words:
    :return:
    """
    word = valid_word(board, path)
    print("word in  is valid", word)
    if word in words:
        return word
    else:
        return None


def valid_word(board: Board, path: Path):
    """
    Making sure that all items in path are legal (x,y < 4)
    Making sure that the moves in the path are legal
    :param board:
    :param path:
    :return:
    """
    if len(path) == 0:
        return None
    word = ""
    is_valid = True
    i = 0
    curr_path = set()
    while is_valid and i < len(path):
        print("word", i, word)
        cell = path[i]
        y, x = cell
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and cell not in curr_path:
            if i >= 1:
                print("i >= 1")
                if not(-1 <= y - path[i-1][0] <= 1 and -1 <= x - path[i-1][1] <= 1):
                    print("not valid")
                    is_valid = False
                    word = None
                    break
                else:
                    print("yes valid")
            word += board[y][x]
            curr_path.add(cell)

        else:
            is_valid = False
            word = None
        i += 1
    return word


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    Run recursively
    """
    all_paths = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            path = add_cell_to_path(board, n, [], i, j)
            print(path)
            word = convert_path_to_word(path, board)
            print("word", word, "!!!!!")
            # if word in words and path not in all_paths:
            #     print("helloooooo")
            all_paths.append(path)
    return all_paths


# def generate_paths(board: Board, length: int, path: set[Tuple[int, int]], i:int, j:int):
# def generate_paths(board: Board, length: int, path: Path, i: int, j: int, words):

def convert_path_to_word(path, board):
    word = ""
    for cell in path:
        print(cell)
        i,j = cell
        word += board[i][j]
    return word


def add_cell_to_path(board: Board, length: int, path: Path, i: int, j: int):
    if len(path) < length:
        print("hihihi")
        # if valid_word(board, path):
        #     print("hihihi2")
        path.append((i ,j))
        for move in POSSIBLE_MOVES:
            print("!!!!!!", move, path)
            if (0 <= i + move[0] <= len(board) and 0 <= j + move[1] <= len(board)):
                add_cell_to_path(board, length, path, i + move[0], j + move[1])
                # path.pop()
    elif len(path) == length:
        return path
    else:
        return None


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    pass


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
