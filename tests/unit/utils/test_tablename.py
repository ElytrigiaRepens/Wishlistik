from re import escape
from string import ascii_uppercase

from pytest import mark, raises

from utils import classname_to_tablename


class TestClassnameToTablename:
    @staticmethod
    def test_raises_value_error_on_empty_string() -> None:
        with raises(
            expected_exception=ValueError,
            match=escape('classname must not be empty'),
        ):
            classname_to_tablename('')

    @staticmethod
    @mark.parametrize(
        ('classname', 'tablename'),
        [
            ('Resume', 'resumes'),
            ('Snack', 'snacks'),
            ('Path', 'paths'),
        ],
    )
    def test_single_word_ending_with_usual_letter(
        classname: str,
        tablename: str,
    ) -> None:
        assert classname_to_tablename(classname) == tablename

    @staticmethod
    @mark.parametrize(
        ('classname', 'tablename'),
        [
            ('Glass', 'glasses'),
            ('Matrix', 'matrixes'),
            ('Jazz', 'jazzes'),
            ('Cach', 'caches'),
            ('Morzh', 'morzhes'),
            ('Dash', 'dashes'),
        ],
    )
    def test_single_word_ending_with_sibliants(
        classname: str,
        tablename: str,
    ) -> None:
        assert classname_to_tablename(classname) == tablename

    @staticmethod
    def test_single_word_ending_with_y() -> None:
        assert classname_to_tablename('Dairy') == 'dairies'

    @staticmethod
    def test_single_word_ending_with_ay() -> None:
        assert classname_to_tablename('Day') == 'days'

    @staticmethod
    def test_single_word_ending_with_number() -> None:
        assert classname_to_tablename('Snack1') == 'snack1s'

    @staticmethod
    def test_single_word_ending_with_underscore() -> None:
        assert classname_to_tablename('_Protected') == '_protecteds'

    @staticmethod
    @mark.parametrize(
        ('classname', 'tablename'),
        [(letter, f'{letter.lower()}s') for letter in ascii_uppercase],
    )
    def test_single_letter(classname: str, tablename: str) -> None:
        assert classname_to_tablename(classname) == tablename

    @staticmethod
    @mark.parametrize(
        ('classname', 'tablename'),
        [
            ('UserProfile', 'user_profiles'),
            ('SnackSet', 'snack_sets'),
            ('DailyCash', 'daily_cashes'),
            ('EmployeeSalary', 'employee_salaries'),
            ('WorkingDay', 'working_days'),
            ('WorkingDirectoryPath', 'working_directory_paths'),
        ],
    )
    def test_many_words(
        classname: str,
        tablename: str,
    ) -> None:
        assert classname_to_tablename(classname) == tablename
