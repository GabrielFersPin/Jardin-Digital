---
created: 2026-09-10
modified: 2026-09-10
area: "Big Data"
tipo_nota: "tecnica"
status: "🌱"
nivel-comprension: "❓"
proxima-revision: "2026-09-12"
ultima-revision: "2026-09-10"
veces-revisado: 0
tiempo-repaso: "5min"
tipo-captura: "concepto"
origen: "Aprendizaje PySpark"
resultado-repaso: ""
intervalo-dias: 7
prioridad: "media"
---

# SparkContext

> [!info] Contexto captura
> **Fecha**: 2026-09-10
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> `SparkContext` representa la conexión de bajo nivel entre una aplicación y el cluster de Spark. Sigue siendo importante, pero normalmente no se crea directamente en aplicaciones modernas de PySpark.

### 🎯 Detalles / Contenido

`SparkContext` coordina la ejecución distribuida y permite a la aplicación comunicarse con el cluster. Es la base de APIs de bajo nivel como los RDDs.

Actualmente, el punto de entrada recomendado es `SparkSession`. Al crear una sesión, Spark crea o reutiliza un `SparkContext` internamente:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Ejemplo").getOrCreate()
sc = spark.sparkContext
```

En este caso, `sc` permite acceder al contexto que ya utiliza la sesión. No es necesario crear otro `SparkContext`.

La creación directa puede encontrarse en código antiguo o en ejemplos que trabajan específicamente con RDDs:

```python
from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Ejemplo RDD")
sc = SparkContext(conf=conf)
```

Para trabajar con DataFrames, SQL y las funciones habituales de PySpark, se debe preferir `SparkSession`. Crear varios `SparkContext` activos en el mismo proceso puede provocar errores; normalmente solo debe existir uno.

## 🔑 Keywords / Conceptos clave

`SparkContext`, `SparkSession`, `RDD`, `cluster`, `driver`, `spark.sparkContext`

> [!note] Para RAG
> SparkContext es el componente de bajo nivel que conecta la aplicación con el cluster. SparkSession lo crea o reutiliza internamente y es la interfaz recomendada para trabajar con DataFrames y SQL.

## 🎴 Flashcards

¿Qué es SparkContext?::El componente de bajo nivel que conecta una aplicación PySpark con el cluster y coordina la ejecución distribuida. #card 

¿Cómo se accede normalmente a SparkContext en PySpark moderno?::A través de `spark.sparkContext`, después de crear una SparkSession. #card 

¿Se debe crear un SparkContext para cada DataFrame?::No. Normalmente se crea o reutiliza uno mediante SparkSession. #card 

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué operaciones de RDD requieren usar directamente `SparkContext`?
- [ ] ¿Qué diferencia hay entre un RDD y un DataFrame?

## 🧩 Conexiones potenciales

- [[SparkSession]]
- [[Spark]]
- [[PySpark - DataFrame]]

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer un ejercicio accediendo a `spark.sparkContext`
- [ ] Conectar con otras notas
- [ ] Actualizar nivel de comprensión

## 💭 Notas adicionales / Ideas rápidas

No es una API obsoleta, pero sí una abstracción más baja que normalmente no necesitas manipular directamente al empezar con DataFrames.

Tags: #big-data #spark #pyspark #spark-context #captura-rapida


## 🧪 Aplicación

- [ ] Explicarlo sin consultar la nota
- [ ] Resolver un caso nuevo o escribir un ejemplo
- [ ] Compararlo con una alternativa
- [ ] Usarlo en un proyecto

## 🔗 Conexiones explicadas

- [[ ]] — Se relaciona porque...
