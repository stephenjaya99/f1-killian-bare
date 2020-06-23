import csv
import logging

logger = logging.getLogger(__name__)


class CSVParser(object):

    def __init__(self, col_name_to_start):
        self.col_name_to_start = col_name_to_start

    def get_row_number_of_col_names(self):
        first_col_name = self.col_name_to_start
        with open(self.filepath, 'rU') as tsv:
            reader = csv.reader(tsv, delimiter=',', quotechar='"')
            for row in reader:
                if first_col_name in row:
                    return int(reader.line_num)
        raise ValueError(
            "Doesn\'t have first column that contains `" + first_col_name + "`")

    def prepare(self, filepath):
        '''
        Preparing data that's required by our main function
        eg. setting up filepath, ignore row, etc
        This function should not validate data
        '''
        self.filepath = filepath
        self.ignore_first_x_row = self.get_row_number_of_col_names()

    def get_col_names(self):
        row_number_of_col_names = self.get_row_number_of_col_names()
        with open(self.filepath, 'rU') as tsv:
            reader = csv.reader(tsv, delimiter=',', quotechar='"')
            for row in reader:
                if reader.line_num == row_number_of_col_names:
                    return row

    def get_col_values(self, row):
        col_names = self.get_col_names()
        return dict(zip(col_names, row))

    def convert_instance_to_json(self, filename):
        count = 0
        instances = []

        self.prepare(filename)
        with open(filename, 'rU') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            for row in reader:
                count = reader.line_num
                if (count > self.ignore_first_x_row):
                    row_values = self.get_col_values(row)
                    instances.append(row_values)

        return instances
