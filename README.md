# Change Making Problem

[Change-making](https://en.wikipedia.org/wiki/Change-making_problem) is a simple [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming) problem.

## Dependencies

In order to run this program you need the python3 yaml library, which can be installed
by running the following command:

```terminal
pip3 install pyyaml
```

## Algorithm Logic

This approach is a [BFS](https://en.wikipedia.org/wiki/Breadth-first_search) (Breadth First Search) on a 
**Tree** containing all the available combinations.

## Use

In order to run the program use git clone and then edit the following variables of the
 **conf.yaml** file:

```python
change: 111
available_coins: [2, 5, 10, 20]
timer: True
```

**change**: is the desired amount

**available_coins**: handles the coins that can be used
in order to return the desired amount

**timer**: handles the code which prints the
execution time of the program

## Run

You execute the program by typing the following command:

```cmd
python3 main.py
```

## Tests with Pytest Library

To install the pytest library run the following command:

```
pip3 install pytest
```

In order to run the tests, navigate to the **tests** folder and then run the following command:

```
pytest test_CoinClass.py -v
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.
