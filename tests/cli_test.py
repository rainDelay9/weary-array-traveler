import os
import stat
from click.testing import CliRunner
from path_finder import find_path


def test_true_file_exists():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--file', 'examples/true.json'])
    assert 'Path exists!' in result.output
    assert result.exit_code == 0

def test_true_string():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--input', '4, 4, 1, 1, 2, 2, 1000, 1'])
    assert 'Path exists!' in result.output
    assert result.exit_code == 0

def test_false_file_exists():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--file', 'examples/false.json'])
    assert 'Path does not exist!' in result.output
    assert result.exit_code == 0

def test_false_string():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--input', '4, 2, 1, 3, 2, 2, 1000, 1'])
    assert 'Path does not exist!' in result.output
    assert result.exit_code == 0

def test_file_not_exist():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--file', 'dfsdfsfdsldjflskjdflksdjflskjdflsjdflsj.txt'])
    assert 'Error! File does not exist!' in result.output
    assert result.exit_code == 1

def test_unreadable_file():
    path = "unreadable-file-for-testing-only"
    f = open(path, "w+")
    f.close()
    os.chmod(path, stat.S_IWUSR)
    runner = CliRunner()
    result = runner.invoke(find_path, ['--file', path])
    assert 'Error! Cannot read file!' in result.output
    assert result.exit_code == 1
    os.remove(path)

def test_no_options_provided():
    runner = CliRunner()
    result = runner.invoke(find_path, [])
    assert 'Error! Please add an option!' in result.output
    assert result.exit_code == 1

def test_formatting_error():
    runner = CliRunner()
    result = runner.invoke(find_path, ['--input', '4, a4, 1, 1, 2, 2, 1000, 1'])
    assert 'Formatting Error' in result.output
    assert result.exit_code == 1
