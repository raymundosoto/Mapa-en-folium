# Generador de Rutas Aleatorias (Grafo Cerrado)

Este proyecto es una aplicación web construida con **Flask** que permite generar rutas aleatorias en un mapa, calculando la distancia total de la ruta cerrada entre ubicaciones aleatorias. La aplicación usa **Folium** para renderizar mapas interactivos, y **Geopy** para obtener información geográfica sobre las ubicaciones generadas.

## Descripción

La aplicación genera un conjunto de ubicaciones aleatorias dentro de un mapa global, conecta esas ubicaciones formando un **grafo cerrado**, y calcula la distancia total de la ruta. Cada ubicación generada tiene un marcador en el mapa con información sobre la latitud, longitud y nombre del lugar (obtenido a través de la geolocalización). La ruta generada se visualiza en el mapa, y también se puede descargar como un archivo HTML.

## Características

- **Generación de rutas aleatorias**: Se generan 10 ubicaciones aleatorias (latitud y longitud) en el mundo.
- **Mapa interactivo**: El mapa se muestra usando **Folium** y está centrado en la ruta generada.
- **Cálculo de distancia**: Se calcula la distancia total de la ruta cerrada entre todas las ubicaciones generadas usando la fórmula de **geodesic** de la librería **Geopy**.
- **Descarga del mapa**: El mapa generado se puede descargar como un archivo HTML.
- **Geolocalización**: Para cada ubicación generada, se obtiene el nombre del lugar mediante la API de **Geopy**.

## Estructura de Archivos

- `app.py`: El archivo principal de la aplicación Flask. Define las rutas y la lógica del servidor, incluyendo la generación de ubicaciones aleatorias, el cálculo de distancias y la creación del mapa.
- `index.html`: La plantilla HTML que se renderiza en el navegador. Presenta el formulario para generar una ruta, muestra el mapa generado, lista las ubicaciones y la distancia total.
- `style.css`: El archivo de estilos CSS que define la apariencia de la aplicación web, con un diseño simple y moderno.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado **Python 3.x** y las siguientes librerías:

- Flask
- Folium
- Geopy

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install Flask folium geopy

## Uso

1. **Clona este repositorio** en tu máquina local:
   - Abre una terminal y ejecuta:
     ```bash
     git clone https://github.com/tu-usuario/Generador-de-Rutas.git
     ```

2. **Navega al directorio del proyecto**:
   - Cambia al directorio del proyecto:
     ```bash
     cd Generador-de-Rutas
     ```

3. **Instala las dependencias** necesarias con `pip`:
   - Ejecuta el siguiente comando para instalar las bibliotecas requeridas:
     ```bash
     pip install Flask folium geopy
     ```

4. **Ejecuta la aplicación Flask**:
   - En la terminal, corre el siguiente comando:
     ```bash
     python app.py
     ```

5. **Abre tu navegador web**:
   - Dirígete a la siguiente URL en tu navegador:
     ```
     http://127.0.0.1:5000/
     ```

6. **Genera una ruta aleatoria**:
   - Haz clic en el botón **"Generar Ruta"** para crear una ruta aleatoria.
   - El mapa generado aparecerá en la página, junto con una lista de las ubicaciones y la distancia total de la ruta cerrada.

7. **Descarga el mapa generado**:
   - Haz clic en el botón **"Descargar Mapa"** para guardar el mapa como un archivo HTML en tu dispositivo.
