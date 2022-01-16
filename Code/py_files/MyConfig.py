import json


class MyConfig:
    def __init__(self):
        self.content = dict()
        self.metadata = dict()
        self.steps = dict()

    def load_data_by_path(self, path):
        self.content = self.__read_json(path)
        self.to_segments()
        self.merge_parts()

    @staticmethod
    def __read_json(path):
        data = {}
        with open(path, "r") as read_file:
            data = json.load(read_file)
        return data

    def to_segments(self):
        # form steps dict (without description) and metadata dict (without steps)
        self.metadata = self.content.copy()
        self.steps = self.metadata['configurations']['steps'].copy()
        self.steps.pop('description')
        self.metadata['configurations'].pop('steps')

    def merge_parts(self):
        """
        :return: dictionary formed during the program operation
        """
        data = self.metadata.copy()
        data['configurations'].update(self.steps.copy())
        return data
