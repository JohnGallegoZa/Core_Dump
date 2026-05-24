from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

@runtime_checkable
class Reportable(Protocol):
    def obtener_reporte(self) -> str:
        ...

