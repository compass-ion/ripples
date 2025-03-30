from __future__ import annotations
from time import ctime as timestamp
from copy import deepcopy


class Node:
    """ Object representing one single node. """
    def __init__(self, position_in_ripple: str = '', caption: str = '',
                 opposite: str = '') -> None:
        """ Initializing position_in_ripple, caption, and opposite. """

        self._position_in_ripple = position_in_ripple
        self._caption = caption
        self._opposite = opposite
        self._history: list[dict[str, str]] = []

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
            'timestamp': str(timestamp()),
            'previous caption': self._caption
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
            'timestamp': str(timestamp()),
            'previous opposite': self._opposite
        })
        self._opposite = new_opposite

    @property
    def history(self) -> list[dict[str, str]]:
        """ Return a Deep Copy of the History. """
        return deepcopy(self._history)

    def clear_history(self) -> None:
        """ Clearing / Resetting the Node's History. """
        self._history.clear()

    def visualize(self) -> str:
        """ Returning ASCII Visualization of Node. """
        visual: str = ""
        visual += "+-" + "-"*len(self.caption) + "-+\n"
        visual += "| " + self.caption + " |\n"
        visual += "+-" + "-"*len(self.caption) + "-+\n"
        return visual

    def __repr__(self) -> str:
        """ Returning canonical string representation:
            eval(repr(Node)) != Node """
        return "'{}', '{}', '{}'".format(
            self._position_in_ripple, self._caption, self._opposite)

    def __str__(self) -> str:
        """ Returning a printable Representation of Node object. """
        return (f"Position: {self.position_in_ripple}\n"
                f"Caption: {self.caption}\n"
                f"Opposite: {self.opposite}\n")

    def __eq__(self, other: Node) -> bool:
        """ Equality means equal Captions and equal Opposites. """
        if isinstance(other, Node):
            return self.caption == other.caption and \
                self.opposite == other.opposite
        return False


if __name__ == '__main__':
    # defining nodes
    node0 = Node('center circle', 'circle of wisdom', 'never ending story')
    node1 = Node('cc', 'time', 'space')
    node2 = Node('r0n0', 'center node')
    print(node0, node1, node2, sep='\n', end='\n\n')

    # comparing nodes
    node1 = deepcopy(node0)
    print(f"node0 equals node1: {node0 == node1}")
    print(f"node0 is node1: {node0 is node1}", end='\n\n')

    # history
    node1.caption = 'new caption'
    print(node1.history)
    node1.clear_history()
    print(f'cleared history: {node1.history}', end='\n\n')

    # ASCII Visualization
    print(node0.visualize(), node1.visualize(), node2.visualize(), sep='')
