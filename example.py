import ex11_utils as utils
from typing import *
import ex11_utils

Board = List[List[str]]
Path = List[Tuple[int, int]]
POSSIBLE_MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]


_board = [['L', 'L', 'E', 'N'],
          ['O', 'F', 'E', 'T'],
          ['N', 'E', 'T', 'H'],
          ['N', 'E', 'E', 'QU']]
# path = [(3, 2), (3, 3), (2, 3)]
# _words = []
with open("boggle_dict.txt", "r") as txt_file:
    _words = [word.split("\n")[0] for word in txt_file.readlines()]


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    final_list = []
    for word in words:
        max_for_length = 0
        temp_path = []
        for path in ex11_utils.find_length_n_words(len(word), board, words):
            if len(path) > max_for_length:
                max_for_length = len(path)
                temp_path = path
        if len(temp_path) > 0:
            final_list.append(temp_path)
    return final_list


letters_3 = [word for word in _words if len(word) == 3]

def _valid_side(start: tuple, end: tuple) -> bool:
    """
    " checking for valid side. start and end Coordinates given,
    Along the same row or column, they must be.
    return: True, if valid. False, otherwise."
    """
    if start[0] == end[0]:
        if start[1] - 1 == end[1] or start[1] + 1 == end[1]:
            return True
    elif start[1] == end[1]:
        if start[0] - 1 == end[0] or start[0] + 1 == end[0]:
            return True
    else:
        return False
def _valid_diagonal(start: tuple, end: tuple) -> bool:
    """
    Coordinates are given, start and end.
    Only in diagonal direction, they can be moved.
    return:True if valid. False, otherwise.
    """
    if end[1] == start[1] - 1 and end[0] == start[0] - 1:
        return True
    elif end[1] == start[1] - 1 and end[0] == start[0] + 1:
        return True
    elif end[1] == start[1] + 1 and end[0] == start[0] - 1:
        return True
    elif end[1] == start[1] + 1 and end[0] == start[0] + 1:
        return True
    else:
        return False


def _valid_cord(path: Path, board: Board) -> bool:
    """
    we are checking Boundaries. Coordinates given, in a path.
    Within the allowed range, they must be.
    return: False if invalid. otherwise True .
    """
    if len(path) == 0:
        return False

    for cords in path:
        if cords[0] < 0 or cords[0] >= len(board):
            return False
        if cords[1] < 0 or cords[1] >= len(board[0]):
            return False
    return True
def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    Validity, we are checking . A path and words, given.
    Coordinates must be in a proper sequence.
    Also, formed word must match with any of the given words.
    Return: the word, we will if it is valid. None, otherwise
    """
    if not _valid_cord(path, board):
        return
    word_of_path = ""
    # this part checks if there are no repetition for cords in path
    for ind in range(len(path) - 1):
        if path[ind] in path[ind + 1:] or path[ind] in path[:ind]:
            return
    # this part checks if cords in path has valid location compare to next cord
    for cord_index in range(len(path) - 1):
        if not _valid_side(path[cord_index], path[cord_index + 1]) and not _valid_diagonal(path[cord_index], path[cord_index + 1]):
            return
        word_of_path += board[path[cord_index][0]][path[cord_index][1]]
    word_of_path += board[path[-1][0]][path[-1][1]]
    # if all cords are valid this part checks if the word is legal in dict
    if word_of_path in words:
        return word_of_path
    return


def _next_place(board: Board, place: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    takes a place on the board and figuring out what is the next moves
    possible :param: board: an instance of the Board class representing the current
    state of the game board.
    :param: place: a tuple of two integers representing the current location
    :return: List[Tuple[int, int]]
    """
    final_lst = []
    for cord in POSSIBLE_MOVES:
        if _valid_cord([(place[0]+cord[0], place[1]+cord[1])], board):
            if _valid_diagonal(place, (place[0] + cord[0],place[1] + cord[1])):
                    final_lst.append((place[0]+cord[0], place[1]+cord[1]))
            if _valid_side(place, (place[0]+cord[0], place[1]+cord[1])):
                    final_lst.append((place[0]+cord[0], place[1]+cord[1]))
    return final_lst


