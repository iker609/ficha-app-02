"""Ficha técnica de una aplicación móvil antes de publicarla en la tienda."""
from decimal import ROUND_HALF_UP, Decimal
import platform
from typing import Final

# ---------------------------------------------------------------------------
# Datos de la aplicación. Asignados a la Pareja 2 (APP-02).
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-02"
NOMBRE: Final[str] = "Lista de la Compra"
PAQUETE: Final[str] = "es.hogar.listacompra"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 3, 0, 7
TAMANO_APK: Final[int] = 18_874_368          # bytes
DESCARGAS: Final[int] = 25_400
PRECIO: Final[float] = 0.49                  # euros, IVA incluido
VALORACIONES: Final[int] = 1_000
ESTRELLAS: Final[int] = 4_350                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b0010011
COLOR_ICONO: Final[int] = 0xFFF9A825         # ARGB


# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "Iker Alcolea Mateos · David Raúl Rus Almaján"
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
DOSDECIMALES: Final[int] = 2
PLANTILLA_UNDECIMAL: Final[str] = "0.1"
PLANTILLA_DOSDECIMALES: Final[str] = "0.01"
"""Opcion 8"""
CARACTER_DOBLE: Final[str] = "="
CARACTER_SIMPLE: Final[str] = "-"

# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
COMISION: Final[float] = 0.15


def fila(etiqueta: str, valor: str) -> str:
    """Devuelve una etiqueta la izquierda y valor a la derecha."""
    return f"{etiqueta:<{ANCHO_ETIQUETA}}{valor:>{ANCHO_VALOR}}"


def separador(caracter: str) -> str:
    """Devuelve una linea de separación con el ancho del programa."""
    return caracter * ANCHO


# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra el código, nombre, paquete y versión de la aplicación."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    print(fila("Codigo:", CODIGO))
    print(fila("Nombre:", NOMBRE))
    print(fila("PAquete:", PAQUETE))
    print(fila("Versión:", version))


def opcion_2_tamano() -> None:
    """Muestra el tamaño del apk en bytes, mb y mib y su diferencia."""
    tamano_mb = TAMANO_APK / BYTES_POR_MB
    tamano_mib = TAMANO_APK / BYTER_POR_MIB
    diferenciaTamanos = (tamano_mb - tamano_mib) / tamano_mb * PORCENTAJE
    print("TAMAÑO DEL APK")
    print(fila("Bytes:", f"{TAMANO_APK} B"))
    print(fila("En la tienda:", f"{tamano_mb:.2f} MB"))
    print(fila("En el movil:", f"{tamano_mib:.2f} MiB"))
    print(fila("Diferencia:", f"{diferenciaTamanos:.1f} %"))


def opcion_3_ingresos() -> None:
    """Muestra ingresos brutos, netos y la comision de la tienda."""
    ingresos_brutos = DESCARGAS * PRECIO
    comision_tienda = ingresos_brutos * COMISION
    ingresos_netos = ingresos_brutos - comision_tienda
    print("INGRESOS")
    print(fila("Descargas:", f"{DESCARGAS} uds."))
    print(fila("Precio:", f"{PRECIO:.2f} €"))
    print(fila("Ingresos brutos:", f"{ingresos_brutos:.2f} €"))
    print(fila("Comisión tienda:", f"{comision_tienda:.2f} €"))
    print(fila("Ingresos netos:", f"{ingresos_netos:.2f} €"))


def opcion_4_version() -> None:
    """Empaqueta la version de un entero y lo desempaqueta con bits."""
    version = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"

    mayor = VERSION_MAYOR << DESPLAZAMIENTO_MAYOR
    menor = VERSION_MENOR << DESPLAZAMIENTO_MENOR
    parche = VERSION_PARCHE
    version_code = mayor | menor | parche

    mayor = version_code >> DESPLAZAMIENTO_MAYOR
    menor = (version_code >> DESPLAZAMIENTO_MENOR) & MASCARA
    parche = version_code & MASCARA

    version_desempaquetada = f"{mayor}.{menor}.{parche}"

    print("VERSIONCODE")
    print(fila("Versión:", version))
    print(fila("versionCode:", str(version_code)))
    print(fila("En hexadecimal:", f"0x{version_code:06X}"))
    print(fila("Desempaquetado:", version_desempaquetada))


