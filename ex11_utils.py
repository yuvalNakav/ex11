from typing import List, Tuple, Iterable, Optional

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """

    Making sure that the word exists in dict.txt
    :param board:
    :param path:
    :param words:
    :return:
    """
    word = valid_word(board, path)
    # print("word in  is valid", word)
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
        # print("word", i, word)
        cell = path[i]
        y, x = cell
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and cell not in curr_path:
            if i >= 1:
                # print("i >= 1")
                if not (
                    -1 <= y - path[i - 1][0] <= 1 and -1 <= x - path[i - 1][1] <= 1
                ):
                    # print("not valid")
                    is_valid = False
                    word = None
                    break
                # else:
                #     #print("yes valid")
            word += board[y][x]
            curr_path.add(cell)

        else:
            is_valid = False
            word = None
        i += 1
    return word


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    transford the word to set beacuse we want to run faster,
    :param n:
    :param board:
    :param words:
    :return:
    """
    words_set = set()
    for word in words:
        string = ""
        for letter in word:
            string += letter
            words_set.add(string)
    final_lst = []
    uses_path = []
    inner_lst = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            row, col = i, j
            find_length_n_paths_helper(
                n,
                words_set,
                board,
                row,
                col,
                [(i, j)],
                uses_path + [(row, col)],
                inner_lst,
            )
    # for i in inner_lst:
    #     if is_valid_path(board,i,words):
    #         final_lst.append(i)
    # return (final_lst) == (inner_lst)
    return inner_lst


def make_word_from_path(board, path):
    word = ""
    print(path)
    for cord in path:
        row, col = cord
        word += board[row][col]
    return word


def find_length_n_paths_helper(n, words, board, row, col, path, uses_path, inner_lst):
    """
    in evrey index we  for all travelers
    :param n:
    :param words:
    :param board:
    :param row:
    :param col:
    :param path:
    :param uses_path:
    :param inner_lst:
    :return:
    """
    word = make_word_from_path(board, path)
    # print(word)
    if word:
        if word not in words:
            return
    if (len(path)) == n:
        inner_lst.append(path)
        return
    moves = all_moves(row, col, board, uses_path)
    # print(moves, "this is moves ", ",row=", row, " col=", col)
    for move in moves:
        cur_row = move[0]
        cur_cul = move[1]
        if (cur_row, cur_cul) not in uses_path:
            print(cur_row, cur_cul, " tuple")
            find_length_n_paths_helper(
                n,
                words,
                board,
                cur_row,
                cur_cul,
                path + [(cur_row, cur_cul)],
                uses_path + [(cur_row, cur_cul)],
                inner_lst,
            )
    return


def all_moves(row, col, board, uses_path):
    moves = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if valid_move(board, i, j, uses_path) and ((i, j) != (row, col)):
                moves.append((i, j))
    return moves


def valid_move(board, row, col, uses_path):
    if (
        0 <= col < len(board[0])
        and 0 <= row < len(board)
        and (row, col) not in uses_path
    ):
        return True
    return False


# board = [['Q', 'Q', 'Q', 'Q'],
#          ['B', 'O', 'B', 'Q'],
#          ['Q', 'Q', 'Q', 'Q'],
#          ['Q', 'Q', 'Q', 'Q']]
# word_dict = {'BOB': True}
# expected_1 = [[(1, 0), (1, 1), (1, 2)]]
# expected_2 = [[(1, 2), (1, 1), (1, 0)]]
# actual = find_length_n_paths(3, board, word_dict)
# print(actual)


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    final_lst = []
    uses_path = []
    inner_lst = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            row, col = i, j
            find_length_n_words_helper(
                n,
                words,
                board,
                row,
                col,
                [(i, j)],
                uses_path + [(row, col)],
                inner_lst,
                "" + board[row][col],
            )
    for i in inner_lst:
        # print(i)
        if is_valid_path(board, i, words):
            final_lst.append(i)
    return final_lst


def find_length_n_words_helper(
    n, words, board, row, col, path, uses_path, inner_lst, word
):
    if len(word) == n:
        inner_lst.append(path)
        return
    moves = all_moves(row, col, board, uses_path)
    # print(moves, "this is moves ", ",row=", row, " col=", col)
    for move in moves:
        cur_row = move[0]
        cur_cul = move[1]
        if (cur_row, cur_cul) not in uses_path:
            find_length_n_words_helper(
                n,
                words,
                board,
                cur_row,
                cur_cul,
                path + [(cur_row, cur_cul)],
                uses_path + [(cur_row, cur_cul)],
                inner_lst,
                word + board[cur_row][cur_cul],
            )
    return


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    word_path_dict = dict()
    high_score_path = []
    for cur_length in range(len(board) * len(board[0]), 1, -1):
        path_lst = find_length_n_paths(cur_length, board, words)
        # print(path_lst)
        for path in path_lst:
            print("path_lst:", path_lst)
            print("path", path)
            word = make_word_from_path(board, path)
            if word not in word_path_dict and word in words:
                word_path_dict.update({word: path})
    for key in word_path_dict:
        high_score_path.append(word_path_dict[key])
    return high_score_path
