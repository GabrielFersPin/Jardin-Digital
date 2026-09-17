---
created: 2026-09-10
modified: 2026-09-17
area: Big Data
tipo_nota: tecnica
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-10-17
ultima-revision: 2026-09-17
veces-revisado: 2
tiempo-repaso: 5min
tipo-captura: referencia
origen: Aprendizaje PySpark
tiempo-estimado: 10min
resultado-repaso: ""
intervalo-dias: 7
prioridad: "media"
---

# PySpark - Métodos más utilizados

> [!info] Contexto captura
> **Fecha**: 2026-09-10
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Los DataFrames de PySpark se manipulan principalmente mediante transformaciones como `filter`, `select`, `withColumn`, `groupBy` y `orderBy`. Estas operaciones son perezosas y normalmente necesitan una acción como `show()` o `count()` para ejecutarse.

### 🎯 Datos de ejemplo

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, desc, sum

spark = SparkSession.builder.appName("Metodos PySpark").getOrCreate()

ventas = spark.createDataFrame([
    ("Laptop", "Norte", 2, 800.0),
    ("Tablet", "Sur", 5, 300.0),
    ("Laptop", "Sur", 1, 800.0),
], ["producto", "region", "cantidad", "precio"])
```

## Seleccionar y observar datos

### `show()`

Muestra filas del DataFrame. Es una acción útil para inspeccionar resultados:

```python
ventas.show()
ventas.show(), truncate=False)
```

### `select()`

Selecciona columnas o expresiones:

```python
ventas.select("producto", "precio").show()
ventas.select((col("cantidad") * col("precio")).alias("importe")).show()
```

### `printSchema()` y `describe()`

```python
ventas.printSchema()
ventas.describe("cantidad", "precio").show()
```

`printSchema()` muestra los tipos y la estructura. `describe()` calcula estadísticas básicas.

## Filtrar y modificar columnas

### `filter()` y `where()`

Ambos métodos filtran filas y son equivalentes:

```python
ventas.filter(col("cantidad") > 2).show()
ventas.where((col("region") == "Sur") & (col("precio") > 500)).show()
```

En expresiones compuestas se utilizan `&` para AND, `|` para OR y `~` para NOT. Cada condición debe ir entre paréntesis.

### `withColumn()`

Crea una columna nueva o reemplaza una existente:

```python
ventas_con_importe = ventas.withColumn(
    "importe",
    col("cantidad") * col("precio"),
)
```

### `drop()` y `withColumnRenamed()`

```python
ventas.drop("precio")
ventas.withColumnRenamed("cantidad", "unidades")
```

## Ordenar y eliminar duplicados

### `orderBy()` y `sort()`

`sort()` y `orderBy()` son alias para ordenar un DataFrame:

```python
ventas.orderBy("precio").show()
ventas.orderBy(desc("precio"), "producto").show()
ventas.sort(col("cantidad").asc()).show()
```

`asc()` ordena ascendentemente y `desc()` descendentemente. En grandes volúmenes, ordenar puede provocar un `shuffle` porque los datos deben redistribuirse entre particiones.

### `distinct()` y `dropDuplicates()`

```python
ventas.select("producto").distinct().show()
ventas.dropDuplicates(["producto", "region"]).show()
```

`distinct()` elimina filas completamente repetidas. `dropDuplicates()` permite indicar las columnas que determinan el duplicado.

## Agrupar y agregar

### `groupBy()` y `agg()`

```python
ventas.groupBy("region").agg(
    sum("cantidad").alias("unidades_totales"),
    avg("precio").alias("precio_medio"),
).show()
```

`groupBy()` crea grupos y `agg()` calcula resultados sobre cada grupo. Esta operación normalmente requiere un `shuffle`.

## Combinar y limitar datos

### `join()`

Combina DataFrames usando una columna relacionada:

```python
regiones = spark.createDataFrame([
    ("Norte", "America"),
    ("Sur", "America"),
], ["region", "continente"])

ventas.join(regiones, on="region", how="left").show()
```

Los tipos habituales son `inner`, `left`, `right` y `outer`.

### `union()`

Añade filas de dos DataFrames con el mismo esquema:

```python
ventas_completas = ventas.union(ventas_nuevas)
```

Para combinar por nombre de columna, incluso si el orden cambia, puede utilizarse `unionByName()`.

### `limit()`

Devuelve como máximo un número determinado de filas:

```python
ventas.limit(10).show()
```

## Acciones frecuentes

Las acciones desencadenan la ejecución del plan de Spark:

```python
ventas.show()       # Muestra filas
ventas.count()      # Cuenta filas
ventas.first()      # Devuelve la primera fila
ventas.take(3)      # Devuelve hasta tres filas al driver
ventas.collect()    # Devuelve todas las filas al driver
```

`collect()` debe utilizarse con cuidado: intenta traer todos los datos al driver y puede consumir demasiada memoria.

## `map()` y RDDs

`map()` no es el método habitual de un DataFrame. Es una transformación de RDD que aplica una función a cada elemento:

```python
numeros = spark.sparkContext.parallelize([1, 2, 3])
doblados = numeros.map(lambda numero: numero * 2)
doblados.collect()
```

Para DataFrames se suelen preferir `select()`, `withColumn()` y las funciones nativas de `pyspark.sql.functions`. Estas operaciones permiten que Spark entienda y optimice mejor el plan de ejecución.

## 🔑 Keywords / Conceptos clave

`filter`, `where`, `select`, `show`, `withColumn`, `drop`, `orderBy`, `sort`, `groupBy`, `agg`, `join`, `union`, `distinct`, `limit`, `map`, `collect`

> [!note] Para RAG
> Las operaciones habituales de DataFrame incluyen seleccionar, filtrar, transformar columnas, ordenar, agrupar, unir y guardar datos. `map()` pertenece principalmente a la API de RDD, no al flujo habitual de DataFrames.

## 🎴 Flashcards

¿Qué diferencia hay entre `filter()` y `where()`?::Ninguna relevante en este contexto; ambos métodos filtran filas de un DataFrame. #card 

¿Qué diferencia hay entre `sort()` y `orderBy()`?::Son alias para ordenar un DataFrame. #card 

¿Por qué hay que tener cuidado con `collect()`?::Porque trae todas las filas al driver y puede provocar problemas de memoria. #card 

¿Dónde se utiliza principalmente `map()`?::En RDDs, para aplicar una función a cada elemento; en DataFrames suelen preferirse las funciones nativas de PySpark. #card 

¿Qué operación puede provocar un shuffle?::Operaciones como `orderBy`, `groupBy` y algunos `join`, porque pueden redistribuir datos entre particiones. #card 

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia existe entre `join` y `union`?
- [ ] ¿Cómo se manejan los valores nulos con `na.drop()` y `na.fill()`?
- [ ] ¿Cuándo conviene usar funciones nativas en lugar de una UDF?

## 🧩 Conexiones potenciales

- [[SparkSession]]
- [[SparkContext]]
- [[Lectura y escritura de datos]]
- [[Spark]]

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer un ejercicio usando `filter`, `withColumn`, `groupBy` y `orderBy`
- [ ] Conectar con otras notas
- [ ] Actualizar nivel de comprensión

## 💭 Notas adicionales / Ideas rápidas

Esta nota es una referencia rápida. Cada método que se convierta en un tema de estudio profundo puede separarse después en una nota atómica propia.

Tags: #big-data #spark #pyspark #dataframe #rdd #captura-rapida


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
