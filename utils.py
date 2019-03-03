import re
import os
import glob

path = 'data/Full_text'  # TODO get path so command line arguments can be parsed from working directory


def get_directory():
    pass

def get_year(filename):
    regex = r'(\.\d{4})'
    date = re.search(regex, filename).group(0)
    return date

def year_regex(year):
    return r"\w{{3,13}}.({}).b{{1}}[0-9]{{8}}.txt".format(year)

def files_for_year(path, year):
    regex = r"\w{{3,13}}.({}).b{{1}}[0-9]{{8}}.txt".format(year)
    res = [f for f in os.listdir(path) if re.search(regex, f)]
    return res

def files_for_bourough(path, borough):
    """:return text file names for bourough"""
    res = [f for f in os.listdir(path) if re.search(borough, f)]
    return sorted(res)

def read_files_for_year(path, year):
    text = ''
    files = files_for_year(path, year)
    for file in files:
         with open(os.path.join(path, file)) as file_in:
                for line in file_in:
                    text = text + line
    return text


def all_files():
    files = sorted([f for f in glob.glob(os.path.join(path, '*'))])
    return files

# TODO 

# add year extraction regex 