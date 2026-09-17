---
created: 2026-09-07
modified: 2026-09-10
area: Machine Learning
tipo_nota: captura_rapida
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-09-24
ultima-revision: 2026-09-10
veces-revisado: 1
tiempo-repaso: 5min
tiempo-estimado: 10min
resultado-repaso: ""
intervalo-dias: 7
prioridad: "media"
---

# Amazon SageMaker Model Registry

> [!info] Contexto captura
> **Fecha**: 2026-09-07 11:34
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Amazon SageMaker Model Registry es un repositorio para registrar, versionar y gestionar modelos de machine learning.

### 🎯 Detalles / Contenido

<!-- Captura rápida del contenido sin preocuparte por formato perfecto -->
Permite:

- Guardar distintas versiones de un modelo.
- Asociar metadatos, métricas, parámetros y artefactos.
- Gestionar estados como `Pending`, `Approved` o `Rejected`.
- Controlar qué modelos están autorizados para desplegarse.
- Mantener un historial de cambios.
- Integrarse con pipelines de entrenamiento, validación y despliegue.
- Facilitar procesos de CI/CD para machine learning.

Un flujo típico sería:

> Entrenar modelo → evaluar métricas → registrar versión → aprobar modelo → desplegar en SageMaker Endpoint

Importante:

- [[Amazon SageMaker Training Jobs]]: entrenan el modelo.
- [[Amazon SageMaker Model Registry]]: guarda y controla sus versiones.
- [[Amazon SageMaker Endpoints]]: sirven el modelo para realizar predicciones.
- [[Amazon SageMaker Pipelines]]: automatizan el flujo completo.

---

## 🔑 Keywords / Conceptos clave

`AWS`, `SageMaker`, `Machine Learning`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es Amazon SageMaker Model Registry?::Un repositorio para registrar, versionar y gestionar modelos de machine learning. #aws #sagemaker

¿Qué información puede asociarse a una versión de modelo?::Metadatos, métricas, parámetros y artefactos del modelo. #aws #model-registry

¿Qué estados puede tener un modelo en SageMaker Model Registry?::Por ejemplo, `Pending`, `Approved` o `Rejected`. #aws #model-registry

¿Qué controla SageMaker Model Registry antes del despliegue?::Qué versiones del modelo están autorizadas para desplegarse. #aws #model-registry

¿Qué ventaja ofrece el versionado de modelos?::Permite mantener un historial de cambios y gestionar distintas versiones del mismo modelo. #machine-learning #model-versioning

¿Cuál es el flujo típico desde el entrenamiento hasta el despliegue?::Entrenar el modelo → evaluar métricas → registrar la versión → aprobar el modelo → desplegarlo en un SageMaker Endpoint. #mlops #sagemaker

¿Qué servicio entrena el modelo antes de registrarlo?:::Amazon SageMaker Training Jobs #aws #sagemaker

¿Qué servicio automatiza el flujo de entrenamiento, validación y despliegue?:::Amazon SageMaker Pipelines #aws #mlops

¿Qué servicio sirve el modelo para realizar predicciones?:::Amazon SageMaker Endpoints #aws #sagemaker

Cloze: El Model Registry permite registrar, ==versionar== y gestionar modelos de machine learning. #aws #model-registry

---

## ❓ Preguntas / Dudas pendientes

- [ ]
- [ ]

---

## 🧩 Conexiones potenciales

<!-- ¿Con qué otros temas se relaciona? Escribe rápido, ya harás los links después -->

-
-

---

## ✅ Checklist procesamiento

- [ ] Revisar y expandir contenido
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [ ] Conectar con otras notas ([[]])
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas

<!-- Zona libre para cualquier cosa que quieras capturar rápido -->

SageMaker Model Registry funciona como un control de versiones y catálogo de modelos de machine learning listos para ser evaluados o desplegados.

---

## 📋 Metadata resumen

| Campo                | Valor                      |
| -------------------- | -------------------------- |
| Capturado            | 2026-09-07 11:34           |
| Área/Tema            | `= this.area`              |
| Estado               | `= this.status`            |
| Prioridad            | `= this.prioridad`         |
| Revisión             | `= this.proxima-revision`  |
| Nivel de comprensión | `= this.nivel-comprension` |

---

Tags: #pendiente-procesar #captura-rapida


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