def opcion_5_permisos() -> None:
    """Que permisos tiene la aplicación."""
    internet = (PERMISOS & INTERNET) != 0
    notificaciones = (PERMISOS & NOTIFICACIONES) != 0
    camara = (PERMISOS & CAMARA) != 0
    ubicacion = (PERMISOS & UBICACION) != 0
    contactos = (PERMISOS & CONTACTOS) != 0
    microfono = (PERMISOS & MICROFONO) != 0
    almacenamiento = (PERMISOS & ALMACENAMIENTO) != 0

    sin_ubicacion = PERMISOS & ~UBICACION

    print("PERMISOS")
    print(f"En binario: {PERMISOS:07b}")
    print(f"Internet: {internet}")
    print(f"Notificaciones: {notificaciones}")
    print(f"Cámara: {camara}")
    print(f"Ubicación: {ubicacion}")
    print(f"Contactos: {contactos}")
    print(f"Micrófono: {microfono}")
    print(f"Almacenamiento: {almacenamiento}")
    print(f"Sin ubicación: {sin_ubicacion:07b}")


def opcion_6_color() -> None:
    """Muestra los componentes del color del icono."""
    alfa = (COLOR_ICONO >> ALFA) & MASCARA
    rojo = (COLOR_ICONO >> ROJO) & MASCARA
    verde = (COLOR_ICONO >> VERDE) & MASCARA
    azul = (COLOR_ICONO >> AZUL) & MASCARA

    opacidad = alfa / CANAL * PORCENTAJE
    color_css = f"#{rojo:02X}{verde:02X}{azul:02X}"

    print("COLOR DEL ICONO")
    print(f"ARGB: 0x{COLOR_ICONO:08X}")
    print(f"Rojo: {rojo} {rojo:08b} {rojo:02X}")
    print(f"Verde: {verde} {verde:08b} {verde:02X}")
    print(f"Azul: {azul} {azul:08b} {azul:02X}")
    print(f"Opacidad: {opacidad:.1f} %")
    print(f"Para CSS: {color_css}")


def opcion_7_tipos() -> None:
    """Muestra tipo y valor de varios datos y conversiones."""
    media = ESTRELLAS / VALORACIONES
    permisos_camaraa = (PERMISOS & PERMISO_CAMARA) != 0
    texto_descargas = str(DESCARGAS)
    mayor = VERSION_MAYOR << DESPLAZAMIENTO_MAYOR
    menor = VERSION_MENOR << DESPLAZAMIENTO_MENOR
    codigo = mayor | menor | VERSION_PARCHE
    print("TIPOS DE DATOS")
    print(f"NOMBRE: {type(NOMBRE)} {NOMBRE}")
    print(f"DESCARGAS: {type(DESCARGAS)} {DESCARGAS}")
    print(f"PRECIO: {type(PRECIO)} {PRECIO}")
    print(f"media: {type(media)} {media}")
    print(f"pide_camara: {type(permisos_camaraa)} {permisos_camaraa}")
    print(f"texto_descargas: {type(texto_descargas)} {texto_descargas}")
    print(f"codigo: {type(codigo)} {codigo}")


def opcion_8_redondeo() -> None:
    """Compara round() con el redondeo de la valoracion media."""
    media = ESTRELLAS / VALORACIONES
    media_decimal = Decimal(str(media))
    plantilla_1 = Decimal(PLANTILLA_UNDECIMAL)
    plantilla_2 = Decimal(PLANTILLA_DOSDECIMALES)
    round_1 = round(media, UNDECIMAL)
    round_2 = round(media, DOSDECIMALES)
    escolar_1 = media_decimal.quantize(plantilla_1, rounding=ROUND_HALF_UP)
    escolar_2 = media_decimal.quantize(plantilla_2, rounding=ROUND_HALF_UP)
    print("REDONDEO DE LA VALORACIÓN MEDIA")
    print(f"Valor exacto: {media}")
    print(f"round(), 1 dec.: {round_1}")
    print(f"Escolar, 1 dec.: {escolar_1}")
    print(f"round(), 2 dec.: {round_2}")
    print(f"Escolar, 2 dec.: {escolar_2}")


def opcion_9_ficha() -> None:
    """Muestra la ficha completa reutilizando las opciones 1 a 4."""
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
    """Muestra el docstring, versión, autores y versión de Python."""
    descripcion = __doc__.strip() if __doc__ else ""
    version_python = platform.python_version()
    print("ACERCA DE")
    print(descripcion)
    print(f"Versión: {VERSION_PROGRAMA}")
    print(f"Autores: {AUTORES}")
    print(f"Python: {version_python}")


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
