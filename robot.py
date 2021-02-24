import wpilib
import utils.logger as logger

import subsystem
import command.drivetrain
import command.shooter
import oi


class Robot(wpilib.TimedRobot):
    drivetrain: subsystem.Drivetrain
    shooter: subsystem.Shooter
    oi: oi.OI

    def robotInit(self):
        logger.info("initializing robot")

        self.oi = oi.OI()

        self.drivetrain = subsystem.Drivetrain()
        self.drivetrain.setDefaultCommand(command.drivetrain.DriveArcade(self.drivetrain, self.oi))

        self.shooter = subsystem.Shooter()

        self.oi.map_controls(self.shooter)

        logger.info("initialization complete")

    def robotPeriodic(self):
        pass

    def autonomousInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def _simulationInit(self) -> None: ...
    def _simulationPeriodic(self) -> None: ...


if __name__ == "__main__":
    wpilib.run(Robot)