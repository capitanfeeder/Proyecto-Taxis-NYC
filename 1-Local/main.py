"""
FUNCIONES CREADAS PARA EL PROYECTO FINAL DE DATA SCIENCE DE SOY HENRY
                            - NY TAXIS - 

FUNCIONES PARA ALIMENTAR LA API
"""


# Importamos las librerías necesarias
import boto3
import pandas as pd
import pyarrow.parquet as pq
import pyarrow.fs
from s3fs import S3FileSystem
import s3fs
import joblib
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import timedelta
from pyathena import connect

# Instanciamos la aplicación FastAPI
app = FastAPI()


class InputData(BaseModel):
    pBoroughID: int
    dayofweek: int
    hour: int


# Ruta para la página de inicio
@app.get("/", response_class=HTMLResponse)
async def inicio():
    """
    Página de inicio de la API Taxis.

    Realice sus consultas.
    """
    template = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>API Taxi</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>API de consultas predictivas sobre viajes en Taxi</h1>
            <p>Bienvenido a la API de Taxis. Utiliza la ruta <strong>/predict</strong> para realizar predicciones.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=template)

# Ruta para realizar predicciones
@app.post("/predict")
def predict(data: InputData):
    """
    Endpoint para realizar predicciones.

    Permite realizar predicciones basadas en datos de entrada proporcionados en el cuerpo de la solicitud.

    Parameters:
    - data: Datos de entrada en formato JSON. Debe incluir campos específicos:
        - pBoroughID: Identificador del distrito de recogida (pickup borough). Debe ser un número entero del 1 al 6, donde:
            - 1: Manhattan
            - 2: Bronx
            - 3: Brooklyn
            - 4: Queens
            - 5: Staten Island
            - 6: EWR (Newark Airport)
        - dayofweek: Número que representa el día de la semana. Debe ser un número entero del 0 al 6, donde:
            - 0: Domingo
            - 1: Lunes
            - 2: Martes
            - 3: Miércoles
            - 4: Jueves
            - 5: Viernes
            - 6: Sábado
        - hour: Hora del día. Debe ser un número entero del 0 al 23, representando las horas en formato de 24 horas.

    Returns:
        - JSON con el resultado de la predicción indicando la probabilidad de obtener clientes o un mensaje de error si ingresó un dato erróneo.
    """
    try:
        # Especificamos las credenciales de AWS
        aws_access_key_id = 'tu_access_key_id'
        aws_secret_access_key = 'tu_secret_access_key'

        # Configuramos la conexión a S3 con las credenciales
        s3 = s3fs.S3FileSystem(key=aws_access_key_id, secret=aws_secret_access_key)

        # Especificamos la ruta del modelo en S3
        model_path = 'tu_bucket/tu_modelo'

        # Descargamos el modelo desde S3
        with s3.open(model_path, 'rb') as f:
            xgb_model = joblib.load(f)

        # Convertirmos los datos de entrada a un DataFrame
        input_data = pd.DataFrame([data.model_dump()])

        # Realizarmos la predicción
        prediction = xgb_model.predict(input_data)

        # Devolvemos la predicción como JSON
        return {"Probabilidad de conseguir pasajero": prediction.tolist()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





# Nueva ruta para obtener el top 3 de vehículos ecológicos y económicos
@app.get("/top_3_vehicles")
def top_3_vehicles(max_price_usd: float):
    """
    Endpoint para obtener el top 3 de vehículos ecológicos de acuerdo al capital.

    Parameters:
    - max_price_usd: Precio máximo en dólares para filtrar los vehículos.

    Returns:
        - JSON con el top 3 de vehículos ecológicos.
    """
    try:    
        # Especificamos las credenciales de AWS
        aws_access_key_id = 'tu_access_key_id'
        aws_secret_access_key = 'tu_secret_access_key'

        # Especificamos la ruta del archivo Parquet en S3
        s3_path = 'tu_bucket/tu_archivo'

        # Configura la conexión a S3 con las credenciales
        s3 = s3fs.S3FileSystem(key=aws_access_key_id, secret=aws_secret_access_key)

        # Abrimos el archivo Parquet directamente desde S3
        parquet_file = pq.ParquetFile(s3.open(s3_path))

        # Leemos el archivo Parquet en un DataFrame de pandas
        df = parquet_file.read().to_pandas()

        # Filtramos los vehículos por precio
        filtered_vehicles = df[df['Price (USD)'] <= max_price_usd]

        # Ordenamos los vehículos por CO2 en orden ascendente, luego por Sound Emission y finalmente por Range
        sorted_vehicles = filtered_vehicles.sort_values(by=['CO2 Emission (g/mi)', 'Sound Emission (dB)', 'Range (mi)'], ascending=[True, True, False])

        # Tomamos los tres primeros vehículos dentro del rango de precio
        top_3_vehicles = sorted_vehicles.head(3)

        # Creamos el formato de salida como una lista de diccionarios
        output_format = []
        for idx, row in enumerate(top_3_vehicles.itertuples(), start=1):
            output_format.append({
                f'Puesto {idx}': f'{row.Manufacturer} {row.Model}',
                'Precio (USD)': row._9,
                'Combustible': row.Fuel,
                'CO2': row._7,
                'dB': row._8,
                'Millas con un tanque lleno': row._10,
            })

        return output_format

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.get("/stats")
def taxi_stats_test(pickup_borough: str):
    """
    Endpoint para obtener estadísticas sobre los viajes en taxi para un distrito específico.

    Parameters:
        - pickup_borough: Nombre del distrito para el cual se desean las estadísticas. Debe ser uno de los siguientes:
            - Manhattan
            - Brooklyn
            - Queens
            - Bronx
            - Staten Island
            - EWR

    Returns:
        - JSON con información estadística predefinida para cada distrito.
    """
    try:
        # Configuramos las credenciales de AWS
        aws_access_key_id = 'tu_access_key_id'
        aws_secret_access_key = 'tu_secret_access_key'
        region_name = 'tu_region'

        # Configuramos la conexión a Athena
        conn = connect(aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name=region_name,
                    schema_name='tu_schema',
                    s3_staging_dir='tu_bucket')

        # Ejecutamos una consulta
        query = '''
            WITH tu_table AS (
        SELECT
            "pickup_borough",
            COUNT(*) AS "Viajes_Totales",
            ROUND(AVG(date_diff('second', "pickup_datetime", "dropoff_datetime")) / 3600, 2) AS "Duracion_Promedio_Hs",
            ROUND(COUNT(*) / COUNT(DISTINCT date_trunc('day', "pickup_datetime")), 2) AS "Media_de_Viajes_por_Dia",
            ROUND(COUNT(*) / COUNT(DISTINCT date_trunc('month', "pickup_datetime")), 2) AS "Media_de_Viajes_por_Mes",
            ROUND(AVG("trip_distance"), 2) AS "Distancia_recorrida_promedio_millas",
            ROUND(AVG("total_amount"), 2) AS "Total_ganado_en_promedio_USD"
        FROM
            "tu_database"."tu_table"
        GROUP BY
            "pickup_borough"
        )
        SELECT
        *
        FROM
        tu_table
        ORDER BY
        "pickup_borough"
        '''

        cursor = conn.cursor()
        cursor.execute(query, parameters={'pickup_borough': 'Manhattan'})  

        result = pd.DataFrame(cursor.fetchall(), columns=["pickup_borough", "Viajes_Totales", "Duracion_Promedio_Hs", "Media_de_Viajes_por_Dia", "Media_de_Viajes_por_Mes", "Distancia_recorrida_promedio_millas", "Total_ganado_en_promedio_USD"])

        borough_result = result[result["pickup_borough"] == pickup_borough]

        formatted_result = {
            "Viajes Totales": int(borough_result["Viajes_Totales"].values[0]),
            "Duración Promedio (Hs)": float(borough_result["Duracion_Promedio_Hs"].values[0]),
            "Media de Viajes por Día": float(borough_result["Media_de_Viajes_por_Dia"].values[0]),
            "Media de Viajes por Mes": float(borough_result["Media_de_Viajes_por_Mes"].values[0]),
            "Distancia recorrida promedio (millas)": float(borough_result["Distancia_recorrida_promedio_millas"].values[0]),
            "Total ganado en promedio (USD)": float(borough_result["Total_ganado_en_promedio_USD"].values[0])
        }

        # Borramos los archivos .csv y .metadata del bucket
        s3_client = boto3.client('s3',
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=region_name)

        # Definimos el nombre del bucket
        bucket_name = 'tu_bucket'

        # Obtenemos la lista de objetos en el bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Eliminamos los archivos .csv y .metadata encontrados
        for obj in response['Contents']:
            if obj['Key'].endswith('.csv') or obj['Key'].endswith('.metadata'):
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])


        return formatted_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))