def _set_partial_all_words(words):
    """
    This function takes a list of words and creates a set of all possible
    substrings of those words
    :param words: words valid for boggle game
    :return: set of all possible substring
    """
    set_final = set()
    for word in words:
        str_temp = ""
        for let in word:
            str_temp += let
            set_final.add(str_temp)
    return set_final


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    finding all the valid paths on the board representing a word with n cells
    :param n: the num of wanted cells
    :param board:Board
    :param words:iterable with strings as valid words
    :return:List[Path]
    """
    set_partial = _set_partial_all_words(words)
    if n == 0 or len(board) == 0:
        return []
    lst_final = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            cord = (row, col)
            _find_n_length_helper(n, board, words, lst_final, [cord],set_partial)
    return lst_final



def _find_n_length_helper(n: int, board: Board, words: Iterable[str],lst_final: List, lst_one_cord: List, set_partial: set) -> None:

    """
    helper to backtrack on all the possible n lengths
    :param n: num of wanted cells
    :param board:Board
    :param words:iterable strings
    :param lst_final:list of all paths
    :param lst_one_cord:the last cord of building path
    :param set_partial:set of all partial words
    :return:None
    """
    if len(lst_one_cord) == n:
        if is_valid_path(board, lst_one_cord, words):
            lst_final.append(lst_one_cord)
        return
    if _cord_to_letter(lst_one_cord, board) not in set_partial:
        return
    now_cord = lst_one_cord[-1]
    for move in _next_place(board, now_cord):
        if move in lst_one_cord:
            continue
        _find_n_length_helper(n, board, words, lst_final,lst_one_cord + [move], set_partial)
    return


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    finding all the valid paths on the board representing a word with cells
    that when joining them it will give a valid word
    :param n: n represent the length of the word
    :param board:Board
    :param words:iterable string
    :return:List of list with tuples representing path on board
    """
    set_partial = _set_partial_all_words(words)
    if n == 0 or len(board) == 0:
        return []
    lst_final = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            cord = (row, col)
            _find_n_word_length_helper(n, board, words, lst_final, [cord], set_partial)
    return lst_final


def _cord_to_letter(path, board):
    """
    giving a path of cords it will join them to a word,
    helping to n word function
    :param path:list of tuples
    :param board:Board
    :return:str
    """
    final_word = ""
    for cord in path:
        final_word += board[cord[0]][cord[1]]
    return final_word


def _find_n_word_length_helper(n: int, board: Board, words: Iterable[str], lst_final: List[Tuple[int, int]],lst_one_cord,set_partial_words: set) -> None:
    """
    A helper function for finding words of a specific length (n) on a given Boggle board.
    :param n: the length of the words being searched for
    :param board: the Boggle board to search on
    :param words: a list of valid words to search for
    :param lst_final: a list to store the valid paths found
    :param lst_one_cord: the current path being searched for
    :param set_partial_words: a set of partial words that can be formed by the current path
    :return: None
    """
    if _char_in_lst(lst_one_cord, board) == n:
        if is_valid_path(board, lst_one_cord, words):
            lst_final.append(lst_one_cord)
        return
    if _cord_to_letter(lst_one_cord, board) not in set_partial_words:
        return
    now_cord = lst_one_cord[-1]
    for move in _next_place(board, now_cord):
        if move in lst_one_cord:
            continue
        _find_n_word_length_helper(n, board, words, lst_final, lst_one_cord + [move], set_partial_words)
    return


def _char_in_lst(lst, board):
    """
    Counts the number of characters in a path on a Boggle board.
    :param lst: a list of coordinates in the form of tuples (x, y)
    :param board: a 2D list representing a Boggle board
    :return: the number of characters in the path
    """
    counter = 0
    for char in lst:
        counter += len(board[char[0]][char[1]])
    return counter


if __name__ == '__main__':
    # us = ex11_utils.find_length_n_paths(3, board, _words)
    # us2 = ex11_utils.find_length_n_words(3, board, _words)
    # his = find_length_n_paths(3, board, _words)
    # his2 = find_length_n_words(3, board, _words)
    # us = max_score_paths(board, _words)
    his = ex11_utils.max_score_paths(_board, _words)
    # print("us", len(us), us)
    # print("us2", len(us2), us2)
    print("his", len(his), his)
    # print("his2", len(his2), his2)
