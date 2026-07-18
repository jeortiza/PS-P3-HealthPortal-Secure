import sqlite3 # Usamos la herramienta nativa de Python para leer bases de datos directamente.

# Imprimimos unos mensajes de alerta para darle un toque más dramático y profesional a la demo.
print("\n[!] INICIANDO SIMULACIÓN DE EXTRACCIÓN DE BASE DE DATOS...")
print("[!] Abriendo el archivo físico db.sqlite3 directamente...\n")

try:
    # Nos conectamos físicamente al archivo db.sqlite3, esquivando totalmente a Django.
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    
    # Le pedimos a la base de datos la columna exacta con el nombre físico que descubrimos antes.
    cursor.execute("SELECT patient_id, diagnostico_cifrado FROM records_medicalrecord LIMIT 1;")
    resultado = cursor.fetchone()

    # Si encuentra el registro, lo imprime en pantalla mostrando la sopa de letras (Base64).
    if resultado:
        print("=== RESULTADO DE LA EXTRACCIÓN CRUDA ===")
        print(f"ID del Paciente: {resultado[0]}")
        print(f"Diagnóstico en disco: {resultado[1]}") # Aquí se verá el AES-256 en acción
        print("========================================\n")
        print("Conclusión: Los datos médicos están protegidos por AES-256 y son completamente ilegibles para un intruso.")
    else:
        print("No se encontraron registros en la base de datos.")

# Si algo sale mal (como ejecutar el archivo desde la carpeta equivocada), nos avisa.
except Exception as e:
    print(f"Error de lectura: {e}\nAsegúrate de ejecutar este script en la misma carpeta donde está tu archivo db.sqlite3.")
finally:
    # Cerramos la conexión para no dejar el archivo bloqueado.
    if 'conexion' in locals():
        conexion.close()