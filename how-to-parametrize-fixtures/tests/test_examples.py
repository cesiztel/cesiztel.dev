"""Module that contains examples of the fixtures and parametrization."""
import pytest


@pytest.fixture(name="first_sum_op")
def fixture_first_sum_op():
    return "3+5"

@pytest.fixture(name="second_sum_op")
def fixture_second_sum_op():
    return "2+4"

@pytest.fixture(name="multiplication_op")
def fixture_multiplication_op():
    return "6*9"

# example of parametrization
@pytest.mark.parametrize(
  "test_input,expected", 
  [
    ("first_sum_op", 8), 
    ("second_sum_op", 6), 
    ("multiplication_op", 54)
  ],
  ids=["first_sum_op", "second_sum_op", "multiplication_op"]
)
def test_eval(test_input, expected, request):
    # ARRANGE
    test_input_data = request.getfixturevalue(test_input)
    
    # ASSERT
    assert eval(test_input_data) == expected

@pytest.fixture(name="sum_op")
def fixture_sum_op(request):
    return f"{request.param[0]}+{request.param[1]}"

@pytest.mark.parametrize(
  "sum_op, expected", 
  [
    ((2, 3), 5),
    ((5, 3), 8),
    ((4, 5), 9)
  ],
  indirect=["sum_op"]
)
def test_eval_sum_operations(sum_op, expected):
    # ASSERT
    assert eval(sum_op) == expected