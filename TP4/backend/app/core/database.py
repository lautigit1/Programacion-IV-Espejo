"""
Persistencia en memoria — sin imports de modelos para evitar ciclos.
Las listas se tipan con `list` genérica; los servicios hacen el cast correcto.
"""

categorias: list = []
productos: list = []

categoria_id_counter: int = 1
producto_id_counter: int = 1
