import json
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
