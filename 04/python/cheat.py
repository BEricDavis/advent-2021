def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


class BingoBoard:
    def __init__(self, list_of_rows):
        self.bingo = False
        self.numbers = flatten(list_of_rows.copy())
        self.crossed = {number: False for number in self.numbers}
        self.rows = list_of_rows.copy()
        self.columns = self.get_columns(list_of_rows.copy())

    def update(self, number):
        self.crossed[number] = True
        self.bingo = self.check_bingo()

    def check_bingo(self):
        return self.check_bingo_rows() or self.check_bingo_columns()

    def check_bingo_rows(self):
        is_bingo_rows = [sum(self.crossed[number] for number in row) == len(row) for row in self.rows]
        return sum(is_bingo_rows) >= 1

    def check_bingo_columns(self):
        is_bingo_columns = [sum(self.crossed[number] for number in column) == len(column) for column in self.columns]
        return sum(is_bingo_columns) >= 1

    def calculate_sum(self):
        return sum([num for num in self.numbers if not self.crossed[num]])

    @staticmethod
    def get_columns(list_of_rows):
        return [[row[j] for row in list_of_rows] for j in range(len(list_of_rows[0]))]


def read_input(file_name) -> list:
    with open(file_name, 'r') as f:
        text = f.readlines()
    return text


def create_boards_from_text(text):
    board_rows = []
    boards = []
    for line in text:
        if line == "\n":
            boards.append(BingoBoard(board_rows))
            board_rows = []
        else:
            board_rows.append([int(i) for i in line.split()])
    boards.append(BingoBoard(board_rows))
    return boards


def update_boards(boards, number):
    for board in boards:
        board.update(number)


def check_one_bingo(boards):
    for board in boards:
        if board.bingo:
            return True
    return False


def check_bingo_number(boards):
    return len([board for board in boards if board.bingo])


def get_boards_no_bingo(boards):
    return [board for board in boards if not board.bingo]


if __name__ == '__main__':
    text = read_input('input.txt')
    bingo_numbers = [int(i) for i in text[0].split(',')]
    boards = create_boards_from_text(text[2:])
    winning_number = 0
    for number in bingo_numbers:
        update_boards(boards, number)
        if check_one_bingo(boards):
            winning_number = number
            break
    #determine score
    for board in boards:
        if board.bingo:
            winning_score = board.calculate_sum()

    print(f"The solution for 4a is {winning_score * winning_number}")

    boards = create_boards_from_text(text[2:])
    winning_number = 0
    last_board = 0
    for number in bingo_numbers:
        update_boards(boards, number)
        number_of_bingos = check_bingo_number(boards)
        if number_of_bingos == (len(boards)-1):
            last_board = get_boards_no_bingo(boards)[0]
        if number_of_bingos == len(boards):
            winning_number = number
            winning_score = last_board.calculate_sum()
            break
    print(f"The solution for 4b is {winning_score * winning_number}")