class GameException(Exception):
    pass

class InsufficientEnergyError(GameException):
    pass

class InsufficientBitsError(GameException):
    pass

class EmptyInventoryError(GameException):
    pass

class LowIntegrityError(GameException):
    pass

class AllSectorsRepairedError(GameException):
    pass

