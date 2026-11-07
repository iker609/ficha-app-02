""" FIcha técnica de una aplicación móvil antes de publicarla en la tienda """
from typing import Final

# Añadid aquí las importaciones que necesitéis.
"""Para la opcion 8"""
from decimal import ROUND_HALF_UP, Decimal
# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-00"
NOMBRE: Final[str] = "Agenda Escolar"
PAQUETE: Final[str] = "es.ieseuropa.agenda"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 2, 5, 13
TAMANO_APK: Final[int] = 48_734_208          # bytes
DESCARGAS: Final[int] = 12_500
PRECIO: Final[float] = 1.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 400
ESTRELLAS: Final[int] = 1_700                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0001011
COLOR_ICONO: Final[int] = 0xFF3A7BD5         # ARGB


# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "[usuario] · [usuario]"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 44
ANCHO_ETIQUETA: Final[int] = 16
ANCHO_VALOR: Final[int] = 14
BYTES_POR_MB: Final[int] = 1_000_000
BYTER_POR_MIB: Final[int] = 1_048_576
PORCENTAJE: Final[int] = 100

"""Pistas sacados del PDF del ejercicio y constantes necesarias:"""
"""Opcion 4"""
DESPLAZAMIENTO_MAYOR: Final[int] = 16
DESPLAZAMIENTO_MENOR: Final[int] = 8
MASCARA: Final[int] = 0xFF
"""Opcion 5"""
INTERNET: Final[int] = 0b0000001
NOTIFICACIONES: Final[int] = 0b0000010
CAMARA: Final[int] = 0b0000100
UBICACION: Final[int] = 0b0001000
CONTACTOS: Final[int] = 0b0010000
MICROFONO: Final[int] = 0b0100000
ALMACENAMIENTO: Final[int] = 0b1000000
"""Opcion 6"""
ALFA: Final[int] = 24
ROJO: Final[int] = 16
VERDE: Final[int] = 8
AZUL: Final[int] = 0
CANAL: Final[int] = 255
"""Opcion 7"""
PERMISO_CAMARA: Final[int] = 0b0000100 
UNDECIMAL: Final[int] = 1
DOSDECIMALES:Final[int] = 2
PLANTILLA_UNDECIMAL: Final[str] = "0.1"
PLANTILLA_DOSDECIMALES: Final[str] = "0.01"
"""Opcion 8"""
CARACTER_DOBLE: Final[str] = "="
CARACTER_SIMPLE: Final[str] = "-"

# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
COMISION: Final[float] = 0.15
def fila(etiqueta: str, valor:str) -> str:
    """ DEvuelve una etiqueta la izquierda y valor a la drecha"""
    return f"{etiqueta:<{ANCHO_ETIQUETA}}{valor:>{ANCHO_VALOR}}"

def separador(caracter:str)-> str:
    """DEvuelve una linea de separación con el ancho del programa"""
    return caracter * ANCHO
# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra el código, el nombre, el paquete y la version de la aplicación"""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    print(fila("Codigo:", CODIGO))
    print(fila("Nombre:", NOMBRE))
    print(fila("PAquete:", PAQUETE))
    print(fila("Versión:", version))
    


def opcion_2_tamano() -> None:
    """Muestra el tamaño del apk en bytes, mb y mib y su diferencia"""
    tamano_mb = TAMANO_APK / BYTES_POR_MB
    tamano_mib = TAMANO_APK / BYTER_POR_MIB
    diferenciaTamanos = (tamano_mb - tamano_mib) / tamano_mb * PORCENTAJE
    print("TAMAÑO DEL APK")
    print(fila("Bytes:", f"{TAMANO_APK} B"))
    print(fila("En la tienda:", f"{tamano_mb}"))
    print(fila("En el movil:", f"{tamano_mib}"))
    print(fila("Diferencia entre los dos:", f"{diferenciaTamanos}")) 



def opcion_3_ingresos() -> None:
    """Muestra ingresos brutos, netos y la comision de la tienda,"""
    ingresos_brutos = DESCARGAS * PRECIO
    comision_tienda = ingresos_brutos * COMISION
    ingresos_netos = ingresos_brutos - comision_tienda
    print("Ingresos")
    print(fila("Descargas:", f"{DESCARGAS} unidades"))
    print(fila("Precio:", f"{PRECIO:.2F}"))
    print(fila("INgresos brutos:", f"{ingresos_brutos:.2f}"))
    print(fila("Comision tienda:", f"{comision_tienda:.2f}"))
    print(fila("Ingresos netos:", f"{ingresos_netos:.2f}"))


def opcion_4_version() -> None:
    """Empaqueta la version de un entero y lo desempaqueta con bits"""
    version=f"{VERSION_MAYOR}, {VERSION_MENOR}, {VERSION_PARCHE}"

    mayor = VERSION_MAYOR << DESPLAZAMIENTO_MAYOR
    menor = VERSION_MENOR << DESPLAZAMIENTO_MENOR
    parche =    VERSION_PARCHE
    version_code = mayor | menor | parche

    mayor = version_code >> DESPLAZAMIENTO_MAYOR
    menor = (version_code >> DESPLAZAMIENTO_MENOR) & MASCARA
    parche = version_code & MASCARA

    version_desempaquetada = f"{mayor}, {menor}, {parche}"
    
    print("VersionCode")
    print(fila("Version:", version))
    print(fila("versionCOde:", str(version_code)))
    print(fila("En hexadecimal:", f"0x{version_code}"))
    print(fila("Desempaquetado:", version_desempaquetada))


