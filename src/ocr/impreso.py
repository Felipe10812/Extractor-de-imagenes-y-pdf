import easyocr

class ImpresoOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['es', 'en'], gpu=False)  # Desactivar GPU para evitar problemas de compatibilidad

    def reconocer_texto_impreso(self, imagen):
        resultados = self.reader.readtext(imagen, detail=0,paragraph=True)
        texto = "\n".join(resultados)
        if not texto.strip():
            raise ValueError("No se pudo reconocer texto impreso en la imagen.")
        return texto.strip()