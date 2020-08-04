import pytest
from data_import import location

def test1():
    starting_string = "Cruel, Unusual & Pointless in Newville, Pennsylvania"
    result_string = "Newville, Pennsylvania"
    assert(location([starting_string]) == [result_string])