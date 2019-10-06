# Dependencies
from CoinClass import CoinProblem
import pytest

# Initial configuration of the Class
conf = {'experiment': 'Minimum Coin Problem', 'inputs': {'change': 111, 'available_coins': [2, 5, 50], 'timer': True}}


@pytest.fixture
def get_test_layer_init_data():

    # get_test_layer_init_data : (coin_value_list, expected_init_layer)
    data = [([2], [[2, 2]]), ([2, 5], [[2, 2], [5, 5]]), ([2, 5, 10], [[2, 2], [5, 5], [10, 10]])]

    return data

@pytest.fixture
def get_test_calculate_next_layer_data():

    # get_test_calculate_next_layer_data :
    # (coin_value_list, previous_layer, next_layer)
    data = [([2], [[2, 2]], [[4, 2, 2]]), ([2, 5], [[2, 2], [5, 5]], [[4, 2, 2], [7, 2, 5], [10, 5, 5]])]

    return data


def test_layer_init(get_test_layer_init_data):

    # Function that tests the layer_init() function of the CoinProblem class
    # in order to secure that it has the right output

    # Class initializer
    test_class = CoinProblem(conf)

    for data in get_test_layer_init_data:

        test_class.coin_value_list = data[0]
        expected = data[1]
        test_class.layer_init()

        assert test_class.next_layer == expected


def test_layer_init_output_type(get_test_layer_init_data):

    # Function that tests the layer_init() function of the CoinProblem class
    # in order to secure that the output has the right type

    # Class initializer
    test_class = CoinProblem(conf)

    for data in get_test_layer_init_data:

        test_class.coin_value_list = data[0]
        test_class.layer_init()

        assert type(test_class.next_layer) is list


def test_calculate_next_layer(get_test_calculate_next_layer_data):

    # Function that tests the calculate_next_layer() function of the CoinProblem class
    # in order to secure that it has the right output

    # Class initializer
    test_class = CoinProblem(conf)

    for data in get_test_calculate_next_layer_data:

        test_class.coin_value_list = data[0]
        test_class.next_layer = data[1]
        expected = data[2]
        test_class.calculate_next_layer()

        assert test_class.next_layer == expected


def test_calculate_next_layer__output_type(get_test_calculate_next_layer_data):

    # Function that tests the calculate_next_layer() function of the CoinProblem class
    # in order to secure that the output has the right type

    # Class initializer
    test_class = CoinProblem(conf)

    for data in get_test_calculate_next_layer_data:

        test_class.coin_value_list = data[0]
        test_class.next_layer = data[1]
        test_class.calculate_next_layer()

        assert type(test_class.next_layer) == list

