from weary import WearyGraph
import click

@click.command()
@click.option('-f', '--file', 'path', type=str, help='input file (takes precedence over input string)')
@click.option('-i', '--input', 'input', type=str, help='input string')
def find_path(path, input):
    if path is None and input is None:
        print("Error! Must add an option!")
        exit(1)

    if path is not None:
        try:
            with open(path, 'r') as f:
                data = f.read().replace('\n', '')
        except PermissionError:
            print("Error! Cannot read file! Perhaps you are missing some permissions...\n")
            exit(1)
        except FileNotFoundError:
            print("Error! File does not exist!\n")
            exit(1)
    else:
        data = input

    try:
        graph = WearyGraph(data)
        print("Input: ", graph)
    except ValueError:
        print("Formatting Error! Please check input data! Exiting...\n")
        exit(1)

    print("Result: " + ("Path exists!" if graph.has_path() else "Path does not exist!") + "\n")


if __name__ == '__main__':
    find_path()
