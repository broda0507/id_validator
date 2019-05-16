import unittest


def is_validator(id_number: str) -> bool:
    if not len(id_number) == 9:
        return False
    letters, digits = id_number[0:3], id_number[3:]
    if not letters.isupper() or not digits.isdigit():
        return False

    numbers = []

    weights = [7, 3, 1, 9, 7, 3, 1, 7, 3]
    for letter in letters:
        numbers.append(ord(letter) - 55)
    for digit in digits:
        numbers.append(int(digit))
    control_sum = sum([x * y for x, y in zip(numbers, weights)])
    return control_sum % 10 == 0


class ValidatorTest(unittest.TestCase):

    def test_too_short_id_returns_false(self):
        self.assertFalse(is_validator('AY123456'))

    def test_too_long_id_returns_false(self):
        self.assertFalse(is_validator('AY12345678'))

    def test_first_3_obj_not_letters_returns_false(self):
        self.assertFalse(is_validator('A1V123456'))

    def test_last_6_obj_not_numbers_retruns_false(self):
        self.assertFalse(is_validator('AGVC12345'))

    def test_empty_string_returns_false(self):
        self.assertFalse(is_validator(''))

    def test_correct_number_returns_true(self):
        self.assertTrue(is_validator('XTO140605'))



    def test_lowercase_letters_returns_false(self):
        self.assertFalse(is_validator('xTO140605'))
