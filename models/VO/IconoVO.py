from dataclasses import dataclass
from typing import Optional
@dataclass
class IconoVO:
    tipo : Optional[str] = None
    imagen : Optional[str] = None
    ID_Icono : Optional[int] = None