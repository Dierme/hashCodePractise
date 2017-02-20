class TaskReader(object):

    def __init__(self, filepath):

        self.__filepath = filepath

        parseResult = self.__parse_file()

        self.__rows = parseResult['rows']

        self.__cols = parseResult['cols']

        self.__min = parseResult['min']

        self.__max = parseResult['max']

        self.__matrix = self.compose_matrix(parseResult['matrix'])

    def __parse_file(self):
        file = open(self.__filepath, 'r')

        first_line = file.readline().strip().split(' ')

        matrix_unformated = file.readlines()

        parse_result = {
            'rows' : first_line[0],
            'cols' : first_line[1],
            'min'  : first_line[2],
            'max'  : first_line[3],
            'matrix': matrix_unformated
        }

        return parse_result

    def compose_matrix(self, matrix_str):

        rows = int(self.get_rows())
        cols = int(self.get_cols())

        matrix = [[0 for x in range(cols)] for y in range(rows)]

        matrix_formatted = []

        for col in matrix_str:
            matrix_formatted.append(col.strip())

        for x, col in enumerate(matrix_formatted):
            for y, letter in enumerate(col):
                matrix[x][y] = letter

        return matrix

    def get_matrix(self):
        return self.__matrix

    def get_min(self):
        return self.__min

    def get_max(self):
        return self.__max

    def get_rows(self):
        return self.__rows

    def get_cols(self):
        return self.__cols
