from dataclasses import dataclass
from models.VO.ConfiguracionVO import ConfiguracionVO
from typing import Optional


@dataclass 
class UsuarioVO:
    ID_usuario : Optional[int] = None
    fecha_registro : Optional[str] = None
    email : Optional[str] = None
    nombre : Optional[str] = None
    configuracion : Optional[ConfiguracionVO] = None

