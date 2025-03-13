from __future__ import annotations  # for forward referencing
from datetime import datetime  # for timestamp in history
from copy import deepcopy  # return deepcopies to prevent manipulation

class Node:
    """ Object representing one single node. """
    
    def __init__(self, position_in_ripple: str, caption: str, opposite: str = "") -> None:
        """ Initializing position_in_ripple, caption, and opposite. """
        self._position_in_ripple = position_in_ripple
        self._caption = caption
        self._opposite = opposite
        self._history: list[dict[str, str, str, str]] = []

    @property
    def position_in_ripple(self) -> str:
        """
        Returning the Deep Copy of the Node's Position in the Ripple.
        Not to be changed after Initialization.
        """
        return deepcopy(self._position_in_ripple)

    @property
    def caption(self) -> str:
        """ Returning a Deep Copy of the Node's caption. """
        return deepcopy(self._caption)

    @caption.setter
    def caption(self, new_caption: str) -> str:
        """ Changing the Node's Caption to new_caption. """
        # checking for object type
        if not isinstance(new_caption, str):  
            raise ValueError("Caption must be a string.")
        # saving previous states csv-ready
        self._history.append({
            'timestamp': str(datetime.now()),
            'caption': self._caption,
            'opposite': self._opposite,
            'changed': 'caption'
        })
        self._caption = new_caption

    @property
    def opposite(self) -> str:
        """ Returning the Caption's Opposite. """
        return self._opposite

    @opposite.setter
    def opposite(self, new_opposite: str) -> None:
        """ Changing the Captions's Opposite to new_opposite. """
        if not isinstance(new_opposite, str):
            raise ValueError("Opposite must be a string")
        self._history.append({
            'timestamp': str(datetime.now()),
            'caption': self._caption,
            'opposite': self._opposite,
            'changed': 'opposite'
        })
        self._opposite = new_opposite

    @property
    def history(self) -> list[dict[str, str, str, str]]:
        """ Return a Deep Copy of the History. """
        return deepcopy(self._history)

    def __str__(self) -> str:
        """ Returning a printable Representation of Node object. """
        return f"{self.position_in_ripple} / {self.caption} / {self.opposite}"

    def __eq__(self, other: Node) -> bool:
        """ Equality means equal Captions. """
        if isinstance(other, Node):
            return self.caption == other.caption
        return False

if __name__ == '__main__':
    node0 = Node('CC: center circle', 'circle of wisdom', 'never ending story')
    node1 = Node('c1n1: circle1 node1', 'time', 'fairytail')
    node2 = Node('c1n2', 'no end')

    print(node0)
    print(node1)
    print(node2)

    print(node0 == node1)
    print(node0 == node2)

    node1.caption = node2.caption
    print(node1 == node2)
    print(node1.history)

# history: storing only changed values
# method: clearing_history
