---
created: 2026-09-02
modified: 2026-09-21
area: Redes
tipo_nota: captura_rapida
status: 🌿 Creciendo
nivel-comprension: 💡
proxima-revision: 2026-10-21
ultima-revision: 2026-09-21
veces-revisado: 2
tiempo-repaso: 5min
tiempo-estimado: 10min
resultado-repaso: dificil
intervalo-dias: 30
prioridad: media
innerlevel_card_id: obsidian-data-studies-redes-url-md-2026-09-21
innerlevel_last_sync: 2026-09-21
---

# URL (Uniform Resource Locator)

> [!info] Contexto captura
> **Fecha**: 2026-09-02 14:56
> **Origen**: `= this.origen`
> **Tipo**: `= this.tipo-captura`

---

## 📝 Captura principal

> [!tip] Lo más importante
> Una URL (_Uniform Resource Locator_) es la dirección que identifica dónde se encuentra un recurso en Internet, como una página web, una imagen o un archivo.


### 🎯 Detalles / Contenido

```text
http://350.5th-ave.com:80/unit/243?floor=77
```
>Protocol: The means of transportation 
http: //
>Domai: The street address of the office building 
350.5th-ave.com 
>Port: The gate or door to use when entering the building 
:80
>Path: The specific office unit inside the building
/unit/243 
>Query: Any additional instructions
?floor=77

### Addind query parameters with requests

```python
# Append the query parameter to the URL string
response = requests.get('http://350.5th-ave.com:80/unit/243?floor=77elevator=True')
print(response.url)
```
### Use the params argument to add query parameters
```python
# Create dictionary
query_params = {'floor': 77, 'elevator': True}

# Pass the dictionary using the params argument
response = requests.get{
http://350.5th-ave.com:80/unit/243?floor=77, params=query_params}
```

---

## 🔑 Keywords / Conceptos clave

`URL`, `API`, `keyword3`

> [!note] Para RAG
> Estos keywords ayudarán a encontrar esta nota después

---

## 🎴 Flashcards

¿Qué es una URL?::Es la dirección que identifica dónde se encuentra un recurso en Internet, como una página web, una imagen o un archivo. #redes #web #url #card

¿Qué representa el protocolo en una URL?::Indica el medio o conjunto de reglas utilizado para comunicarse con el recurso, por ejemplo `http` o `https`. #redes #url #card 

¿Qué representa el dominio en una URL?::Identifica la dirección o servidor donde se encuentra el recurso, por ejemplo `350.5th-ave.com`. #redes #url #card 

¿Qué representa el puerto en una URL?::Indica la puerta lógica que se utilizará para acceder al servicio, por ejemplo `80` en `:80`. #redes #url #card 

¿Qué representa el path o ruta en una URL?::Indica la ubicación específica del recurso dentro del dominio, por ejemplo `/unit/243`. #redes #url #card 

¿Qué es el query string de una URL?::Es la parte que comienza normalmente con `?` y contiene parámetros adicionales para la petición, como `?floor=77`. #redes #url #api #card 

¿Cómo se pueden añadir query parameters con requests?::Se pueden concatenar directamente en la URL o pasarlos mediante el argumento `params` usando un diccionario. #python #requests #api #card 

¿Por qué es preferible usar el argumento `params` de requests?::Porque separa los parámetros de la URL base y permite que requests los codifique correctamente. #python #requests #card 

¿Qué URL puede generar requests con `params={'floor': 77, 'elevator': True}`?::Una URL con los parámetros codificados en la query, por ejemplo `...?floor=77&elevator=True`. #python #requests #url #card p

> 💡 **Formato recomendado**:
> - Inline: `¿Pregunta?::Respuesta #tags`
> - Reversa: `Término:::Definición #tags`
> - Cloze: `Texto con ==palabra== oculta`
---

## ❓ Preguntas / Dudas pendientes

- [ ]
- [ ]

---

## 🧩 Conexiones potenciales

Es un tipo de comunicación de red con un protocolo específico [[HTTP]]

-
-

---

## ✅ Checklist procesamiento

- [x] Revisar y expandir contenido ✅ 2026-09-21
- [x] Crear flashcards si es necesario
- [ ] Hacer ejercicios relacionados
- [x] Conectar con otras notas ([[]]) ✅ 2026-09-21
- [ ] Actualizar nivel de comprensión
- [ ] Mover a vault definitivo / Cambiar status a 🌿

---

## 💭 Notas adicionales / Ideas rápidas


En resumen, una URL funciona como una dirección de Internet que indica qué recurso se quiere consultar y dónde encontrarlo.



---

## 📋 Metadata resumen

| Campo | Valor |
|-------|-------|
| Capturado | 2026-09-02 14:56 |
| Área/Tema | `= this.area` |
| Estado | `= this.status` |
| Prioridad | `= this.prioridad` |
| Revisión | `= this.proxima-revision` |
| Nivel de comprensión | `= this.nivel-comprension` |

---

#pendiente-procesar #captura-rapida


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
