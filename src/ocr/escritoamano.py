import easyocr

class EscritoManoOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['es', 'en'], gpu=False)  # Desactivar GPU para evitar problemas de compatibilidad

    def reconocer_texto_escrito_mano(self, imagen):
        resultados = self.reader.readtext(imagen, detail=0, paragraph=True)
        if not resultados:
            raise ValueError("No se pudo reconocer texto manuscrito en la imagen.")

        # Unimos los párrafos/líneas detectados con un salto de línea.
        texto_final = "\n".join(resultados)
        
        return texto_final