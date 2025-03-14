# check-dependencies

`check-dependencies` is a simple command line tool to easily check if your Python project contains too many outdated dependencies. 

## Usage

Add `check-dependencies` to your project:

```
$ poetry add --group=dev git+https://github.com/hekonsek/check-dependencies.git@v0.3.0 
```

Check dependencies:

```
$ poetry run check-dependencies
Number of outdated dependencies: 0
Dependency check passed.
```