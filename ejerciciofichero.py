def guardar_resumen(nombre_fichero, alumnos):
    """Ejercicio para guardar resumenes"""
    try:
        alumno = [{nombre: "Angela"}, {nota:5}]
    except FileExistsError:
        print("El archivo no existe")

if __name__ == "__main__":
    guardar_resumen()
