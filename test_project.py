import pytest
from project import new_topic, get_day, formatdaily

def main():
    test_new_topic()
    test_get_day()
    test_formatdaily()

def test_new_topic():
    assert new_topic("Physics", "Chemistry") == ["Physics", "Chemistry"]
    assert new_topic("Maths", "Regression") == ["Maths", "Regression"] 


def test_get_day():
    assert get_day(0) == "Monday" 
    assert get_day(3) == "Thursday"

def test_formatdaily():
    assert formatdaily([[], ['Maths', 'Suvats', 'Friday', '2024-11-15', '2024-11-16', '2024-11-22', '2024-12-01', '2024-12-20', ''], ['Maths', 'Deviation', 'Friday', '2024-11-15', '2024-11-16', '2024-11-22', '2024-12-01', '2024-12-20', '']], '2024-11-15' ) == ['Suvats', 'Deviation']
main()