---
created: 2026-09-10
modified: 2026-09-16
area: Big Data
tipo_nota: tecnica
status: 🌱 Semilla
nivel-comprension: 🤔
proxima-revision: 2026-09-23
ultima-revision: 2026-09-16
veces-revisado: 1
tiempo-repaso: 5min
tipo-captura: concepto
origen: Aprendizaje PySpark
tiempo-estimado: 10min
resultado-repaso: ""
intervalo-dias: 7
prioridad: "media"
---

# PySpark - Lectura y escritura de datos

> [!info] Contexto captura
> **Fecha**: 2026-09-10
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> En PySpark, `spark.read` carga datos en un DataFrame y `DataFrame.write` guarda ese DataFrame en un formato o destino determinado.

### 🎯 Detalles / Contenido

La lectura parte de una `SparkSession`:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lectura y escritura").getOrCreate()
```

## Lectura de datos

### CSV

```python
ventas = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("datos/ventas.csv")
)
```

`header=True` indica que la primera fila contiene los nombres de las columnas. `inferSchema=True` pide a Spark que intente deducir automáticamente los tipos de datos.

La inferencia puede ser útil al explorar datos, pero requiere analizar parte del archivo y puede producir resultados inesperados si una columna contiene valores inconsistentes. En procesos importantes es preferible definir el esquema explícitamente.

```python
from pyspark.sql.types import DoubleType, IntegerType, StructField, StructType

esquema = StructType([
    StructField("producto", "string", nullable=False),
    StructField("cantidad", IntegerType(), nullable=True),
    StructField("venta", DoubleType(), nullable=True),
])

ventas = (
    spark.read
    .option("header", True)
    .schema(esquema)
    .csv("datos/ventas.csv")
)
```

- IntegerType: Números enteros (ejemplo: 2, 234, -12)
- LongType: Números enteros largos (ejemplo: 1292312312343)
- FloatType o DoubleType: Números decimales (ejemplo: 1.2, )
- StringType: Datos de tipo string (ejemplo: This is an example string)

### Otros formatos

```python
usuarios = spark.read.json("datos/usuarios.json")
eventos = spark.read.parquet("datos/eventos.parquet")
```

Parquet suele ser una buena opción para datos estructurados porque conserva el esquema y utiliza un formato columnar eficiente.

## Escritura de datos

```python
(
    ventas.write
    .mode("overwrite")
    .parquet("salidas/ventas_procesadas")
)
```

Los modos de escritura más habituales son:

- `error` o `errorifexists`: falla si el destino ya existe.
- `overwrite`: reemplaza los datos existentes.
- `append`: añade nuevos datos al destino.
- `ignore`: no hace nada si el destino ya existe.

Spark suele escribir varias partes de salida, una por partición, en lugar de crear un único archivo. Esto permite escribir en paralelo y es el comportamiento esperado en un entorno distribuido.

```python
ventas.write.mode("overwrite").option("header", True).csv("salidas/ventas_csv")
```

## 🔑 Keywords / Conceptos clave

`spark.read`, `DataFrame.write`, `CSV`, `JSON`, `Parquet`, `header`, `inferSchema`, `StructType`, `mode`, `overwrite`, `append`, `particiones`

> [!note] Para RAG
> `spark.read` carga datos como DataFrame y `DataFrame.write` los guarda. `inferSchema` deduce tipos automáticamente, pero un esquema explícito ofrece mayor control y estabilidad.

## 🎴 Flashcards

¿Para qué sirve `inferSchema=True`?::Para pedirle a Spark que intente deducir automáticamente los tipos de las columnas al leer datos, especialmente CSV.

¿Qué diferencia hay entre `overwrite` y `append`?::`overwrite` reemplaza los datos existentes; `append` añade nuevos datos al destino.

¿Por qué Spark puede crear varios archivos al guardar un DataFrame?::Porque escribe en paralelo, normalmente generando una salida por cada partición.

¿Cuándo conviene usar un esquema explícito?::En procesos importantes o repetibles, porque ofrece control sobre los tipos y evita inferencias inesperadas.

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Cómo se elige un formato adecuado entre CSV, JSON y Parquet?
- [ ] ¿Cómo afectan las particiones al número de archivos generados?
- [ ] ¿Cuándo utilizar `partitionBy()` al guardar datos?

## 🧩 Conexiones potenciales

- [[SparkSession]]
- [[SparkContext]]
- [[Spark]]
- [[Data Lake]]
- [[Data Lakehouse]]

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer un ejercicio leyendo un CSV y guardándolo como Parquet
- [ ] Conectar con otras notas
- [ ] Actualizar nivel de comprensión

## 💭 Notas adicionales / Ideas rápidas

La ruta de escritura representa normalmente una carpeta que contiene varios archivos de salida y metadatos, no un único archivo final.

Tags: #big-data #spark #pyspark #dataframe #lectura-datos #escritura-datos #captura-rapida


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
