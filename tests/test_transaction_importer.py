from unittest.mock import patch, Mock
from src.transaction_importer import reading_operations_from_csv, reading_operations_from_excel


@patch("pandas.read_csv")
def test_reading_operations_from_csv(mock_read_csv) -> None:
    fake_dataframe = Mock()
    fake_dataframe.to_dict.return_value = [
        {
            'PassengerId': "1, 2, 3, 4, 5",
            'Survived': "0, 1, 1, 1, 0"
        }
]

    mock_read_csv.return_value = fake_dataframe
    data_from_csv = reading_operations_from_csv("test.csv")
    assert data_from_csv == fake_dataframe.to_dict.return_value


@patch("pandas.read_excel")
def test_reading_operations_from_excel(mock_read_excel) -> None:
    fake_dataframe = Mock()
    fake_dataframe.to_dict.return_value = [
        {
            'PassengerId': "1, 2, 3, 4, 5",
            'Survived': "0, 1, 1, 1, 0"
        }
    ]

    mock_read_excel.return_value = fake_dataframe
    data_from_excel = reading_operations_from_excel("test.excel")
    assert data_from_excel == fake_dataframe.to_dict.return_value
