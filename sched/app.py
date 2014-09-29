from flask import *
import doctest

app = Flask(__name__)


@app.route('/')
def hello():
    """

    >>> hello()
    'Hello, world!'
    """
    return 'Hello, world!'


if __name__ == "__main__":
    doctest.testmod()
    app.run()
