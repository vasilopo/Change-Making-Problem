# Dependencies
import yaml


def parse_yaml(path):
    # Function that parses a yaml file
    # into a python dictionary

    # Args:
    #   path: path to the yaml file

    with open(path) as f:

        return yaml.load(f, Loader=yaml.FullLoader)

