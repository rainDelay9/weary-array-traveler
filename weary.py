import re
import json
from collections import deque
from enum import Enum


class FileType(Enum):
    CSV = 'CSV'
    TSV = 'TSV'
    JSON = 'JSON'


FileTypes = {
    'CSV': FileType.CSV,
    'TSV': FileType.TSV,
    'JSON': FileType.JSON
}


def parse_uint(s):
    num = int(s)
    if num < 0:
        raise ValueError
    return num


def parse_xsv(s, delim):
    if not s:
        return []
    return [parse_uint(x) for x in s.split(delim)]


def parse_csv(s):
    return parse_xsv(s, ',')


def parse_tsv(s):
    return parse_xsv(s, '\t')


def parse_json(s):
    parsed = json.loads(s)
    if not all(isinstance(x, int) and x >= 0 for x in parsed):
        raise ValueError
    return parsed


parsers = {FileType.CSV: parse_csv,
           FileType.TSV: parse_tsv,
           FileType.JSON: parse_json}


def parse_to_graph(s, file_type):
    return parsers[file_type](s)


class WearyGraph:
    def __init__(self, arr_str, file_type):

        self.graph = parse_to_graph(arr_str, file_type)

        if self.graph is None:
            raise ValueError

    def __str__(self):
        if len(self.graph) > 20:
            return ("%s" % self.graph[:20])[:-1] + "...]"
        return "%s" % self.graph

    def __repr__(self):
        return self.__str__()

    def has_path(self):
        size = len(self.graph)
        if size <= 1:
            return True

        stack = deque()
        visited = set()
        stack.append(0)

        while len(stack) != 0:
            location = stack.pop()
            visited.add(location)

            forward = location + self.graph[location]
            backward = location - self.graph[location]

            # will we reach the end if we move forward?
            if forward == size - 1:
                return True

            # scan backward coordinate if in bounds
            if backward > 0 and backward not in visited:
                stack.append(backward)

            # scan forward coordinate if in bounds
            if forward < size - 1 and forward not in visited:
                stack.append(forward)

        return False
