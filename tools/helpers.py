import yaml
import re


class Helpers:

    def read_yaml(self, file_path):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    def convert_string_to_camel_case(self, word):
        word = re.sub("[$@&]", "", word)
        word = re.sub(r"(_|-)+", " ", word).title().replace(" ", "")
        return ''.join([word[0], word[1:]])
