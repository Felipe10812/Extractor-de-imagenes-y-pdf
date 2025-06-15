from ocr.escritoamano import EscritoManoOCR
from ocr.impreso import ImpresoOCR

class ImagenScanner:
    def escanear_imagen(self, imagen):
        print("¿El texto es impreso o escrito a mano?")
        opcion = input(" 1- Para impreso \n 2- Para escrito a mano \nIngrese su elección (1 o 2): ").strip()
        
        try:
            if opcion == '1':
                ocr = ImpresoOCR()
                texto = ocr.reconocer_texto_impreso(imagen)
            elif opcion == '2':
                ocr = EscritoManoOCR()
                texto = ocr.reconocer_texto_escrito_mano(imagen)
            else:
                raise ValueError("Opción no válida. Por favor, elija 1 o 2.")
            return texto
        except ValueError as e:
            print(f"Error: {e}")