# inheritence ? Controls -> (Keyboard/Gamepad)


class Controls(object):
    """
    """

    # inputs are pygame keyboard
    def __init__(self, left, right, up, down, select):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.select = select