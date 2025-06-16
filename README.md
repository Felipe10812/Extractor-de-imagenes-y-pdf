# Escáner de Imágenes y PDF

Este proyecto es un sistema en Python que permite escanear imágenes y archivos PDF para extraer texto, ya sea impreso o manuscrito, utilizando reconocimiento óptico de caracteres (OCR) con la librería [EasyOCR](https://github.com/JaidedAI/EasyOCR).

## Características

- **Escaneo de Imágenes:**  
  Permite seleccionar una imagen y elegir si el texto es impreso o manuscrito. El sistema procesa la imagen y extrae el texto respetando la estructura visual original lo mejor posible.

- **Escaneo de PDF:**  
  Convierte cada página del PDF en una imagen y extrae el texto impreso de cada una, mostrando y guardando los resultados por página.

- **Reconocimiento de Texto Manuscrito e Impreso:**  
  Usa modelos de EasyOCR para español e inglés, agrupando los fragmentos de texto por líneas según su posición en la imagen.

- **Gestión de Resultados:**  
  El texto extraído se guarda automáticamente en la carpeta `src/respuestas` con un nombre que indica el tipo de archivo y la fecha/hora del escaneo.

- **Manejo de Errores:**  
  El sistema informa si no se reconoce texto, si el archivo no existe o si ocurre algún error inesperado.

## Estructura del Proyecto

```
src/
├── main.py
├── ocr/
│   ├── __init__.py
│   ├── escritoamano.py
│   └── impreso.py
├── respuestas/
│   └── ... (archivos de texto generados)
├── scanner/
│   ├── __init__.py
│   ├── scanner_imagen.py
│   └── scanner_pdf.py
└── utils/
    ├── __init__.py
    └── file_utils.py
```

## Instalación

1. Clona el repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install easyocr opencv-python pdf2image numpy
   ```
   Además, instala [poppler](https://github.com/oschwartz10612/poppler-windows/releases/) para que `pdf2image` funcione en Windows.

## Uso

Ejecuta el programa principal:
```bash
python src/main.py
```
Sigue las instrucciones en pantalla para seleccionar el tipo de archivo y la ruta. El texto extraído se mostrará y se guardará automáticamente en la carpeta `src/respuestas`.

## Notas

- Los archivos generados en `src/respuestas` están ignorados en el control de versiones (`.gitignore`).
- La carpeta `utils` contiene funciones auxiliares para manejo de archivos binarios.
- Los archivos `__init__.py` permiten que las carpetas sean paquetes de Python y facilitan la importación de módulos.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.