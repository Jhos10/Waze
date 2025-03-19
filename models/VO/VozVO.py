from dataclasses import dataclass
from typing import List, Optional

@dataclass
class VozVo:
    Tipo_voz : str
    ID_voz : Optional[int] = None