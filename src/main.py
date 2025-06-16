# filepath: /image-pdf-scanner/image-pdf-scanner/src/main.py
import os
from datetime import datetime
from scanner.scanner_imagen import ImagenScanner
from scanner.scanner_pdf import PDFScanner

def guardar_texto(texto, tipo):
    nombre_carpeta = os.path.join(os.path.dirname(__file__), "respuestas")
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)

    nombre_archivo = datetime.now().strftime(f"{tipo}_%Y-%m-%d_%H-%M-%S.txt")
    ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print(f"\nEl texto se guardó en el archivo: {nombre_archivo}")

def main():
    print("Bienvenido al escáner de imágenes y PDF")
    while True:
        print("Escoja una opción:")
        print(" 1- Escanear una imagen \n 2- Escanear un PDF")
        
        opcion = input("Ingrese su elección (1 o 2): ").strip()

        if opcion == '1':
            imagen = input("Ingrese la ruta del archivo de imagen: ").strip()
            image_scanner = ImagenScanner()

            try:
                if not os.path.exists(imagen):
                    raise FileNotFoundError("La imagen no existe.")

                scanned_text = image_scanner.escanear_imagen(imagen)

                if scanned_text and scanned_text.strip():
                    guardar_texto(scanned_text, "imagen")
                else:
                    print("\nNo se reconoció texto en la imagen. Intente con otra imagen o verifique la calidad.")
            except FileNotFoundError as fnf:
                print(f"\n{fnf}")
            except ValueError as ve:
                print(f"\n{ve}")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {e}")
            break

        elif opcion == '2':
            ruta_pdf = input("Ingrese la ruta del archivo PDF: ").strip()
            pdf_scanner = PDFScanner()

            try:
                if not os.path.exists(ruta_pdf):
                    raise FileNotFoundError("El archivo PDF no existe.")

                scanned_text = pdf_scanner.scan_pdf(ruta_pdf)

                if scanned_text and scanned_text.strip():
                    guardar_texto(scanned_text, "PDF")
                else:
                    print("\nNo se reconoció texto en el PDF. Intente con otro archivo o verifique la calidad.")
            except FileNotFoundError as fnf:
                print(f"\n{fnf}")
            except ValueError as ve:
                print(f"\n{ve}")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {e}")
            break

        else:
            print("Opción no válida. Por favor, elija 1 o 2.\n")

if __name__ == "__main__":
    main()