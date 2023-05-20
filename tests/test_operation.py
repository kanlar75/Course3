def test_get_date(obj_full_attributes):
    assert obj_full_attributes.get_date() == "2019-07-03T18:35:29.512364"


def test_get_description(obj_full_attributes):
    assert obj_full_attributes.get_description() == "Перевод организации"


def test_get_state(obj_full_attributes):
    assert obj_full_attributes.get_state() == "EXECUTED"


def test_get_from_full(obj_full_attributes):
    assert obj_full_attributes.get_from() == "MasterCard 7158300734726758"


def test_get_from_no_full(obj_no_full_attributes):
    assert obj_no_full_attributes.get_from() == ""


def test_get_to(obj_full_attributes):
    assert obj_full_attributes.get_to() == "Счет 35383033474447895560"
