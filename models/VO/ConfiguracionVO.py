from dataclasses import dataclass
from typing import List, Optional
from models.VO import DireccionVO, IdiomaVO, VozVO, IconoVO

@dataclass
class ConfiguracionVO:
    Id_configuracion : int
    unidadDistancia : str
    notificaciones : bool
    modo : str
    placa : str
    lista_direcciones : List[DireccionVO.DireccionVO] = None
    idioma : Optional[IdiomaVO.IdiomaVO] = None
    voz : Optional[VozVO.VozVo] = None
    icono : Optional[IconoVO.IconoVO] = None