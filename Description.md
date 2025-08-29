## Descripción del Proyecto de Microservicio Geo-procesador

Este documento describe un proyecto para construir un ecosistema de microservicios de "geo-procesador" que trabaje con coordenadas de mapas. El sistema consiste en tres servicios principales:

---

### 1. Servicio Python (FastAPI)

**Núcleo del proyecto:** Procesa las coordenadas geográficas.

- **Entrada de datos:**
  - Espera un cuerpo JSON con un campo llamado `points` que contiene una lista de objetos, cada uno con las claves `lat` (latitud) y `lng` (longitud).

- **Validación de errores:**
  - Si el campo `points` no está presente, no es una matriz, está vacío, o alguna entrada carece de valores numéricos para latitud o longitud, debe devolver un error **400 Bad Request**.

- **Cálculos requeridos:**
  - **Puntos cardinales:** Buscar el norte (latitud máxima), sur (latitud mínima), este (longitud máxima) y oeste (longitud mínima).
  - **Centroide:** Calcular el centroide promediando las coordenadas de latitud y longitud de todos los puntos.

- **Respuesta de salida:**
  - Retornar una respuesta JSON bien formateada que incluya el centroide y los límites (bounds) calculados (norte, sur, este, oeste).

- **Tecnología:**
  - Se recomienda usar **FastAPI** y **Pydantic** para la validación y serialización de datos.
  - Utilizar funciones integradas de Python como `min()`, `max()` y `sum()` para los cálculos.
  - El servicio debe ser **stateless** (sin estado).

- **Documentación:**
  - Documentar las firmas de las funciones y las respuestas de error tanto en el código como en el archivo README.

---

### 2. NestJS API

**Capa intermedia:**
- Reenvía las solicitudes al servicio Python.
- Valida la entrada de datos.
- Maneja el almacenamiento en caché de los resultados.

---

### 3. Next.js Frontend

**Interfaz de usuario:**
- Permite al usuario ingresar coordenadas.
- Visualiza el cuadro delimitador (bounding box) y el centroide calculados en un mapa simple tras el procesamiento por el servicio Python.

---

## Entregables

- Un repositorio (mono o multi-repo) con la justificación de la elección.
- Un archivo **README** con todas las decisiones, justificación y las instrucciones para ejecutar el proyecto.
- Repositorios individuales para los servicios de **Python**, **NestJS** y **Next.js**.
