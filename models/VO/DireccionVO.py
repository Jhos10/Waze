from dataclasses import dataclass
from typing import Optional


@dataclass
class DireccionVO:
    id_direccion : Optional[int] = None
    direccion : Optional[str] = None