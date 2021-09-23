from sample_app import first_name, last_name, capitalise_name
import unittest


class TestSum(unittest.TestCase):
    def test_first(self):
        first_n = first_name("Spiros Morfonios")

        try:
            assert first_n == "Spiros"
        except AssertionError:
            raise AssertionError(f"did not match: {first_n} Spiros ")

    def test_first_name_multiple_times(self):
        test_list = [
            ("Dora Sun", "Dora"),
            ("Tawfiq H", "Tawfiq"),
            ("Spiros Morfonios", "Spiros"),
        ]

        for full_name, expected_first_name in test_list:
            first_result = first_name(full_name)

            try:
                assert expected_first_name == first_result
            except AssertionError:
                raise AssertionError(
                    f"Expected first name:{expected_first_name} Did not match actual first-name: {first_result}"
                )

    def test_last_multiple(self):
        test_list = [
            ("Dora Sun", "Sun"),
            ("Tawfiq Hamid", "Hamid"),
            ("Spiros Morfonios", "Morfonios"),
        ]

        for full_name, expected_last_name in test_list:
            last_result = last_name(full_name)

            try:
                assert expected_last_name == last_result
            except AssertionError:
                raise AssertionError(
                    f"Expected Last Name:{expected_last_name}  Did not match last name {last_result}"
                )

    def test_capitalize(self):
        test_list = [
            ("Dora Sun", "DORA SUN"),
            ("Tawfiq Hamid", "TAWFIQ HAMID"),
            ("Spiros Morfonios", "SPIROS MORFONIOS"),
        ]

        for full_name, expected_capitalised in test_list:
            last_result = capitalise_name(full_name)

            try:
                assert expected_capitalised == last_result
            except AssertionError:
                raise AssertionError(
                    f"did not match:{expected_capitalised} - {last_result}"
                )


if __name__ == "__main__":
    unittest.main()
