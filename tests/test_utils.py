from unittest.mock import mock_open, patch

from src.utils import currency_conversion, read_json_file

@patch("os.path.exists")
def test_read_json_file(mock_os) -> None:
    mock_os.return_value = True
    with patch("builtins.open", mock_open(read_data='{"1":"2"}')):
        assert read_json_file("a") == {"1":"2"}
    assert read_json_file("") == []


def test_currency_conversion() -> None:
    with patch("requests.get") as r_mock:
        r_mock.return_value.json.return_value = {"result": 111}
        assert (
            currency_conversion(
                [{"operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}}}]
            )
            == 111
        )
        assert (
            currency_conversion(
                [{"operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}}}]
            )
            == 79114.93
        )
