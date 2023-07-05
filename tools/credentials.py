import os
from tools.helpers import Helpers


class Credentials(Helpers):

    def __init__(self):
        self.PATH = os.path.join(os.path.dirname(__file__), '..', 'configuration', 'env_credentials.yaml')

    def get_credentials(self, ENV):
        credentials = self.read_yaml(self.PATH)
        return credentials[ENV]
