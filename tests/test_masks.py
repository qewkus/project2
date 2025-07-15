import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_longer():
    with pytest.raises(ValueError):
        get_mask_account("736541084301358743052354")


def test_get_mask_account_shorted():
    with pytest.raises(ValueError):
        get_mask_account("736541084301")


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** ****6361"


def test_get_mask_card_number_longer():
    with pytest.raises(ValueError):
        get_mask_card_number("736541084301358743052354")


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_shorted():
    with pytest.raises(ValueError):
        get_mask_card_number("736541084301")










