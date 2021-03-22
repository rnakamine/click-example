# click-example
Example of using the CLICK package

## Usage

### Hello World
```sh
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```

### Add Option
```sh
$ python option.py --count 3 -n Ryo
Hello Ryo
Hello Ryo
Hello Ryo
```
```sh
$ python option.py --help
Usage: option.py [OPTIONS]

  Simple program that greets NAME for a total of COUNT times.

Options:
  --count INTEGER  Number of greetings.
  -n, --name TEXT  The person to greet.
  --help           Show this message and exit.
```

### Add Arguments
```sh
$ python arguments.py Ryo
Hello, Ryo
```

```
$ python arguments.py --help
Usage: arguments.py [OPTIONS] NAME

Options:
  --help  Show this message and exit.
```

If there is no argument, an error will occur.
```sh
$ python arguments.py
Usage: arguments.py [OPTIONS] NAME
Try 'arguments.py --help' for help.

Error: Missing argument 'NAME'.
```
