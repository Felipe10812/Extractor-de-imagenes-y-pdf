import cv2
import os
import numpy as np
from ocr.escritoamano import EscritoManoOCR
from ocr.impreso import ImpresoOCR

class ImagenScanner:
    def __init__(self):
        # Carpeta donde se guardarán las imágenes procesadas
        self.carpeta_guardado = os.path.join(os.path.dirname(__file__), "respuestas")
        if not os.path.exists(self.carpeta_guardado):
            os.makedirs(self.carpeta_guardado)

    def guardar_imagen(self, imagen, nombre):
        """ Guarda la imagen procesada en la carpeta respuestas. """
        ruta_guardado = os.path.join(self.carpeta_guardado, nombre)
        cv2.imwrite(ruta_guardado, imagen)

    def procesar_imagen(self, imagen):
        try:
            img = cv2.imread(imagen)

            if img is None:
                print("Error: No se pudo cargar la imagen. Verifique la ruta.")
                return None

            self.guardar_imagen(img, "1_imagen_original.jpg")

            # Conversión a escala de grises
            gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            self.guardar_imagen(gris, "2_imagen_gris.jpg")

            # Eliminación de ruido con desenfoque Gaussiano
            filtrada = cv2.GaussianBlur(gris, (5, 5), 0)
            self.guardar_imagen(filtrada, "3_imagen_filtrada.jpg")

            # Binarización adaptativa
            binaria = cv2.adaptiveThreshold(filtrada, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY, 11, 5)
            self.guardar_imagen(binaria, "4_imagen_binarizada.jpg")

            return binaria
        
        except Exception as e:
            print(f"Error inesperado al procesar la imagen: {e}")
            return None

    def escanear_imagen(self, imagen):
        print("¿El texto es impreso o escrito a mano?")
        opcion = input(" 1- Para impreso \n 2- Para escrito a mano \nIngrese su elección (1 o 2): ").strip()
        
        try:
            imagen_procesada = self.procesar_imagen(imagen)

            if imagen_procesada is None:
                print("Error: No se pudo procesar la imagen.")
                return None

            if opcion == '1':
                ocr = ImpresoOCR()
                texto = ocr.reconocer_texto_impreso(imagen)
            elif opcion == '2':
                ocr = EscritoManoOCR()
                texto = ocr.reconocer_texto_escrito_mano(imagen_procesada)
            else:
                print("Opción no válida. Por favor, elija 1 o 2.")
                return None

            return texto
        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None