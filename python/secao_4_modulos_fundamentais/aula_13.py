# Usando o metodo os.path.getsize e o os.stat

import os
import math

def format_size(size_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    if size_bytes <= 0:
        return "0B"

    size_names = "B", "KB", "MB", "GB", "TB", "PB", "YB"
    index_name = int(math.log(size_bytes, base))
    pot = base ** index_name

    final_size = round(size_bytes/pot, 2)

    size_sufix = size_names[index_name]
    return f"{final_size} {size_sufix}"

