import os


class Config(object):
    def __init__(self):
        self.data_folder = 'backend/data'
        self.word_curve = os.path.join(self.data_folder, 'all_word_sim_new.csv')


CONFIG = Config()
