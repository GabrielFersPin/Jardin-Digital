---
created: 2026-09-10
modified: 2026-09-16
area: Big Data
tipo_nota: tecnica
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-09-23
ultima-revision: 2026-09-16
veces-revisado: 1
tiempo-repaso: 5min
tipo-captura: concepto
origen: Clase
tiempo-estimado: 20min
resultado-repaso: ""
intervalo-dias: 7
prioridad: "media"
---

# Spark

> [!info] Contexto captura
> **Fecha**: 2026-09-10
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Apache Spark es un motor para procesar grandes volúmenes de datos de forma distribuida. PySpark es su API para trabajar con Spark desde Python.

### 🎯 Detalles / Contenido

Spark divide los datos y el trabajo entre varias particiones que pueden procesarse en paralelo. Una aplicación Spark tiene un proceso **driver**, que coordina el trabajo, y procesos **executor**, que ejecutan las tareas sobre los datos.

En PySpark, la abstracción principal para trabajar con datos estructurados es el **DataFrame**. Normalmente se crea mediante una [[SparkSession]] y se transforma usando operaciones como `select`, `filter`, `withColumn` y `groupBy`.

Spark distingue entre:

- **Transformaciones**: describen un nuevo conjunto de datos, pero no ejecutan el trabajo inmediatamente.
- **Acciones**: solicitan un resultado y desencadenan la ejecución, por ejemplo `show()`, `count()` o `write`.
- **Lazy evaluation**: Spark espera hasta una acción para construir y optimizar el plan de ejecución.
- **Narrow transformation**: cada partición de salida depende de pocas particiones de entrada, como `filter`.
- **Wide transformation**: puede necesitar redistribuir datos entre particiones, como `groupBy` o `join`; esta redistribución se denomina `shuffle`.

`repartition()` redistribuye los datos y puede provocar un `shuffle`.
`coalesce()` suele utilizarse para reducir particiones evitando una redistribución completa.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

spark = SparkSession.builder.appName("Ventas").getOrCreate()

ventas = spark.read.option("header", True).option("inferSchema", True).csv("ventas.csv")
resultado = (
    ventas.filter(col("cantidad") > 10)
    .groupBy("producto")
    .agg(avg("venta").alias("venta_media"))
)

resultado.show()
```

En este ejemplo, `filter`, `groupBy` y `agg` son transformaciones. `show()` es la acción que inicia la ejecución.

## 🔑 Keywords / Conceptos clave

`Apache Spark`, `PySpark`, `DataFrame`, `driver`, `executor`, `partición`, `transformación`, `acción`, `lazy evaluation`, `shuffle`

> [!note] Para RAG
> Spark es el motor distribuido; PySpark es la API de Python. El flujo habitual es crear una SparkSession, leer datos, aplicar transformaciones y ejecutar una acción.

## 🎴 Flashcards

¿Qué es PySpark?::La API de Python para trabajar con Apache Spark y procesar datos de forma distribuida. #card 

¿Cuál es la diferencia entre una transformación y una acción?::Una transformación describe una operación que se ejecutará después; una acción solicita un resultado y desencadena la ejecución. #card 

¿Qué es un shuffle?::La redistribución de datos entre particiones, normalmente provocada por operaciones como groupBy o join. #card 

---

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia hay entre el driver y los executors?
- [ ] ¿Cómo se visualiza el plan de ejecución con `explain()`?

## 🧩 Conexiones potenciales

- [[SparkSession]]
- [[Data Lake]]
- [[Data Lakehouse]]
- [[Data Processing]]

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas
- [ ] Actualizar nivel de comprensión

## 💭 Notas adicionales / Ideas rápidas

Esta nota resume Spark. Los conceptos concretos de PySpark se desarrollarán en notas atómicas dentro de la carpeta `PySpark`.

Tags: #big-data #spark #pyspark #captura-rapida


---

## 🚧 Plan de Mejora / Tareas Pendientes

Define las tareas que te ayudarán a subir tu `nivel-comprension` en la próxima revisión. Usa los tags: `#mejora-concepto`, `#mejora-practica`, `#mejora-analogia`.

- [ ] Tarea para aclarar una duda de concepto. Usa #mejora-concepto
- [ ] Tarea para implementar un ejercicio práctico. Usa #mejora-practica
- [ ] Tarea para crear una analogía o diagrama. Usa #mejora-analogia


## 🧪 Aplicación

- [ ] Explicarlo sin consultar la nota
- [ ] Resolver un caso nuevo o escribir un ejemplo
- [ ] Compararlo con una alternativa
- [ ] Usarlo en un proyecto

## 🔗 Conexiones explicadas

- [[ ]] — Se relaciona porque...
