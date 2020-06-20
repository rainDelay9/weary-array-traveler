import pytest
from weary import WearyGraph


######################################################
###################### UTILS #########################
######################################################

def true_path(s):
    graph = WearyGraph(s)
    assert graph.has_path() is True


def false_path(s):
    graph = WearyGraph(s)
    assert graph.has_path() is False


def to_json_str(s):
    return "[" + s + "]"


def to_tsv(s):
    return s.replace(",", "\t")


def all_formats(test, s):
    test(s)
    test(to_tsv(s))
    test(to_json_str(s))


######################################################
###################### PATHS #########################
######################################################

def test_good_graph():
    all_formats(true_path, "4, 4, 1, 1, 2, 2, 1000, 1")


def test_bad_graph():
    all_formats(false_path, "4, 2, 1, 3, 2, 2, 1000, 1")


def test_starts_with_zero():
    all_formats(false_path, "0, 1")


def test_empty_string():
    all_formats(true_path, "")


def test_single_number():
    all_formats(true_path, "2")


HUGE_NUMBER = "9999999999999999999999999999999999999999999999999999999999999999999999999999"


def test_huge_number():
    all_formats(true_path, "1" + HUGE_NUMBER)


########################################################
##################### Exceptions #######################
########################################################

def all_throws(s):
    with pytest.raises(ValueError):
        WearyGraph(s)
    with pytest.raises(ValueError):
        WearyGraph(to_tsv(s))
    with pytest.raises(ValueError):
        WearyGraph(to_json_str(s))


def test_throws_two_delims():
    all_throws("1,,2")


def test_throws_end_with_delim():
    all_throws("1,")


def test_throws_negative_number():
    all_throws("1,-2")