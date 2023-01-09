# Retrieving docstrings
sum.__doc__

# Using inspect module
import inspect
inspect.get_doc(sum)

# How to make a context manager
@contextlib.contextmanager
# Define a function
def my_context():
    # Add any set up code you need
    yield


