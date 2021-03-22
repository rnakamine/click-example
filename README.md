# click-example
Example of using the CLICK package

## Usage

### Hello World
[hello.py](hello.py)
```sh
$ python hello.py --help
Usage: hello.py [OPTIONS]

Options:
  --help  Show this message and exit.
```

### Add Option
[option.py](option.py)
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
[arguments.py](arguments.py)
```sh
$ python arguments.py Ryo
Hello, Ryo
```

```sh
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

### Add Subcommand
[subcommand.py](subcommand.py)
```sh
$ python subcommand.py
Usage: subcommand.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  command1
  command2
```

```sh
$ python subcommand.py command1
execute command1
```

```sh
$ python subcommand.py command2
execute command2
```

### Add Contexts
[pass_contexts.py](pass_contexts.py)
```sh
$ python pass_contexts.py
Usage: pass_contexts.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  sync
```

```sh
$ python pass_contexts.py sync
Debug is off
```

```sh
$ python pass_contexts.py --no-debug sync
Debug is off
```
