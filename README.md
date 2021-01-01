# python-private-packages

An exercise exploring the behaviors of Python Packages and how to create
private packages.

The approach is to take a simple task, and refactor it to an extreme

In reality, you likely would never do this specifically, but the exmaple is here
to be explored for its structural benefits, not the task itself.

## Requirements

To measure the success here, I set myself some guidelines:

- The code has to be readily testable by `pytest`
- The code has to pass `pylint` with no customiztion/overrides

**Note:** In most real-world scenarios, there's often some configuration for
`pylint`, such as removing a requirement for test functions to have docstrings.
Instead of trying to disable things, I've opted to not configure `pylint`,
rather provide simple (if not very useful) docstrings to pass the linter.
Please don't judge the content of these docstrings.

## The App

Well, the ultimate goal of "my awesome app" is to return a `"Hello, world."`
string.

Yes, that's it.

But instead of simply accomplishing the task like some normal person, let's
refactor the task to a crazy degree, splitting pieces of work apart to explore
import and test structure.

As a way to separate concerns, the `myawesomeapp` package is only responsible
for the execution part - not the internals of how to construct and represent
the desired outcome.

The rest of the phrase's work is delegated to the `helloworld` package, which
could be an open source/installed package, or part of the same codebase.

By segregating the internals of what is essentially a subdirectory structure
wth a naming convention, we create a boundary which can be broken, but
convention shows the user the "right way".

After all, [we are all responsible users][].

[we are all responsible users]: https://docs.python-guide.org/writing/style/#we-are-all-responsible-users

## Running

If you want to checkout the code, run the tests yourself, please do!

1. Clone the repository locally
2. Run `make init` to install the requisite dependencies
3. Run `make test` to execute the tests

Run `make uninstall` to have `pipenv` remove the created virtualenv.
We don't remove [`pipenv`][] itself, since it's an awesome tool, check it out.

[pipenv]: https://pipenv.pypa.io/

## Author

- [Mike Fiedler](https://github.com/miketheman)
