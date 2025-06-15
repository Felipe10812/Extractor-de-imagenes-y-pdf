import easyocr

class ImpresoOCR:
    def __init__(self):
        self.reader = easyocr.Reader(['es', 'en'], gpu=False)  # Usa CPU para evitar problemas de GPU

    def reconocer_texto_impreso(self, imagen):
        try:
            resultados = self.reader.readtext(imagen, detail=1)
            if not resultados:
                raise ValueError("No se pudo reconocer texto impreso en la imagen.")

            # Ordenar los resultados por la coordenada Y (de arriba a abajo)
            resultados.sort(key=lambda x: x[0][0][1])

            lineas = []
            linea_actual = []
            umbral = 15  # Ajusta este valor según el tamaño de tus líneas

            for i, (caja, texto, conf) in enumerate(resultados):
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

            return "\n".join(lineas).strip()
        except Exception as e:
            print(f"Error al procesar la imagen: {e}")
            return None