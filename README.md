# Advent of Code 20XX


## Python

### Setup

Get set up by activating the environment:

```bash
$ .venv/bin/activate
```

Install any necessary packages using uv:

```bash
$ uv sync
```

### Running

Run using the following command:

```bash
$ python aoc.py [day] [part]
# e.g
$ python aoc.py 9 2
```

If not in `debug` mode, `log()` messages will be hidden from output.

You can run in `debug` mode by passing `--debug`:
```
$ python aoc.py 6 1 --debug
```

### Testing

Some days will give you a small, sample problem.

If this input is copied to `test.txt`, you can run your solution against the sample by passing `--test`:

```bash
$ python aoc.py 11 2 --test
```

