import numpy as np

from aoc.day_03 import get_indices, o2_filter_value, co2_filter_value


def test_get_indices():

    data = np.array(
        [
            [1, 0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0],
        ]
    )

    # Test O2 behavior
    filter_rule = o2_filter_value

    np.array_equal(get_indices(data, 0, np.arange(4), filter_rule), np.array([0, 2, 3, 5]))
    np.array_equal(get_indices(data, 1, np.arange(4), filter_rule), np.array([1, 3, 5]))
    np.array_equal(get_indices(data, 2, np.arange(4), filter_rule), np.array([1, 2, 3, 4, 5]))

    indices_1 = get_indices(data, 0, np.arange(4), filter_rule)
    np.array_equal(indices_1, np.array([0, 2, 3]))

    indices_2 = get_indices(data, 1, indices_1, filter_rule)
    np.array_equal(indices_2, np.array([0, 2]))

    indices_3 = get_indices(data, 2, indices_2, filter_rule)
    np.array_equal(indices_3, np.array([0]))

    # Test CO2 behavior
    filter_rule = co2_filter_value

    np.array_equal(get_indices(data, 0, np.arange(4), filter_rule), np.array([1, 4]))
    np.array_equal(get_indices(data, 1, np.arange(4), filter_rule), np.array([0, 2, 4]))
    np.array_equal(get_indices(data, 2, np.arange(4), filter_rule), np.array([0]))

    indices_1 = get_indices(data, 0, np.arange(4), filter_rule)
    np.array_equal(indices_1, np.array([1, 4]))

    indices_2 = get_indices(data, 1, indices_1, filter_rule)
    np.array_equal(indices_2, np.array([4]))
