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

```


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


## Instalación en un entorno virtual de Python

Sigue estos pasos para instalar y ejecutar el proyecto en un entorno virtual:

1. **Clonar el repositorio**:
   - Ejecuta el siguiente comando para clonar el repositorio:
     ```bash
     git clone https://github.com/tu_usuario/tu_repositorio.git
     ```

2. **Acceder a la carpeta del proyecto**:
   - Navega al directorio del proyecto con:
     ```bash
     cd nombre_del_proyecto
     ```

3. **Crear un entorno virtual (opcional)**:
   - Para **Windows**, crea y activa un entorno virtual:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Para **Mac/Linux**, crea y activa un entorno virtual:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Instalar las dependencias**:
   - Instala todas las dependencias necesarias desde el archivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

5. **Ejecutar el proyecto**:
   - Una vez instaladas las dependencias, ejecuta el proyecto con:
     ```bash
     python app.py
     ```
   - El servidor se iniciará y podrás acceder a la aplicación en tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000).


## Créditos

- **Desarrollado por**: Raymundo Soto Soto
- **Librerías utilizadas**:
  - [Flask](https://flask.palletsprojects.com/) - Framework para el desarrollo de aplicaciones web.
  - [Folium](https://python-visualization.github.io/folium/) - Librería para la creación de mapas interactivos.
  - [Geopy](https://geopy.readthedocs.io/en/stable/) - Librería para realizar geocodificación y cálculos de distancias geográficas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Ejemplos
![imagen](https://github.com/user-attachments/assets/0ba3959d-c4dc-4192-b710-51b0a97f81f0)

![imagen](https://github.com/user-attachments/assets/7647552b-6e00-41a4-a5a1-9d0ec388b8cc)





