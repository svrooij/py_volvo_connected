from enum import Enum

class CommandListItem_command(str, Enum):
    HONK_AND_FLASH = "HONK_AND_FLASH",
    HONK = "HONK",
    FLASH = "FLASH",
    LOCK = "LOCK",
    LOCK_REDUCED_GUARD = "LOCK_REDUCED_GUARD",
    UNLOCK = "UNLOCK",
    ENGINE_START = "ENGINE_START",
    ENGINE_STOP = "ENGINE_STOP",
    CLIMATIZATION_START = "CLIMATIZATION_START",
    CLIMATIZATION_STOP = "CLIMATIZATION_STOP",
    SEND_NAVI_POI = "SEND_NAVI_POI",

