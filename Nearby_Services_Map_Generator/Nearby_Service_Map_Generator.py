import requests
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from collections import Counter

def find_services(lat, lon, radio=1000):

    """
    Generates a map with services near a geographic point.

    Args:
    lat (float): Latitude of the center point.
    lon (float): Longitude of the center point.
    radius (int, optional): Search radius in meters. Default is 1000.

    Returns:
    folium.Map: Interactive map with nearby services.

    """
    query = f"""
    [out:json][timeout:25];
    (
      node["shop"="supermarket"](around:{radio},{lat},{lon});
      way["shop"="supermarket"](around:{radio},{lat},{lon});
      relation["shop"="supermarket"](around:{radio},{lat},{lon});

      node["name"~"Lider"](around:{radio},{lat},{lon});
      way["name"~"Lider"](around:{radio},{lat},{lon});
      relation["name"~"Lider"](around:{radio},{lat},{lon});

      node["name"~"Jumbo"](around:{radio},{lat},{lon});
      way["name"~"Jumbo"](around:{radio},{lat},{lon});
      relation["name"~"Jumbo"](around:{radio},{lat},{lon});

      node["name"~"Tottus"](around:{radio},{lat},{lon});
      way["name"~"Tottus"](around:{radio},{lat},{lon});
      relation["name"~"Tottus"](around:{radio},{lat},{lon});

      node["name"~"Santa Isabel"](around:{radio},{lat},{lon});
      way["name"~"Santa Isabel"](around:{radio},{lat},{lon});
      relation["name"~"Santa Isabel"](around:{radio},{lat},{lon});

      node["amenity"="hospital"](around:{radio},{lat},{lon});
      way["amenity"="hospital"](around:{radio},{lat},{lon});
      node["amenity"="clinic"](around:{radio},{lat},{lon});
      way["amenity"="clinic"](around:{radio},{lat},{lon});

      node["shop"="mall"](around:{radio},{lat},{lon});
      way["shop"="mall"](around:{radio},{lat},{lon});
      node["amenity"="marketplace"](around:{radio},{lat},{lon});
      way["amenity"="marketplace"](around:{radio},{lat},{lon});

      node["railway"="station"](around:{radio},{lat},{lon});
      way["railway"="station"](around:{radio},{lat},{lon});
      node["station"="subway"](around:{radio},{lat},{lon});
      node["public_transport"="station"](around:{radio},{lat},{lon});

      node["amenity"="fuel"](around:{radio},{lat},{lon});
      way["amenity"="fuel"](around:{radio},{lat},{lon});
    );
    out center;
    """

    url = "https://overpass-api.de/api/interpreter"
    response = requests.get(url, params={"data": query})

    if response.status_code != 200:
        raise Exception("Error in query Overpass API")

    data = response.json()["elements"]

    lugares = []
    for el in data:
        tags = el.get("tags", {})
        latitud = el.get("lat") or el.get("center", {}).get("lat")
        longitud = el.get("lon") or el.get("center", {}).get("lon")
        if latitud and longitud:
            tipo = (
                tags.get("shop")
                or tags.get("amenity")
                or tags.get("railway")
                or tags.get("station")
                or tags.get("public_transport")
                or "Otro"
            )
            lugares.append({
                "tipo": tipo,
                "name": tags.get("name", "no name"),
                "lat": latitud,
                "lon": longitud
            })

    df = pd.DataFrame(lugares)

    # Mapa base
    mapa = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Circle([lat, lon], radius=radio, color='blue', fill=True, fill_opacity=0.1).add_to(mapa)
    folium.Marker([lat, lon], popup="Initial Point", icon=folium.Icon(color="red", icon="home")).add_to(mapa)

    # Icons
    icon_map = {
        'supermarket': 'shopping-cart',
        'clinic': 'plus-square',
        'hospital': 'plus',
        'fuel': 'gas-pump',
        'mall': 'store',
        'marketplace': 'store',
        'railway': 'train',
        'station': 'train',
        'subway': 'train',
        'public_transport': 'train'
    }

    emoji_map = {
        'supermarket': '🛒',
        'clinic': '➕',
        'hospital': '➕',
        'fuel': '⛽',
        'mall': '🏬',
        'marketplace': '🏬',
        'railway': '🚆',
        'station': '🚆',
        'subway': '🚆',
        'public_transport': '🚆',
        'Otro': '📍'
    }

    counter = Counter()
    marker_cluster = MarkerCluster().add_to(mapa)

    for _, row in df.iterrows():
        tipo = row["tipo"]
        icono = icon_map.get(tipo, "map-marker")
        counter[tipo] += 1

        folium.Marker(
            location=[row["lat"], row["lon"]],
            popup=f'{row["name"]} ({tipo})',
            icon=folium.Icon(color="blue", icon=icono, prefix="fa")
        ).add_to(marker_cluster)

    # Summary in popup
    resumen = "<b>📊 Services found:</b><br>"
    for tipo, cantidad in counter.most_common():
        emoji = emoji_map.get(tipo, "📍")
        resumen += f" - {emoji} {tipo}: {cantidad}<br>"

    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(resumen, max_width=300),
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(mapa)

    return mapa