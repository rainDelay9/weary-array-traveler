import os
import stat
from click.testing import CliRunner
from path_finder import find_path


def check_cli(args, msg, exit_value):
    runner = CliRunner()
    result = runner.invoke(find_path, args)
    assert msg in result.output
    assert result.exit_code == exit_value


def test_true_file_exists():
    check_cli(['--file', 'examples/true.json', '--type', 'json'], 'Path exists!', 0)


def test_true_string():
    check_cli(['--arr', '4, 4, 1, 1, 2, 2, 1000, 1 ', '--type', 'csv'], 'Path exists!', 0)


def test_false_file_exists():
    check_cli(['--file', 'examples/false.json', '--type', 'json'], 'Path does not exist!', 0)


def test_false_string():
    check_cli(['--arr', '4, 2, 1, 3, 2, 2, 1000, 1', '--type', 'csv'], 'Path does not exist!', 0)


def test_file_not_exist():
    check_cli(['--file', 'dfsdfsfdsldjflskjdflksdjflskjdflsjdflsj.txt', '--type', 'csv'],
              'Error! File does not exist!', 1)


def test_unreadable_file():
    path = "unreadable-file-for-testing-only"
    if os.path.exists(path):
        os.remove(path)
    f = open(path, "w+")
    f.close()
    os.chmod(path, stat.S_IWUSR)
    check_cli(['--file', path, '--type', 'csv'], 'Error! Cannot read file!', 1)
    os.remove(path)


def test_no_options_provided():
    check_cli(['--type', 'csv'], 'Error! Please add an option!', 1)


def test_formatting_error():
    check_cli(['--arr', '4, a4, 1, 1, 2, 2, 1000, 1', '--type', 'csv'], 'Formatting Error', 1)


def test_wrong_type_given_tsv():
    check_cli(['--arr', '4, 4, 1, 1, 2, 2, 1000, 1', '--type', 'tsv'], 'Formatting Error', 1)


def test_wrong_type_given_csv():
    check_cli(['--arr', '[4, 4, 1, 1, 2, 2, 1000, 1]', '--type', 'csv'], 'Formatting Error', 1)


def test_wrong_type_given_json():
    check_cli(['--arr', '4\t4\t1\t1\t2\t2\t1000\t1', '--type', 'json'], 'Formatting Error', 1)
