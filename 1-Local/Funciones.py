# Funciones a utilizar en el proyecto
import pandas as pd
from re import search



# Función para extraer solo los valores numéricos de una cadena usando expresiones regulares
def extraer_valor_numerico(cadena):
    match = search(r'\d+', str(cadena))  # Encuentra una secuencia de dígitos en la cadena
    if match:
        return int(match.group())  # Devuelve el valor numérico encontrado como entero
    else:
        return None  # Si no se encuentra ningún valor numérico, devuelve None


# Función para convertir de kilómetros a millas
def convert_km_to_mile(value):
    # 1 km = 0.621371 millas
    result = value * 0.621371
    return round(result, 2)  # Redondear el resultado a 2 decimales


# Función que convierte litros a galones
def convert_l_to_gal(x):
    # 1 litro = 0.264172 galones
    result = x * 0.264172
    return round(result, 2)  # Redondear el resultado a 2 decimales


# Función para asignar ubicaciones a boroughs
def asignar_borough(ubicacion):

    # Cargamos las ubicaciones de la columna 'Geo Place Name' en un diccionario clasificando por borough
    codigo_borough = {
        'Manhattan': ['Alphabet City', 'Battery Park', 'Battery Park City', 'Bloomingdale', 'Central Harlem', 'Central Harlem North',
                      'Central Park', 'Chinatown', 'Clinton East', 'Clinton West', 'East Chelsea', 'East Harlem North', 'East Harlem South',
                      'East Village', 'Financial District North', 'Financial District South', 'Flatiron', 'Garment District',
                      "Governor's Island/Ellis Island/Liberty Island", "Governor's Island/Ellis Island/Liberty Island",
                      "Governor's Island/Ellis Island/Liberty Island", 'Gramercy', 'Greenwich Village North', 'Greenwich Village South',
                      'Hamilton Heights', 'Highbridge Park', 'Hudson Sq', 'Inwood', 'Inwood Hill Park', 'Kips Bay', 'Lenox Hill East',
                      'Lenox Hill West', 'Lincoln Square East', 'Lincoln Square West', 'Little Italy/NoLiTa', 'Lower East Side',
                      'Manhattan Valley', 'Manhattanville', 'Marble Hill', 'Meatpacking/West Village West', 'Midtown Center', 'Midtown East',
                      'Midtown North', 'Midtown South', 'Morningside Heights', 'Murray Hill', 'Penn Station/Madison Sq West', 'Randalls Island',
                      'Roosevelt Island', 'Seaport', 'SoHo', 'Stuy Town/Peter Cooper Village', 'Sutton Place/Turtle Bay North',
                      'Times Sq/Theatre District', 'TriBeCa/Civic Center', 'Two Bridges/Seward Park', 'UN/Turtle Bay South', 'Union Sq',
                      'Upper East Side North', 'Upper East Side South', 'Upper West Side North', 'Upper West Side South',
                      'Washington Heights North', 'Washington Heights South', 'West Chelsea/Hudson Yards', 'West Village', 'World Trade Center',
                      'Yorkville East', 'Yorkville West'],
        
        'Brooklyn': ['Bath Beach', 'Bay Ridge', 'Bedford', 'Bensonhurst East', 'Bensonhurst West', 'Boerum Hill', 'Borough Park',
                     'Brighton Beach', 'Brooklyn Heights', 'Brooklyn Navy Yard', 'Brownsville', 'Bushwick North', 'Bushwick South', 'Canarsie',
                     'Carroll Gardens', 'Clinton Hill', 'Cobble Hill', 'Columbia Street', 'Coney Island', 'Crown Heights North',
                     'Crown Heights South', 'Cypress Hills', 'Downtown Brooklyn/MetroTech', 'DUMBO/Vinegar Hill', 'Dyker Heights',
                     'East Flatbush/Farragut', 'East Flatbush/Remsen Village', 'East New York', 'East New York/Pennsylvania Avenue',
                     'East Williamsburg', 'Erasmus', 'Flatbush/Ditmas Park', 'Flatlands', 'Fort Greene', 'Gowanus', 'Gravesend',
                     'Green-Wood Cemetery', 'Greenpoint', 'Homecrest', 'Kensington', 'Madison', 'Manhattan Beach',
                     'Marine Park/Floyd Bennett Field', 'Marine Park/Mill Basin', 'Midwood', 'Ocean Hill', 'Ocean Parkway South',
                     'Park Slope', 'Prospect-Lefferts Gardens', 'Prospect Heights', 'Prospect Park', 'Red Hook', 'Sheepshead Bay',
                     'South Williamsburg', 'Starrett City', 'Stuyvesant Heights', 'Sunset Park East', 'Sunset Park West',
                     'Williamsburg (North Side)', 'Williamsburg (South Side)', 'Windsor Terrace'],

        'Queens': ['Jamaica Bay', 'Astoria', 'Astoria Park', 'Auburndale', 'Baisley Park', 'Bay Terrace/Fort Totten', 'Bayside', 'Bellerose',
                   'Breezy Point/Fort Tilden/Riis Beach', 'Briarwood/Jamaica Hills', 'Broad Channel', 'Cambria Heights', 'College Point', 'Corona',
                   'Corona', 'Douglaston', 'East Elmhurst', 'East Flushing', 'Elmhurst', 'Elmhurst/Maspeth', 'Far Rockaway', 'Flushing',
                   'Flushing Meadows-Corona Park', 'Forest Hills', 'Forest Park/Highland Park', 'Fresh Meadows', 'Glen Oaks', 'Glendale',
                   'Hammels/Arverne', 'Hillcrest/Pomonok', 'Hollis', 'Howard Beach', 'Jackson Heights', 'Jamaica', 'Jamaica Estates', 'JFK Airport',
                   'Kew Gardens', 'Kew Gardens Hills', 'LaGuardia Airport', 'Laurelton', 'Long Island City/Hunters Point',
                   'Long Island City/Queens Plaza', 'Maspeth', 'Middle Village', 'Murray Hill-Queens', 'North Corona', 'Oakland Gardens',
                   'Old Astoria', 'Ozone Park', 'Queens Village', 'Queensboro Hill', 'Queensbridge/Ravenswood', 'Rego Park', 'Richmond Hill',
                   'Ridgewood', 'Rockaway Park', 'Rosedale', 'Saint Albans', 'Saint Michaels Cemetery/Woodside', 'South Jamaica', 'South Ozone Park',
                   'Springfield Gardens North', 'Springfield Gardens South', 'Steinway', 'Sunnyside', 'Whitestone', 'Willets Point', 'Woodhaven',
                   'Woodside'],

        'Bronx': ['Allerton/Pelham Gardens', 'Bedford Park', 'Belmont', 'Bronx Park', 'Bronxdale', 'City Island', 'Claremont/Bathgate',
                  'Co-Op City', 'Country Club', 'Crotona Park', 'Crotona Park East', 'East Concourse/Concourse Village', 'East Tremont',
                  'Eastchester', 'Fordham South', 'Highbridge', 'Hunts Point', 'Kingsbridge Heights', 'Longwood', 'Melrose South',
                  'Morrisania/Melrose', 'Mott Haven/Port Morris', 'Mount Hope', 'Norwood', 'Parkchester', 'Pelham Bay', 'Pelham Bay Park',
                  'Pelham Parkway', 'Rikers Island', 'Riverdale/North Riverdale/Fieldston', 'Schuylerville/Edgewater Park', 'Soundview/Bruckner',
                  'Soundview/Castle Hill', 'Spuyten Duyvil/Kingsbridge', 'University Heights/Morris Heights', 'Van Cortlandt Park',
                  'Van Cortlandt Village', 'Van Nest/Morris Park', 'West Concourse', 'West Farms/Bronx River', 'Westchester Village/Unionport',
                  'Williamsbridge/Olinville', 'Woodlawn/Wakefield'],

        'Staten Island': ['Arden Heights', 'Arrochar/Fort Wadsworth', 'Bloomfield/Emerson Hill', 'Charleston/Tottenville',
                          "Eltingville/Annadale/Prince's Bay", 'Freshkills Park', 'Great Kills', 'Great Kills Park', 'Grymes Hill/Clifton',
                          'Heartland Village/Todt Hill', 'Mariners Harbor', 'New Dorp/Midland Beach', 'Oakwood', 'Port Richmond',
                          'Rossville/Woodrow', 'Saint George/New Brighton', 'South Beach/Dongan Hills', 'Stapleton', 'West Brighton',
                          'Westerleigh'],

        'EWR': ['Newark Airport']}


    for borough, palabras_clave in codigo_borough.items():
        if any(palabra_clave in ubicacion for palabra_clave in palabras_clave):
            return borough
    return "Unknown"


