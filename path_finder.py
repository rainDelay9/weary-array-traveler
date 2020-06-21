from weary import WearyGraph
import click


@click.command()
@click.option('-t', '--type', 'input_format', type=click.Choice(['CSV', 'TSV', 'JSON'], case_sensitive=False),
              required=True, help='input format')
@click.option('-f', '--file', 'path', type=str, help='input file (takes precedence over input string)')
@click.option('-a', '--arr', 'arr', type=str, help='input string')
def find_path(path, arr, input_format):
    """This script checks whether there's a path from start to finish in a weary array traveler problem.
       Currently acceptes csv, tsv and json file formats."""
    if path is None and arr is None:
        print("Error! Please add an option!")
        exit(1)

    if path is not None:
        try:
            with open(path, 'r') as f:
                data = f.read().replace('\n', '')
        except PermissionError:
            print("Error! Cannot read file! Perhaps you are missing some permissions...")
            exit(1)
        except FileNotFoundError:
            print("Error! File does not exist!")
            exit(1)
    else:
        data = arr

    try:
        graph = WearyGraph(data)
        print("Input: ", graph)
    except ValueError:
        print("Formatting Error! Please check input data! Exiting...")
        exit(1)

    print("Result: ", ("Path exists!" if graph.has_path() else "Path does not exist!"))


if __name__ == '__main__':
    find_path()
