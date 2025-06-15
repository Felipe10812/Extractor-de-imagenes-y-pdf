from pdf2image import convert_from_path
from ocr.impreso import ImpresoOCR

class PDFScanner:
    def escanear_pdf(self, ruta_pdf):
        paginas = convert_from_path(ruta_pdf)
        ocr = ImpresoOCR()
        texto_completo = ""
        for i, pagina in enumerate(paginas):
            ruta_pagina = f"pagina_{i + 1}.png"
            pagina.save(ruta_pagina, "PNG")
            texto = ocr.reconocer_texto_impreso(ruta_pagina)
            texto_completo += f"Página {i + 1}:\n{texto}\n\n"
        return texto_completo.strip()