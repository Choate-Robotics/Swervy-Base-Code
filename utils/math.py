import math


def clamp(val, _min, _max):
    if val < _min:
        return _min
    if val > _max:
        return _max
    return val


def sensor_units_to_inches(sensor_units: float, low_gear: bool) -> float:
    motor_rotations = sensor_units / 2048.0

    if low_gear:
        wheelbase_rotations = motor_rotations / 15.45  # Low gear
    else:
        wheelbase_rotations = motor_rotations / 8.21  # High gear

    inches = wheelbase_rotations * (6 * math.pi)

    return inches


def inches_to_sensor_units(inches: float, low_gear: bool) -> float:
    wheelbase_rotations = inches / (6 * math.pi)

    if low_gear:
        motor_rotations = wheelbase_rotations * 15.45  # Low gear
    else:
        motor_rotations = wheelbase_rotations * 8.21  # High gear

    sensor_units = motor_rotations * 2048.0

    return sensor_units