from typing import Literal


def sort(
    width: int, height: int, length: int, mass: int
) -> Literal["STANDARD", "SPECIAL", "REJECTED"]:
    bulky: bool = check_bulkiness(width, height, length)
    heavy: bool = check_heaviness(mass)
    match bulky, heavy:
        case True, True:
            return "REJECTED"
        case True, False:
            return "SPECIAL"
        case False, True:
            return "SPECIAL"
    return "STANDARD"


def check_bulkiness(width: int, height: int, length: int) -> bool:
    """
    bulkiness is:
    volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³
    or when one of its dimensions is greater or equal to 150 cm
    :param width: side of package
    :param height: side of package
    :param length: side of package
    :return: True if bulky
    """
    if width * height * length >= 1_000_000:
        return True

    if width >= 150:
        return True

    if height >= 150:
        return True

    if length >= 150:
        return True

    return False


def check_heaviness(mass: int) -> bool:
    """
    heavy is when its mass is greater or equal to 20 kg
    :param mass: in kg
    :return: True if over or equal to 20 kg
    """
    if mass >= 20:
        return True

    return False
