from typing import List, Tuple, Iterable, Optional
from tqdm import tqdm

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


def is_valid_move(x: int, y: int, board: Board, visited: List[List[bool]]) -> bool:
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    def _find_length_helper(x: int, y: int, path: Path):
        visited[x][y] = True
        path.append((x, y))
        current_word = "".join([board[i][j] for i, j in path])
        if len(path) == n and current_word in words:
            valid_paths.append(path[:])

        if len(path) < n:
            for delta_x in [-1, 0, 1]:
                for delta_y in [-1, 0, 1]:
                    new_x, new_y = x + delta_x, y + delta_y
                    if is_valid_move(new_x, new_y, board, visited):
                        _find_length_helper(new_x, new_y, path)

        path.pop()
        visited[x][y] = False

    valid_paths = []
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            _find_length_helper(i, j, [])

    return valid_paths


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:

    def _find_length_helper(x: int, y: int, path: Path):
        visited[x][y] = True
        path.append((x, y))
        current_word = "".join([board[i][j] for i, j in path])
        if len(current_word) == n and current_word in words:
            valid_paths.append(path[:])

        if len(current_word) < n:
            for delta_x in [-1, 0, 1]:
                for delta_y in [-1, 0, 1]:
                    new_x, new_y = x + delta_x, y + delta_y
                    if is_valid_move(new_x, new_y, board, visited):
                        _find_length_helper(new_x, new_y, path)

        path.pop()
        visited[x][y] = False

    valid_paths = []
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            _find_length_helper(i, j, [])

    return valid_paths


# def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
#     paths_list = []
#     for word in words:
#         curr_path = []
#         max_len = 0
#         for path in find_length_n_words(len(word), board, words):
#             if len(path) > max_len:
#                 max_len = len(path)
#                 curr_path = path
#         if len(curr_path) > 0:
#             paths_list.append(curr_path)
#     return paths_list


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    def is_valid_word(word, word_set):
        return word in word_set

    def is_near_path(x: int, y: int, path: Path, max_distance: int = 2):
        # Check if the position (x, y) is within max_distance of any position in the path
        for px, py in tqdm(path, colour="blue"):
            if abs(px - x) <= max_distance and abs(py - y) <= max_distance:
                return True
        return False

    def _find_length_helper(x: int, y: int, path: Path, word_length: int):
        visited[x][y] = True
        path.append((x, y))
        current_word = "".join([board[i][j] for i, j in path])

        if len(current_word) == word_length and is_valid_word(current_word, word_set):
            valid_paths.append(path[:])
            return

        if len(current_word) >= word_length:
            return

        for delta_x in [-1, 0, 1]:
            for delta_y in [-1, 0, 1]:
                new_x, new_y = x + delta_x, y + delta_y
                if is_valid_move(new_x, new_y, board, visited) and is_near_path(new_x, new_y, path):
                    _find_length_helper(new_x, new_y, path, word_length)

        path.pop()
        visited[x][y] = False

    word_set = set(words)  # Convert the list of words to a set for efficient lookup
    valid_paths = []
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    max_score_paths = []

    for word in tqdm(words, colour="green"):
        max_length = 0
        temp_path = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                _find_length_helper(i, j, [], len(word))
                if len(valid_paths) > 0:
                    path_length = len(valid_paths[0])
                    if path_length > max_length:
                        max_length = path_length
                        temp_path = valid_paths[0]
                valid_paths.clear()

        if len(temp_path) > 0:
            max_score_paths.append(temp_path)

    return max_score_paths