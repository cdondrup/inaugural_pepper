import yaml


class Config(object):
    def __init__(self, file_name):
        self.conf = Config.load_file(file_name)

    @staticmethod
    def load_file(file_name):
        with open(file_name, 'r') as f:
            return yaml.load(f)

    @property
    def concepts(self):
        return self.conf["concepts"]

    @property
    def applications(self):
        return self.conf["applications"]

    @property
    def precanned_text(self):
        return self.conf["precanned_text"]
