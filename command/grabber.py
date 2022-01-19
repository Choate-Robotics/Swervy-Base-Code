from lib.command import Command, SubsystemCommand, T
from subsystem import Grabber


class GrabberMoveControl(SubsystemCommand[Grabber]):
    def __init__(self, subsystem: Grabber, down: bool = True):
        super().__init__(subsystem)
        self.down = down

    def initialize(self) -> None:
        self.subsystem.set_move(self.down)

    def isFinished(self) -> bool:
        return True


class GrabberGrabControl(SubsystemCommand[Grabber]):
    def __init__(self, subsystem: Grabber, closed: bool = True):
        super().__init__(subsystem)
        self.on = closed

    def initialize(self) -> None:
        self.subsystem.set_grab(self.on)

    def isFinished(self) -> bool:
        return True

