from project import (
    get_price,
    validate_dates,
    calculate_return,
    calculate_return_1,
    get_price_first_last,
    buy_and_hold
)


def create_test_csv(tmp_path):
    file = tmp_path / "test_stock.csv"

    file.write_text(
        "Date,Price\n"
        "2024-01-01,100\n"
        "2024-01-02,110\n"
        "2024-01-03,90\n"
    )

    return str(file)


def test_get_price(tmp_path):
    stock = create_test_csv(tmp_path)

    assert get_price(stock, "2024-01-01") == 100
    assert get_price(stock, "2024-01-02") == 110


def test_get_price_invalid_date(tmp_path):
    stock = create_test_csv(tmp_path)

    assert get_price(stock, "2024-01-10") is None


def test_validate_dates():
    assert validate_dates("2024-01-01", "2024-01-03") is True


def test_validate_dates_invalid_order():
    assert validate_dates("2024-01-03", "2024-01-01") is False


def test_validate_dates_same_day():
    assert validate_dates("2024-01-01", "2024-01-01") is False


def test_validate_dates_invalid_format():
    assert validate_dates("not-a-date", "2024-01-03") is False


def test_calculate_return():
    assert calculate_return(100, 110) == 10
    assert calculate_return(100, 90) == -10


def test_calculate_return_1(tmp_path):
    stock = create_test_csv(tmp_path)

    assert calculate_return_1(
        stock,
        "2024-01-01",
        "2024-01-02"
    ) == 10


def test_calculate_return_1_invalid_dates(tmp_path):
    stock = create_test_csv(tmp_path)

    assert calculate_return_1(
        stock,
        "2024-01-03",
        "2024-01-01"
    ) == "Invalid Dates. You cannot sell a stock before you buy it."


def test_get_price_first_last(tmp_path):
    stock = create_test_csv(tmp_path)

    assert get_price_first_last(stock) == (100, 90)


def test_buy_and_hold(tmp_path):
    stock = create_test_csv(tmp_path)

    assert buy_and_hold(stock) == -10
