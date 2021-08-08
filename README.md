# Python-Testing
Unittest-Pytest-Doctest-Mock

# [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")  — Unit testing framework

In software engineering, a unit test refers to a program used to automatically check for bugs in individual parts/units of software. Unit testing is an important phase of the software development life cycle. To carry out a test, a developer specifies a set of testcases and their expected results for comparison.

A **unit test** is a scripted code-level test, written in Python to verify a small "unit" of functionality.

## **Advantages of Unit Testing**

-   **Detecting problems early**  - Unit tests discloses problems early into the development.
    
-   **Mitigating change**  - Allows the developer to refactor the source code during the testing stage and later on, while still making sure the module works as expected.
    
-   **Simplifying integration**  - By testing the separate components of an application first and then testing them altogether, integration testing becomes much easier.
    
-   **Source of Documentation**  - The unit testing with doctest provides a better insight.
-  **Quality of Code** - Unit testing improves the quality of the code. It identifies every defect that may have come up before code is sent further for integration testing.


# [`pytest`]("https://docs.pytest.org/en/6.2.x/index.html#")  — Pytest framework

The `pytest` framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

## Install  `pytest`
```
$ python -m pip install pytest
```
### Less Boilerplate[](https://realpython.com/pytest-python-testing/#less-boilerplate "Permanent link")

Most functional tests follow the Arrange-Act-Assert model:

1.  **Arrange**, or set up, the conditions for the test
2.  **Act**  by calling some function or method
3.  **Assert**  that some end condition is true

`pytest`  offers a core set of productivity features to filter and optimize your tests along with a flexible plugin system that extends its value even further. Whether you have a huge legacy  `unittest`  suite or you’re starting a new project from scratch,  `pytest`  has something to offer you.



-   **Fixtures**  for handling test dependencies, state, and reusable functionality
-   **Marks**  for categorizing tests and limiting access to external resources
-   **Parametrization**  for reducing duplicated code between tests
-   **Durations**  to identify your slowest tests
-   **Plugins**  for integrating with other frameworks and testing tools


# [`mock`]("https://pypi.org/project/mock/#")  — Mock library

When you’re writing robust code, tests are essential for verifying that your application logic is correct, reliable, and efficient. However, the value of your tests depends on how well they demonstrate these criteria. Obstacles such as complex logic and unpredictable dependencies make writing valuable tests difficult. The Python mock object library, `unittest.mock`, can help you overcome these obstacles.

A  [mock object](https://en.wikipedia.org/wiki/Mock_object)  substitutes and imitates a real object within a  testing environment. It is a versatile and powerful tool for  [improving the quality of your tests.

One reason to use Python mock objects is to control your code’s behavior during testing.

The Python [mock object library](https://docs.python.org/3/library/unittest.mock.html) is `unittest.mock`. It provides an easy way to introduce mocks into your tests.

```
$ pip install mock
```
The library also provides a function, called `patch()`, which replaces the real objects in your code with `Mock` instances. You can use `patch()` as either a decorator or a context manager, giving you control over the scope in which the object will be mocked. Once the designated scope exits, `patch()` will clean up your code by replacing the mocked objects with their original counterparts.



# [`doctest`]("https://docs.python.org/3/library/doctest.html#")  — Docktest library


The  [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")  module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

-   To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
    
-   To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
    
-   To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.
