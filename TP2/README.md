# Gestor de Productos — API REST (FastAPI + SQLModel + PostgreSQL)

Trabajo práctico: migración de un gestor en memoria a persistencia en **PostgreSQL**, con **arquitectura en capas** y **Alembic** para migraciones.

---

## 1. Estructura del proyecto y responsabilidades

```
TP2/
├── app/
│   ├── main.py           # Punto de entrada FastAPI, routers y manejo global de errores de validación
│   ├── database.py       # Motor SQLAlchemy/SQLModel y dependencia `get_session()`
│   ├── core/             # Configuración (variables de entorno), utilidades transversales
│   ├── models/           # Entidades ORM (`SQLModel`, `table=True`) — tablas en la base
│   ├── schemas/          # Modelos Pydantic: entrada/salida y validaciones de formato
│   ├── repositories/     # Consultas y persistencia (sin reglas de negocio)
│   ├── services/         # Reglas de negocio, orquestación y códigos HTTP de dominio
│   └── routers/          # Endpoints HTTP: rutas, dependencias, códigos de respuesta
├── alembic/              # Migraciones versionadas (`versions/`, `env.py`)
├── examples/             # JSON y `.http` para pruebas manuales
├── alembic.ini
├── requirements.txt
└── .env.example
```

| Carpeta / archivo | Rol (Clean Architecture) |
|-------------------|---------------------------|
| **routers** | Capa de presentación HTTP: traduce peticiones a llamadas al servicio y devuelve respuestas. |
| **services** | Casos de uso / aplicación: valida reglas de negocio, coordina repositorios. |
| **repositories** | Infraestructura de datos: CRUD y consultas sobre la sesión SQLModel. |
| **models** | Dominio persistido: forma de las tablas (no exponer directamente al cliente). |
| **schemas** | Contratos de API: qué entra y qué sale, con Pydantic. |
| **core** | Configuración y ajustes globales (por ejemplo URL de base de datos). |
| **database** | Sesión por request y creación del `engine`. |
| **alembic** | Evolución del esquema sin perder historial ni dependencia de “crear tablas a mano” en producción. |

**Justificación:** separar **schemas** (formato y límites de datos) de **services** (reglas que pueden cambiar con el negocio) facilita pruebas y cambios sin mezclar SQL con validaciones de negocio.

---

## 2. Requisitos

- Python 3.10+
- PostgreSQL 14+ (o compatible)
- Entorno virtual recomendado

---

## 3. Configuración de PostgreSQL y variables de entorno

1. Crear base de datos, por ejemplo:

```sql
CREATE DATABASE gestor_productos;
```

2. Copiar `.env.example` a `.env` y ajustar usuario, contraseña, host y nombre de DB:

```env
DATABASE_URL=postgresql+psycopg2://USUARIO:PASSWORD@localhost:5432/gestor_productos
DEBUG=false
```

3. Instalar dependencias y aplicar migraciones (ver sección 4).

La sesión se obtiene con `Depends(get_session)` en cada request: se abre al entrar y se cierra al salir, evitando fugas de conexiones.

---

## 4. Alembic — comandos y flujo

| Comando | Uso |
|--------|-----|
| `alembic init alembic` | Crea la carpeta `alembic/` y `alembic.ini` (en este proyecto ya está hecho). |
| `alembic revision --autogenerate -m "mensaje"` | Genera un script comparando modelos SQLModel con la DB (revisar siempre el archivo generado). |
| `alembic upgrade head` | Aplica todas las migraciones pendientes hasta la última. |

**Primera vez en este repo:**

```powershell
cd "ruta\al\TP2"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
```

Ya incluye una migración inicial (`alembic/versions/20260407_01_initial_products.py`) que crea la tabla `products`.

---

## 5. Cómo ejecutar la API

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Documentación interactiva: **http://localhost:8000/docs** (Swagger UI)
- Alternativa: **http://localhost:8000/redoc**

### Qué verificar en Swagger

- **Endpoints:** `POST/GET/PUT/DELETE` bajo `/products` y `GET /`.
- **Schemas:** cuerpos de `ProductCreate`, `ProductUpdate` y respuesta `ProductRead`.
- **Respuestas:** 201 al crear, 200 al leer/actualizar/listar, 204 al borrar, 404 si el id no existe, 400 si los datos son inválidos o la actualización viene vacía.

---

## 6. Endpoints REST

| Método | Ruta | Descripción | Respuesta típica |
|--------|------|-------------|------------------|
| `POST` | `/products` | Crea un producto | **201** + JSON del producto con `id` |
| `GET` | `/products` | Lista todos | **200** + array JSON |
| `GET` | `/products/{id}` | Detalle por id | **200** o **404** |
| `PUT` | `/products/{id}` | Actualización parcial | **200** o **404** / **400** |
| `DELETE` | `/products/{id}` | Elimina | **204** sin cuerpo o **404** |

---

## 7. Validaciones

- **Esquema (Pydantic):** nombre obligatorio (no vacío tras `strip`), `precio > 0`, `stock >= 0`, límites de longitud.
- **Negocio (Service):** coherencia adicional (por ejemplo actualización sin campos, o reglas que más adelante dependan de políticas del negocio).

Los errores de validación de entrada se responden con **400** y cuerpo JSON con `mensaje` y `errores` (detalle de Pydantic).

---

## 8. Pruebas con Postman / REST Client

En la carpeta `examples/` hay:

- `crear_producto.json`, `actualizar_producto.json` — cuerpos listos para pegar.
- `rest-client.http` — compatible con la extensión REST Client de VS Code.

**Crear (POST `/products`):** usar `examples/crear_producto.json`.

**Actualizar (PUT `/products/1`):** usar `examples/actualizar_producto.json` (ajustar el id en la URL).

---

## 9. Contenido sugerido del .zip para entregar

- Proyecto completo con `app/`, `alembic/`, `requirements.txt`, `alembic.ini`, `.env.example`.
- Carpeta `examples/` con JSON y `.http`.
- **Sin** carpetas `__pycache__` ni entornos virtuales (`.venv/`).
- Opcional: este `README.md` como documentación de entrega.

**Tip:** antes de comprimir, borrar cachés:

```powershell
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force
```

---

## 10. Decisiones técnicas (resumen)

- **SQLModel:** unifica modelo de tabla y tipado con Pydantic, alineado con FastAPI.
- **Sesión por dependencia:** patrón recomendado para no compartir sesión entre requests.
- **400 vs 422:** se unifica la validación de entrada a **400** con un `exception_handler` para cumplir el enunciado; en APIs puras REST a veces se deja 422 (convención de FastAPI).
- **PUT parcial:** el esquema `ProductUpdate` solo aplica campos enviados (`exclude_unset=True`).

---

## Autor

Trabajo práctico — Programación IV — entrega tipo informe técnico estudiantil.
