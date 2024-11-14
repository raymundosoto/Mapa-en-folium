from flask import Flask, render_template, request
import folium
import random
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Función para generar ubicaciones aleatorias
def generate_random_locations(num_points):
    locations = []
    for _ in range(num_points - 1):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        locations.append((lat, lon))
    locations.append(locations[0])  # Hacer que la última ubicación sea igual a la primera para un grafo cerrado
    return locations

# Función para calcular la distancia total entre las ubicaciones
def calculate_total_distance(locations):
    total_distance = 0
    for i in range(len(locations) - 1):
        total_distance += geodesic(locations[i], locations[i + 1]).kilometers
    return total_distance

# Función para obtener el nombre del lugar usando geocodificación inversa
def get_location_name(lat, lon):
    geolocator = Nominatim(user_agent="ruta_app")
    location = geolocator.reverse((lat, lon), language='es')
    if location:
        return location.address
    return "Desconocido"

@app.route('/')
def index():
    # Al cargar por primera vez, no generamos una ruta, por lo que `locations` y `total_distance` son None
    return render_template('index.html', locations=None, total_distance=None, map_filename=None)

@app.route('/generate_route', methods=['POST'])
def generate_route():
    # Generar 10 ubicaciones aleatorias en total, con la primera y última iguales
    locations = generate_random_locations(10)

    # Crear el mapa centrado en las ubicaciones y ajustado para mostrar todas
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Añadir marcadores y unirlos con líneas en el mapa
    marker_bounds = []
    locations_with_names = []
    for i, loc in enumerate(locations):
        # Obtener el nombre del lugar usando geocodificación inversa
        location_name = get_location_name(loc[0], loc[1])
        popup_text = f"Ubicación {i + 1}: ({loc[0]:.4f}, {loc[1]:.4f}) - {location_name}"
        folium.Marker(location=loc, popup=popup_text).add_to(m)
        marker_bounds.append(loc)
        locations_with_names.append({
            "id": i + 1,
            "latitude": loc[0],
            "longitude": loc[1],
            "name": location_name
        })
        if i > 0:
            folium.PolyLine([locations[i - 1], loc], color="blue").add_to(m)

    # Ajustar la vista del mapa para mostrar todos los puntos
    m.fit_bounds(marker_bounds)

    # Definir el nombre del archivo para guardar el mapa
    map_filename = 'my_map.html'
    
    # Guardar el mapa en un archivo HTML en la carpeta 'static/maps/'
    map_path = 'static/maps/' + map_filename
    m.save(map_path)

    # Calcular la distancia total entre los puntos
    total_distance = calculate_total_distance(locations)

    # Pasar el nombre del archivo del mapa a la plantilla
    return render_template('index.html', locations=locations_with_names, total_distance=total_distance, map_filename=map_filename)

if __name__ == '__main__':
    app.run(debug=True)
