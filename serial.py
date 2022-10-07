"""Python serial number generator."""

class SerialGenerator:
    def __init__(self,start=0):
        self.start = start
        self.next = start
    
    def generate(self):
        self.next += 1
        return self.next

    def reset(self):
        """Reset number to original start."""

        self.next = self.start
    
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

