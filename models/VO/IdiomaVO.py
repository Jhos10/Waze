from dataclasses import dataclass 
from typing import Optional

@dataclass
class IdiomaVO:
    id_idioma : Optional[int] = None 
    nombre_idioma : Optional[str] = None