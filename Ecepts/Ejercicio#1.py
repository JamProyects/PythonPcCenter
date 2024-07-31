def contar_palabras(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            numero_palabras = len(palabras)
            return numero_palabras
    except FileNotFoundError:
        return "El archivo no se encontró."
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Ejemplo de uso
ruta_archivo = 'ruta/al/archivo.txt'
numero_palabras = contar_palabras(ruta_archivo)
print(f"El número de palabras en el archivo es: {numero_palabras}")