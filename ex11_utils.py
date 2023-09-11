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
    def is_valid_move(x: int, y: int) -> bool:
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]

    def dfs(x: int, y: int, path: Path):
        visited[x][y] = True
        path.append((x, y))
        current_word = "".join([board[i][j] for i, j in path])
        if len(current_word) == n and current_word in words:
            valid_paths.append(path[:])

        if len(current_word) < n:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if is_valid_move(new_x, new_y):
                        dfs(new_x, new_y, path)

        path.pop()
        visited[x][y] = False

    valid_paths = []
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, [])

    return valid_paths

def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    valid_paths = find_length_n_paths(n, board, words)
    return ["".join([board[i][j] for i, j in path]) for path in valid_paths]


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
print("hey")
