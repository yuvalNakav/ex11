from typing import *

Board = List[List[str]]
Path = List[Tuple[int, int]]


def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    Checks if the path is valid, this function checks if the path represent a word in the board and if
    the word in the words collection
    :param board: Game board
    :param path: The current path that given as parameter
    :param words: Given collection of words
    :return:  The word represented by the path or None if the word is None or not is the words collection
    """
    word = valid_word(board, path)
    if word:
        if word in words:
            return word
        else:
            return None
    else:
        return None


def valid_word(board: Board, path: Path):
    """
    Making sure that all items in path are legal, which are within the boundaries of the board
    Making sure that the moves in the path are legal
    Making sure we don't go back to the same index on the board
    :param board: Game board
    :param path: The current path that given as parameter
    :return: The word represented by the path or None
    """
    if len(path) == 0:
        return None
    word = ""
    is_valid = True
    i = 0
    curr_path = set()
    while is_valid and i < len(path):
        cell = path[i]
        y , x = cell
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and cell not in curr_path:
            #check the move of second index onwards relative to the previous one if not valid it will break loop
            if i >= 1:
                if not(-1 <= y - path[i-1][0] <= 1 and -1 <= x - path[i-1][1] <= 1):
                    word = None
                    break
            word += board[y][x]
            curr_path.add(cell)

        else:
            is_valid = False
            word = None
        i += 1
    return word


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    Returning all valid paths in n size by:
    creating a words set because it's a more efficient runtime
    Running on nested loops on every coordinate and call for the helper that check all possible moves for that coordinate
    Running on the paths and making sure they are valid
    :param n: represents the length of the routes
    :param board: game board
    :param words: given collection of words
    :return: all valid paths in n size
    """
    n_paths_lst = []
    uses_path = []
    inner_lst = []
    words_set = set()
    for word in words:
        reconnect_word = ""
        for letter in word:
            reconnect_word += letter
            words_set.add(reconnect_word)
    for i in range(len(board)):
        for j in range (len(board[0])):
            row,col = i,j
            # Sending the helper with the current coordinate to initialize the path with starting position
            find_length_n_paths_helper(n,words_set,board,row,col,[(i,j)],uses_path+[(row,col)],inner_lst)
    for i in inner_lst:
        if is_valid_path(board,i,words):
            n_paths_lst.append(i)
    return n_paths_lst


def create_word(board, path):
    """
    Create a word from a given path
    :param board: game board
    :param path: given path
    :return: Word represented by the path
    """
    curr_word = ""
    for index in path:
        row , col = index
        curr_word += board[row][col]
    return curr_word


def find_length_n_paths_helper(n,words,board,row,col,path,uses_path,inner_lst):
    """
    Creating a list with all possible moves for current coordinate
    explore recursively every index and checks all possible moves for every new coordinate, backtracking occurs when
    the path not lead to a valid word or it exceeds the desired length and it will backtrack to find other possibilities
    :param n:The size of the path
    :param words:given collection of words
    :param board:game board
    :param row:index of row
    :param col: index of column
    :param path: curr_path
    :param uses_path: what we use until now
    :param inner_lst: list of valid pathes
    :return:  inner list when the path reaches size n
    """
    word= create_word(board,path)
    if word:
        if word not in words:
            return
    if(len(path)) == n:
        inner_lst.append(path)
        return
    moves = all_moves(row,col,board,uses_path)
    for move in moves:
        curr_row = move[0]
        curr_cul = move[1]
        if (curr_row, curr_cul) not in uses_path:
            find_length_n_paths_helper(n,words,board,curr_row,curr_cul,path+[(curr_row,curr_cul)],uses_path +[(curr_row,curr_cul)],inner_lst)
    return


def all_moves(row,col,board,uses_path):
    """
    find all possible moves for a coordinate on the board and checks if its valid, it will be ok if we dont use
    the coordinate already and if we dont use the same coordinate from the start position
    :param row: Initial row
    :param col: Initial column
    :param board: game board
    :param uses_path: all coordinate that we used already in that call
    :return: list of possible moves
    """
    moves = []
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if valid_move(board,i,j,uses_path) and ((i,j) != (row,col)):
                moves.append((i,j))
    return moves


def valid_move(board,row,col,uses_path):
    """
    Checks if the move is valid by checking the board boundaries and coordinates we used
    :param board:game board
    :param row: current row
    :param col: current column
    :param uses_path:all coordinate that we used already in that call
    :return: True if its valid and false otherwise
    """
    if 0<=col<len(board[0]) and 0<=row<len(board) and (row,col) not in uses_path:
        return True
    return False


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    Returning all valid words in n size by:
    Running on nested loops on every coordinate and call for the helper that check all possible moves for that coordinate
    Running on the paths and making sure they are valid and the words are valid
    :param n: represents the length of the word
    :param board: game board
    :param words:given collection of words
    :return: all valid words in n size
    """
    n_words_lst = []
    uses_path = []
    inner_lst = []
    for i in range(len(board)):
        for j in range (len(board[0])):
            row,col = i,j
            # Sending the helper with the a list that holds the current word and saves it for the run
            find_length_n_words_helper(n,words,board,row,col,[(i,j)],uses_path+[(row,col)],inner_lst,""+board[row][col])
    for i in inner_lst:
        if is_valid_path(board,i,words):
            n_words_lst.append(i)
    return n_words_lst


def find_length_n_words_helper(n,words,board,row,col,path,uses_path,inner_lst,word):
    """
    explore recursively every index and checks all possible moves for every new coordinate, backtracking occurs when
    the path not lead to a valid word or it exceeds the desired length and it will backtrack to find other possibilities
    :param n:The size of the word
    :param words:given collection of words
    :param board:game board
    :param row:index of row
    :param col: index of column
    :param path: curr_path
    :param uses_path: what we use until now
    :param inner_lst: list of possible paths
    :param word: A list that holds all the letters we've collected throughout the run
    :return: the inner list
    """
    if len(word) == n:
        inner_lst.append(path)
        return
    moves = all_moves(row, col, board, uses_path)
    for move in moves:
        curr_row = move[0]
        curr_cul = move[1]
        if (curr_row, curr_cul) not in uses_path:
            find_length_n_words_helper(n, words, board, curr_row, curr_cul, path + [(curr_row, curr_cul)],
                                       uses_path + [(curr_row, curr_cul)], inner_lst,word + board[curr_row][curr_cul])
    return


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    """
    Returning  a list of valid paths that provide the maximum score per game for the board and word set by:
    Starting to find possible paths from the longest path to the lowest(the longest is all the possible cells in
    the board),it will check if the word has been here before and if thw word exist in the collection of words,
    if its good it will enter and append to the max_score_path. because its explore from the longest path's first we
    will get all maximum score path in the end.
    :param board: game board
    :param words: given collection of words
    :return: a list(max score path) of valid paths that provide the maximum score per game for the board and word set
    """
    path_word_list = []
    max_score_path = []
    seen_words = set()
    for n in range(len(board) * len(board[0]), 1, -1):
        curr_path_lst = find_length_n_paths(n, board, words)
        for path in curr_path_lst:
            word = create_word(board, path)
            path_word_list.append((path, word))
    for path, word in path_word_list:
        if word not in seen_words and word in words:
            max_score_path.append(path)
            seen_words.add(word)
    return max_score_path