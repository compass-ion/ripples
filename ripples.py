"""
Aus einem Kernpunkt im Zentrum breiten sich die Ringe
der Erkenntnis in konzentrischen Kreisen aus, aehnlich
eines Tropfens, der ins Wasser faellt.

Und so wird aus einem Tropfen Erkenntnis ein ganzer See.
"""
from datetime import datetime  # for timestamp in history
from copy import deepcopy # return deepcopies to prevent manipulation

class Node:
    """"representing one single node"""

    def __init__(self, position, name, antidote):
        """initializing position in the circle, caption or name, and ..."""
        self._position = position
        self._name = name
        self._antidote = antidote
        self._history = []

    @property
    def position(self):
        """returning the initialized position (immutable)"""
        return deepcopy(self._position)

    # intentionally no position setter
    
    @property
    def name(self):
        """returning name of the node"""
        return deepcopy(self._name)

    @name.setter
    def name(self, new_name):
        """changing the Node's name to new_name"""
        if not isinstance(new_name, str):  # checking for object type
            raise ValueError("Name must be a string.")
        self._history.append({  # saving previous states csv-ready
            'timestamp': str(datetime.now()),
            'name': self._name,
            'antidote':self._antidote,
            'changed': 'name'
        })
        self._name = new_name

    @property
    def antidote(self):
        """returning the name's antidote"""
        return self._antidote

    @antidote.setter
    def antidote(self, new_antidote):
        """changing the names's antidote to new_antidote"""
        if not isinstance(new_antidote, str):
            raise ValueError("Antidote must be a string")
        self._history.append({  # saving previous states csv-ready
            'timestamp': str(datetime.now()),
            'name': self._name,
            'antidote':self._antidote,
            'changed': 'antidote'
        })
        self._antidote = new_antidote

    @property
    def history(self):
        """Return a deep copy of the history of changes"""
        return deepcopy(self._history)

    def __str__(self):
        """returning a printable representation of Node"""
        return f"{self.position} / {self.name} / {self.antidote}"

    def __eq__(self, other):
        """equality means equal names"""
        if isinstance(other, Node):
            return self.name == other.name
        return False

if __name__ == '__main__':
    node0 = Node('CC: center circle', 'circle of wisdom', 'never ending story')
    node1 = Node('c1n1: circle1 node1', 'time', 'fairytail')
    node2 = Node('c1n2', 'no end', 'waste')

    print(node0)
    print(node1)
    print(node2)

    print(node0 == node1)
    print(node0 == node2)

    node1.name = node2.name
    print(node1 == node2)
    print(node1.history)
"""
Possible Improvements:

- Type Hints
- History: storing only changed values
- Custom Error Classes
- Method To Clear History
- CSV or JSON support
- Improving __str__
- Unit Tests
- Docstrings With More Context?
- ...
