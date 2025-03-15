import pytest
from product import Warehouse, BadProductError, BadShelfError, BadIdError

wr = Warehouse()
wr.create("Груз", 1)
wr.create("Гири", 2)
wr.create("Сок", 8)


@pytest.fixture
def example_filled_warehouse():
    return wr


@pytest.fixture
def example_empty_warehouse():
    return Warehouse()


def test_create_bad_product(example_empty_warehouse: Warehouse):
    with pytest.raises(BadProductError) as e:
        example_empty_warehouse.create("aa",1)

    assert e.type is BadProductError
    assert e.value.args == ("aa", "Название должно быть более 2 символов")


def test_create_bad_product_str(example_empty_warehouse: Warehouse):
    try:
        example_empty_warehouse.create("aa",1)
    except BadProductError as e:
        assert str(e) == "BadProductError: aa - Название должно быть более 2 символов"


def test_create_bad_shelf(example_empty_warehouse: Warehouse):
    with pytest.raises(BadShelfError) as e:
        example_empty_warehouse.create("aaaa", -1)

    assert e.type is BadShelfError
    assert e.value.args == (-1, "№ стеллажа должен быть от 1 до 100")


def test_create_bad_shelf_str(example_empty_warehouse: Warehouse):
    try:
        example_empty_warehouse.create("aaaa",-1)
    except BadShelfError as e:
        assert str(e) == "BadShelfError: -1 - № стеллажа должен быть от 1 до 100"


def test_create_product_ok(example_empty_warehouse: Warehouse):
    assert example_empty_warehouse.create("Груз", 1)


def test_read_all(example_filled_warehouse):
    assert (example_filled_warehouse.read_all() =="""Список товаров:
id: 1 - Товар: Груз, стеллаж: 1
id: 2 - Товар: Гири, стеллаж: 2
id: 3 - Товар: Сок, стеллаж: 8
""")


def test_read_bad_id(example_empty_warehouse: Warehouse):
    with pytest.raises(BadIdError) as e:
        example_empty_warehouse.read(-1)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер товара от 1")


def test_read_bad_id_str(example_empty_warehouse: Warehouse):
    try:
        example_empty_warehouse.read(-1)
    except BadIdError as e:
        assert str(e) == "BadIdError: -1 - Номер товара от 1"


def test_read_bad_id_not_contained(example_empty_warehouse: Warehouse):
    with pytest.raises(BadIdError) as e:
        example_empty_warehouse.read(100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Такого товара нет")


def test_read_bad_id_not_contained_str(example_empty_warehouse: Warehouse):
    try:
        example_empty_warehouse.read(100)
    except BadIdError as e:
        assert str(e) == "BadIdError: 100 - Такого товара нет"


def test_read_bad_id_ok_contained(example_filled_warehouse):
    assert example_filled_warehouse.read(1).product == "Груз"
    assert example_filled_warehouse.read(1).shelf == 1


def test_read_product_str(example_filled_warehouse):
    assert str(example_filled_warehouse.read(1)) == "Товар: Груз, стеллаж: 1"


# Update testing.
def test_update_product_ok(example_filled_warehouse):
    assert example_filled_warehouse.update(1, 100)


def test_update_product_id(example_filled_warehouse):
    with pytest.raises(BadIdError) as e:
        example_filled_warehouse.update(-1, 100)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер товара от 1")


def test_update_product_id_not_contained(example_filled_warehouse):
    with pytest.raises(BadIdError) as e:
        example_filled_warehouse.update(100, 100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Такого товара нет")


def test_update_bad_shelf(example_filled_warehouse):
    with pytest.raises(BadShelfError) as e:
        example_filled_warehouse.update(1, -1)

    assert e.type is BadShelfError
    assert e.value.args == (-1, "№ стеллажа должен быть от 1 до 100")


def test_delete_product_ok(example_filled_warehouse):
    assert example_filled_warehouse.delete(1)


def test_delete_product_id(example_filled_warehouse):
    with pytest.raises(BadIdError) as e:
        example_filled_warehouse.delete(-1)

    assert e.type is BadIdError
    assert e.value.args == (-1, "Номер товара от 1")


def test_delete_product_id_not_contained(example_filled_warehouse):
    with pytest.raises(BadIdError) as e:
        example_filled_warehouse.delete(100)

    assert e.type is BadIdError
    assert e.value.args == (100, "Такого товара нет")
