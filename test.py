
"""Test module for function get_degree from search_degree."""

import pytest

from search_degree import get_degree

test_data = [
    ((1.0, 3.5, 4.5, 0), 139.215),
    ((1, 1, 1, 1), 85.944),
    ((1.2, 13.2, 1.9, 19.2), 204.248),
]


@pytest.mark.parametrize('input_data, expected', test_data)
def test_get_degree(input_data: list, expected):
    """
    Тест на нахождение градусной меры точки соприкосновения через время.

    Args:
        input_data (list): input data for test
        expected (float): answer for task
    """
    radius, time, accel, start_sp = input_data
    def_answer = get_degree(radius, time, accel, start_sp)
    assert def_answer == expected
