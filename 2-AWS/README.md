# **Implementación de servicios de Amazon Web Services**

## [AWS Lambda](https://aws.amazon.com/es/pm/lambda/?gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi3hA_kpcaFxoJcsHGFQ6Csz1HOeFl6fqBFCYpECIED_WyPmMUSeVjwaApFrEALw_wcB&trk=91e64750-b4c8-4c8d-8ab0-9f93b6d03e96&sc_channel=ps&ef_id=Cj0KCQiAnfmsBhDfARIsAM7MKi3hA_kpcaFxoJcsHGFQ6Csz1HOeFl6fqBFCYpECIED_WyPmMUSeVjwaApFrEALw_wcB:G:s&s_kwcid=AL!4422!3!651510248553!e!!g!!aws%20lambda!19828212861!147446016415) es un servicio de computación sin servidor que nos permite ejecutar código sin aprovisionar ni administrar servidores. Podemos ejecutar código para prácticamente cualquier tipo de aplicación o servicio backend con tolerancia a errores o administración de recursos de computación. Solo tenemos que cargar el código y `Lambda` se encargará de todo lo necesario para ejecutar y escalar el código con alta disponibilidad. Podemos configurar el código para que se ejecute automáticamente desde otras fuentes (como S3, SNS, DynamoDB o Kinesis) sin necesidad de crear un punto de enlace. También podemos usar Lambda para crear nuevos servicios que se activen de forma directa o periódica.

## En esta primer estapa, creamos una función `Lambda` que se encarga de realizar web scrapping a la página [Taxi & Limousine Comission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) para extraer los datos de los viajes realizados en la ciudad de New York durante el año 2023 y finalmente almacenarlos en un bucket de [AWS S3](https://aws.amazon.com/es/s3/).

![lambda_ws](imagenes/Lambda_WS.png)

## A efectos de automatizar el proceso se utilizó [AWS EventBridge](https://aws.amazon.com/es/eventbridge/) para programar la ejecución de la función `Lambda` el día 15 de cada mes a las 00:00 hs.
![imagen](imagenes/inicio_ws.jpg)


## Una vez obtenidos los archivos parquet, recurrimos al uso de [AWS Glue](https://aws.amazon.com/es/glue/) para automatizar el proceso de normalización de los datos.
## [AWS Glue](https://aws.amazon.com/es/glue/) es un servicio de extracción, transformación y carga (ETL) totalmente administrado que facilita la preparación y la carga de los datos para su análisis. Podemos crear y ejecutar trabajos de ETL con unos pocos clics en la consola de AWS o directamente ejecutar el código en Apache Spark para aprovechar los beneficios de escala, seguridad y administración.

![glue](imagenes/etl_glue.png)

## Para automatizar el proceso de normalización de los datos, se utilizó [AWS EventBridge](https://aws.amazon.com/es/eventbridge/) para programar la ejecución de la tarea de [AWS Glue](https://aws.amazon.com/es/glue/) el día 15 de cada mes a las 01:00 hs.

![inicio_glue](imagenes/inicio_etl.png)

## Una vez que se completa la normalización de los datos, se guarda el archivo resultante en formato Parquet en un bucket de [AWS S3](https://aws.amazon.com/es/s3/). Sin embargo, el archivo se guarda con el nombre predeterminado `part-00000-8bbda55c-fad7-46b5-9f8d-b8d8e336c149-c000.snappy.parquet`. Este nombre se genera automáticamente cuando se guarda un archivo Parquet utilizando Apache Spark con el formato de compresión Snappy.
## Para solucionar este problema, utilizamos otra función `Lambda` para renombrar el archivo y almacenarlo en un bucket que alimenta a nuestro `Data Warehouse`.

![lambda_rename](imagenes/Lambda_rename.png)

## La automatización de este proceso se realiza mediante otro evento de [AWS EventBridge](https://aws.amazon.com/es/eventbridge/) que se ejecuta el día 15 de cada mes a las 02:00 hs.

![inicio_rename](imagenes/inicio_rename.jpg)


### Una vez que el archivo se encuentra en el bucket que nutre a [AWS Athena](https://aws.amazon.com/es/athena/), podemos realizar consultas SQL para obtener información de los datos almacenados en el `Data Warehouse` como así también utilizar la librería PyAthena para hacer consultas desde Python y así crear aplicaciones o sitios web que utilicen el database para arrojar resultados. 
### Conforme la base de datos de TLC se renueve, nuestro `Data Warehouse` y todos los servicios de AWS que dependan de él, se actualizarán automáticamente mediante nuestra función `Lambda` que tomará los nuevos registros de viajes y los almacenará en el bucket del `Data Warehouse`.


![tabla_athena](imagenes/tabla_athena.png)