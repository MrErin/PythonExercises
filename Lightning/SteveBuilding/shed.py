from building import Building


class Shed(Building):
    """
    Author: Steve Brownlee
    Inherits from: Building
    Purpose: To represent any kind of shed for users to build in the UI.
    """

    def __init__(self):
        """
        Initialization method for Shed

        Arguments: windows {number} -- integer for number of windows in the shed
        """

        self.workbench = True
        self.tools = []
        super().__init__()
