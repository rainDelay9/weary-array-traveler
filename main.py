from weary import WearyGraph

if __name__ == '__main__':
    tsv = "4\t2\t1\t3\t2\t2\t1000\t1"
    csv = "4,4,1,1,2,2,1000,1"
    js = "[4," \
         "4," \
         "1," \
         "1," \
         "2," \
         "2," \
         "1000," \
         "1" \
         "]"

    with open('examples/c.tsv', 'r') as file:
        data = file.read().replace('\n', '')

    try:
        graph = WearyGraph(data)
        print("Input: ", graph)
    except ValueError:
        print("Formatting Error! Please check input data! Exiting...")
        exit(1)

    print("Result: " + ("Path exists!" if graph.has_path() else "Path does not exist!"))