# Función que modifica los valores de la columna 'Engine Sound' haciendo que -1 sea Bajo, 0 sea Medio y 1 sea Alto
def engine_sound(engine):
    if engine == -1:
        return 'Low'
    elif engine == 0:
        return 'Medium'
    elif engine == 1:
        return 'High'
    else:
        return 'Unknown'


# Función que reemplaza los valores de la columna 'Fuel' por su valor del diccionario B = Electric
def fuel(fuel):
    if fuel == 'B':
        return 'Electric'
    else:
        return fuel


# Función que asigna el tipo de combustible a cada vehículo de acuerdo al diccionario del dataset
# X o Z= Gasoline, D = diesel
def fuel_type(fuel):
    if fuel == 'X' or fuel == 'Z':
        return 'Gasoline'
    elif fuel == 'D':
        return 'Diesel'
    else:
        return 'Unknown'


# Función para dividir la columna 'latitude' en 'Date' y 'Time'
def split_date_time(value):
    # Dividimos la cadena en la T
    date, time = value.split('T')
    return date, time


# Función que nos devuelve el nombre del Borough en 2 nuevas columnas llamadas pickup_borough y dropoff_borough
def get_borough(location_id):

    # Agrupamos los PULocationID y DOLocationID de acuerdo a su Borough correspondiente
    zones = {
        'Manhattan' : [4, 12, 13, 24, 41, 42, 43, 45, 48, 50, 68, 74, 75, 79, 87, 88, 90, 100, 103, 103, 103, 107, 113, 114, 116, 120, 125,
                      127, 128, 137, 140, 141, 142, 143, 144, 148, 151, 152, 153, 158, 161, 162, 163, 164, 166, 170, 186, 194, 202, 209, 211,
                      224, 229, 230, 231, 232, 233, 234, 236, 237, 238, 239, 243, 244, 246, 249, 261, 262, 263],


        'Brooklyn' : [11, 14, 17, 21, 22, 25, 26, 29, 33, 34, 35, 36, 37, 39, 40, 49, 52, 54, 55, 61, 62, 63, 65, 66, 67, 71, 72, 76, 77, 80,
                     85, 89, 91, 97, 106, 108, 111, 112, 123, 133, 149, 150, 154, 155, 165, 177, 178, 181, 188, 189, 190, 195, 210, 217, 222,
                     225, 227, 228, 255, 256, 257],


        'Queens' : [2, 7, 8, 9, 10, 15, 16, 19, 27, 28, 30, 38, 53, 56, 56, 64, 70, 73, 82, 83, 86, 92, 93, 95, 96, 98, 101, 102, 117, 121,
                   122, 124, 129, 130, 131, 132, 134, 135, 138, 139, 145, 146, 157, 160, 171, 173, 175, 179, 180, 191, 192, 193, 196, 197,
                   198, 201, 203, 205, 207, 215, 216, 218, 219, 223, 226, 252, 253, 258, 260],


        'Bronx' : [3, 18, 20, 31, 32, 46, 47, 51, 58, 59, 60, 69, 78, 81, 94, 119, 126, 136, 147, 159, 167, 168, 169, 174, 182, 183, 184,
                   185, 199, 200, 208, 212, 213, 220, 235, 240, 241, 242, 247, 248, 250, 254, 259],
    
        'Staten Island' : [5, 6, 23, 44, 84, 99, 109, 110, 115, 118, 156, 172, 176, 187, 204, 206, 214, 221, 245, 251],
    
    
        'EWR' : [1]}
    
    for borough, ids in zones.items():
        if location_id in ids:
            return borough
    return 'Unknown'


# Función que agrega la columna 'BoroughID' a la tabla de contaminación y clasifica los boroughs
# asignando los números 1 (Manhattan), 2 (Brooklyn), 3 (Queens), 4 (Bronx) y 5 (Staten Island)
def borough_id(borough):
    if borough == 'Manhattan':
        return 1
    elif borough == 'Brooklyn':
        return 2
    elif borough == 'Queens':
        return 3
    elif borough == 'Bronx':
        return 4
    elif borough == 'Staten Island':
        return 5
    else:
        return 0


# Función que crea una columna llamada 'Miles per gallon (mpg)' y la rellena con los valores de la columna Alternative Fuel Economy City
# y en caso de que sea nulo, rellena con los valores de la columna Conventional Fuel Economy City
def mpg_city(row):
    if pd.isnull(row['Alternative Fuel Economy City']):
        return row['Conventional Fuel Economy City']
    else:
        return row['Alternative Fuel Economy City']








