"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Make a new generator, starting at start"""

        self.start = start
        self.index = 0

    def __repr__(self):
        """Show representation."""
        
        return f"<SerialGenerator start={self.start} index={self.index}>"

    def generate(self):
        """Returns a new serial number in increments of 1 each time the function is called; starts with self.start value."""
        new_serial = self.start + self.index
        self.index += 1
        return new_serial

    def reset(self):
        """Resets the serial number index to 0; the first serial number generated with generate() after reset funciton will return the self.start value."""
        self.index = 0
