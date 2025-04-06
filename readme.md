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
source env/bin/activate
```

- Instalar Paquetes

```bash
pip install -r requirements.txt
```

## Uso

```python
python3 file.py
```

![Image](https://github.com/user-attachments/assets/1cda0703-d2ea-4f78-b21b-c677d48092d3)

### Funciones

1. **Gráfico de líneas (`Line`)**: Muestra los datos en una secuencia continua, ideal para representar tendencias a lo largo del tiempo.

2. **Gráfico de barras (`Bar`)**: Representa valores discretos mediante barras verticales, útil para comparar categorías o grupos.

3. **Gráfico de barras horizontales (`Barh`)**: Similar al gráfico de barras, pero con barras horizontales, útil cuando las etiquetas de las categorías son largas.

4. **Gráfico de dispersión (`Hist`)**: Muestra la relación entre dos variables numéricas como puntos individuales en un plano cartesiano.

5. **Gráfico de caja (`Box`)**: Muestra la distribución de los datos, incluyendo la mediana, los cuartiles y los valores atípicos.

6. **Gráfico de área (`Area`)**: Similar a un gráfico de líneas, pero con el área debajo de la línea sombreada, ideal para mostrar el volumen o la magnitud acumulada a lo largo del tiempo.
   
### Ejemplo de uso

![Image](https://github.com/user-attachments/assets/8d4a76bd-100b-44e6-b5b6-5de1d2f3e3f8)

![Image](https://github.com/user-attachments/assets/7b7f4d4e-d209-40d3-9f46-51a434688fad)

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
