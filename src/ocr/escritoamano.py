import easyocr

class EscritoManoOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['es', 'en'])

    def reconocer_texto_escrito_mano(self, imagen):
        resultados = self.reader.readtext(imagen, detail=1, paragraph=True)
        if not resultados:
            raise ValueError("No se pudo reconocer texto manuscrito en la imagen.")

        # Ordenar los resultados por la coordenada Y (de arriba a abajo)
        resultados.sort(key=lambda x: x[0][0][1])

        lineas = []
        linea_actual = []
        umbral = 20  # Puedes ajustar este valor según tus imágenes

        for i, (caja, texto, conf) in enumerate(resultados):
            texto = texto.strip()
            if not texto:
                continue
            y = caja[0][1]
            if i == 0:
                linea_actual.append(texto)
                y_anterior = y
            else:
                if abs(y - y_anterior) > umbral:
                    lineas.append(" ".join(linea_actual))
                    linea_actual = [texto]
                else:
                    linea_actual.append(texto)
                y_anterior = y
        if linea_actual:
            lineas.append(" ".join(linea_actual))

        texto_final = "\n".join(lineas).strip()
        if not texto_final:
            raise ValueError("No se pudo interpretar texto manuscrito en la imagen.")
        return texto_final