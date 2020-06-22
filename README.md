# weary-array-traveler
This is a python CLI solver for the weary array traveler problem

## Installation (UNIX)

1. Clone the directory:
```bash
git clone https://github.com/rainDelay9/weary-array-traveler.git
```

2. cd into the project directory and execute:
```bash
pip install -e .
```

3. run help:
```bash
weary --help
```

Output should look like this:
```bash
Usage: weary [OPTIONS]

  This script checks whether there's a path from start to finish in a weary
  array traveler problem. Currently acceptes csv, tsv and json file formats.

Options:
  -t, --type [CSV|TSV|JSON]  input format  [required]
  -f, --file TEXT            input file (takes precedence over input string)
  -a, --arr TEXT             input string
  --help                     Show this message and exit.
```

## Execution examples

These are some execution examples. For stress testing (arrays with ~8000 elements) see examples/superlong_true.csv and examples/superlong_false.csv.

```bash
> weary --type csv --file examples/true.csv
Input:  [4, 4, 1, 1, 2, 2, 1000, 1]
Result:  Path exists!
```


```bash
> weary -t json -f examples/false.json
Input:  [4, 2, 1, 3, 2, 2, 1000, 1]
Result:  Path does not exist!
```

```bash
> weary -t csv --arr "4, 2, 1, 3, 2, 2, 1000, 1"
Input:  [4, 2, 1, 3, 2, 2, 1000, 1]
Result:  Path does not exist!
```

