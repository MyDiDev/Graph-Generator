# Graph Generator Tool

Una herramienta en Python para generar y automatizar gráficos a partir de archivos `.xlsx`, `.csv` y `.json`. Utiliza bibliotecas populares como `pandas` y `matplotlib` para ofrecer análisis y visualizaciones rápidas y eficientes.

## Instalación

Usa el administrador de paquetes [pip](https://pip.pypa.io/en/stable/) para instalar las dependencias necesarias.

Clonar El repositorio

```bash
git clone https://github.com/MyDiDev/Graph-Generator.git
```

Ingresar a la Carpeta Generada

```bash
cd Graph-Generator
```

Crear y Activar Entorno Virtual

```bash
python3 -m venv env
```

- Windows

```bash
env/scripts/activate
```

- MacOs / Linux

```bash
env/bin/activate
```

- Instalar Paquetes

```bash
pip install -r requirements.txt
```

## Uso

```python
python3 file.py
```

![Use Case](imgs\image.png)

### Funciones

- **`1 - Line`**:

  - Lee el archivo desde el directorio dado (`.csv`, `.xlsx`, `.json`) y genera un gráfico de líneas por defecto.
  - El archivo debe contener datos numéricos adecuados para la creación de gráficos.

- **`2 - bar`**:

  - Genera un gráfico de barras a partir de los datos proporcionados en el archivo.

- **`3 - Barh`**:

  - Genera un gráfico de líneas a partir de los datos proporcionados en el archivo.

- **`4 - Hist`**:

  - Genera un gráfico de dispersión utilizando los datos numéricos del archivo.

- **`5 - Box`**:

  - Genera un gráfico de dispersión utilizando los datos numéricos del archivo.

- **`6 - Area`**:
  - Genera un gráfico de dispersión utilizando los datos numéricos del archivo.

### Ejemplo de uso

![Use Case](imgs\image2.png)

![Use Case](imgs\image3.png)

## Requisitos

- **Python 3.x**: Especificamente 3.11.9
- **pandas**: Para la manipulación de datos.
- **matplotlib**: Para la generación de gráficos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas realizar un cambio importante, abre un _issue_ primero para discutir lo que te gustaría cambiar. Asegúrate de actualizar las pruebas si es necesario.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

---

Este README describe las funcionalidades principales de la herramienta de generación de gráficos y cómo usarla con diferentes tipos de archivos. También proporciona ejemplos básicos y detallados de cómo generar los gráficos.
