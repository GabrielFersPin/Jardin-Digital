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

# SparkSession

> [!info] Contexto captura
> **Fecha**: 2026-09-10
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> `SparkSession` es el punto de entrada principal para crear y utilizar una aplicación PySpark.

### 🎯 Detalles / Contenido

Una `SparkSession` permite acceder a las funcionalidades de Spark desde Python. A través de ella podemos:

- Crear y leer DataFrames.
- Configurar opciones de la aplicación.
- Ejecutar consultas SQL.
- Acceder al contexto de Spark cuando sea necesario.

La forma habitual de crearla es mediante el patrón `builder`:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Mi primera aplicacion PySpark")
    .getOrCreate()
)
```

`appName()` asigna un nombre visible para la aplicación. `getOrCreate()` reutiliza una sesión existente si ya hay una disponible o crea una nueva si no existe.

Después de crear la sesión, podemos usarla para leer datos:

```python
datos = spark.read.option("header", True).csv("datos.csv")
datos.show()
```

Cuando terminamos, podemos liberar los recursos asociados:

```python
spark.stop()
```

En notebooks normalmente se mantiene la sesión abierta mientras se trabaja. En scripts y aplicaciones, `stop()` suele formar parte del cierre de la aplicación.

## 🔑 Keywords / Conceptos clave

`SparkSession`, `builder`, `appName`, `getOrCreate`, `spark.read`, `spark.stop`

> [!note] Para RAG
> SparkSession es el punto de entrada de PySpark. Se utiliza para crear o reutilizar una sesión, leer datos y acceder a las operaciones principales de Spark.

## 🎴 Flashcards

¿Qué es SparkSession?::El punto de entrada principal para trabajar con Apache Spark desde PySpark.

¿Qué hace getOrCreate()?::Reutiliza una SparkSession existente o crea una nueva si no existe.

¿Para qué sirve appName()?::Para asignar un nombre a la aplicación Spark.

## ❓ Preguntas / Dudas pendientes

- [ ] ¿Qué diferencia hay entre SparkSession y SparkContext?
- [ ] ¿Qué configuraciones se pueden establecer mediante `builder.config()`?

## 🧩 Conexiones potenciales

- [[Spark]]
- [[SparkContext]]
- [[PySpark - DataFrame]]
- [[Lectura y escritura de datos]]

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer un ejercicio creando una sesión y leyendo un CSV
- [ ] Conectar con otras notas
- [ ] Actualizar nivel de comprensión

## 💭 Notas adicionales / Ideas rápidas

En un proyecto real, la configuración de la sesión puede incluir memoria, número de executors, modo de ejecución y otras opciones del entorno.

Tags: #big-data #spark #pyspark #spark-session #captura-rapida


## 🧪 Aplicación

- [ ] Explicarlo sin consultar la nota
- [ ] Resolver un caso nuevo o escribir un ejemplo
- [ ] Compararlo con una alternativa
- [ ] Usarlo en un proyecto

## 🔗 Conexiones explicadas

- [[ ]] — Se relaciona porque...
