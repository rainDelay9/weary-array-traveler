import re
import json
from stack import Stack


def parse_uint(s):
    num = int(s)
    if num < 0:
        raise ValueError
    return num


def parse_xsv(s, delim):
    if len(s) == 0:
        return []
    return [parse_uint(x) for x in s.split(delim)]


def construct_list_regex(start, delim, end):
    return r"^" + start + "((\d)+(" + delim + "\d+)*)?" + end + "$"


TSV_REGEX = construct_list_regex("", "\t", "")
CSV_REGEX = construct_list_regex("", ",", "")
JSON_REGEX = construct_list_regex("\[", ",", "\]")


def parse_to_graph(s):

    graph = None

    rx = re.compile('([\n\r ])')
    stripped = rx.sub('', s)

    if re.search(TSV_REGEX, stripped) is not None:
        graph = parse_xsv(stripped, '\t')
    elif re.search(CSV_REGEX, stripped) is not None:
        graph = parse_xsv(stripped, ',')
    elif re.search(JSON_REGEX, stripped) is not None:
        graph = json.loads(stripped)

    return graph


class WearyGraph:
    def __init__(self, str):

        self.graph = parse_to_graph(str)

        if self.graph is None:
            raise ValueError

    def __str__(self):
        return "%s" % self.graph

    def __repr__(self):
        return self.__str__()

    def has_path(self):
        size = len(self.graph)
        if size <= 1:
            return True

        stack = Stack()
        visited = set()
        stack.push(0)

        while len(stack) != 0:
            location = stack.pop()
            visited.add(location)
            step = self.graph[location]

            forward = location + step
            backward = location - step

            # will we reach the end if we move forward?
            if forward == size - 1:
                return True

            # scan backward coordinate if in bounds
            if backward > 0 and backward not in visited:
                stack.push(backward)

            # scan forward coordinate if in bounds
            if forward < size - 1 and forward not in visited:
                stack.push(forward)

        return False
