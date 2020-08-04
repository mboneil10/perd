import pytest
from data_import import location

def test1():
    # This one currently fails
    starting_string = "Pointless in Newville, Pennsylvania"
    result_string = "Newville, Pennsylvania"
    assert(location([starting_string]) == [result_string])

def test2():
    starting_string = "Tricky in American Fork, Utah"
    result_string = "American Fork, Utah"
    assert (location([starting_string]) == [result_string])

def test3():
    starting_string = "Bonus Episode!"
    result_string = ""
    assert (location([starting_string]) == [result_string])

def test4():
    starting_string = "in Antelope, California - Part: 1"
    result_string = "in Antelope, California"
    assert(location([starting_string]) == [result_string])