def opcion_5_permisos() -> None:
    """Que permisos tiene la aplicación"""

    internet = (PERMISOS & INTERNET) != 0
    notificaciones = (PERMISOS & NOTIFICACIONES) != 0
    camara = (PERMISOS & CAMARA) != 0
    ubicacion = (PERMISOS & UBICACION) != 0
    contactos = (PERMISOS & CONTACTOS) != 0
    microfono = (PERMISOS & MICROFONO) != 0
    almacenamiento = (PERMISOS & ALMACENAMIENTO) != 0

    sin_ubicacion = PERMISOS & ~UBICACION

    print("PERMISOS")
    print(f"En binario: {PERMISOS}")
    print(f"Internet: {internet}")
    print(f"Notificaciones: {notificaciones}")
    print(f"Cámara: {camara}")
    print(f"Ubicación {ubicacion}")
    print(f"COntactos {contactos}")
    print(f"Micrófono {microfono}")
    print(f"Almacenamiento: {almacenamiento}")
    print(f"Sin ubicación: {sin_ubicacion}")


def opcion_6_color() -> None:
    """MUestra los componentesdel color del icono"""
    alfa = (COLOR_ICONO >> ALFA) & MASCARA
    rojo = (COLOR_ICONO >> ROJO) & MASCARA
    verde = (COLOR_ICONO >> VERDE) & MASCARA
    azul = (COLOR_ICONO >> AZUL) & MASCARA

    opacidad = alfa/ CANAL * PORCENTAJE
    color_css = f"#{rojo},{verde},{azul}"

    print("Color del icono")
    print(f"ARGB: 0X{COLOR_ICONO}")
    print(f"Rojo: {rojo}, {rojo:08b}, {rojo:02X}")
    print(f"Verde: {verde}, {verde:08b}, {verde:02X}")
    print(f"Azul: {azul}, {azul:08b}, {azul:02X}")
    print(f"Opacidad: {opacidad}")
    print(f"Para CSS: {color_css}")


def opcion_7_tipos() -> None:
    """Muestra tipo y valor de varios datos y conversiones"""
    media = ESTRELLAS / VALORACIONES
    permisos_camaraa = (PERMISOS & PERMISO_CAMARA) != 0
    texto_descargas = str(DESCARGAS)
    mayor = VERSION_MAYOR << DESPLAZAMIENTO_MAYOR
    menor = VERSION_MENOR << DESPLAZAMIENTO_MENOR
    codigo = mayor | menor | VERSION_PARCHE
    ingresos_brutos = DESCARGAS * PRECIO
    print("Tipos de datos")
    print(f"Nombre: {type(NOMBRE)} {NOMBRE}")
    print(f"Descargas: {type(DESCARGAS)} {DESCARGAS}")
    print(f"Precio: {type(PRECIO)} {PRECIO}")
    print(f"Media: {type(media)} {media}")
    print(f"pide_camara: {type(permisos_camaraa)} {permisos_camaraa}")
    print(f"texto_descargas: {type(texto_descargas)} {texto_descargas}")
    print(f"codigo:{type(codigo)} {codigo}")
    print(f"ingresos brutos: {type(ingresos_brutos)} {ingresos_brutos}")

def opcion_8_redondeo() -> None:
    """Compara round() con el redondeo de la valoracion media"""
    media = ESTRELLAS / VALORACIONES
    media_decimal = Decimal(str(media))
    plantilla_1 = Decimal(PLANTILLA_UNDECIMAL)
    plantilla_2 = Decimal(PLANTILLA_DOSDECIMALES)
    round_1 = round(media, UNDECIMAL)
    round_2 = round(media, DOSDECIMALES)
    escolar_1 = media_decimal.quantize(plantilla_1, rounding=ROUND_HALF_UP)
    escolar_2 = media_decimal.quantize(plantilla_2, rounding=ROUND_HALF_UP)
    print("Redondeo de la valoración media")
    print(fila("VAlor exacto:", f"{media}"))
    print(fila("round(), 1 dec.:", f"{round_1}"))
    print(fila("EScolar, 1 dec.:", f"{escolar_1}"))
    print(fila("round(), 2dec.:", f"{round_2}"))
    print(fila("Escolar, 2 dec.:", f"{escolar_2}"))


def opcion_9_ficha() -> None:
    """Muestra la ficha completa reutilizando las opciones 1 a 4"""
    print(separador(CARACTER_DOBLE))
    print(f"{'Ficha de la aplicación':^{ANCHO}}")
    print(separador(CARACTER_DOBLE))
    opcion_1_identificacion()
    print(separador(CARACTER_SIMPLE))
    opcion_2_tamano()
    print(separador(CARACTER_SIMPLE))
    opcion_3_ingresos()
    print(separador(CARACTER_SIMPLE))
    opcion_4_version()
    print(separador(CARACTER_DOBLE))


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
