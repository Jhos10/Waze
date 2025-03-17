from dataclasses import dataclass
from models.VO.ConfiguracionVO import ConfiguracionVO


@dataclass 
class UsuarioVO:
    ID_usuario : int
    fecha_registro : str 
    email : str 
    nombre : str
    configuracion : ConfiguracionVO