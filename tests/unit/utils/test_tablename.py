from pytest import raises

from utils import classname_to_tablename


class TestClassnameToTablename:
    @staticmethod
    def test_raises_value_error_on_empty_string() -> None:
        with raises(
            expected_exception=ValueError,
            match='classname must not be empty',
        ):
            classname_to_tablename('')

    @staticmethod
    def test_single_word_ending_with_vowel() -> None:
        assert classname_to_tablename('Resume') == 'resumes'

    @staticmethod
    def test_single_word_ending_with_sibliants() -> None:
        assert classname_to_tablename('Cash') == 'cashes'

    @staticmethod
    def test_single_word_ending_with_y() -> None:
        assert classname_to_tablename('Dairy') == 'dairies'

    @staticmethod
    def test_single_word_ending_with_default_consonant() -> None:
        assert classname_to_tablename('Snack') == 'snacks'

    @staticmethod
    def test_single_word_ending_with_number() -> None:
        assert classname_to_tablename('Snack1') == 'snack1s'

    @staticmethod
    def double_word() -> None:
        assert classname_to_tablename('SnackSet') == 'snack_sets'
