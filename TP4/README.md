# TP4 — Instrucciones de Ejecución

## 🐍 Backend (FastAPI)

```bash
# 1. Ir al directorio del backend
cd TP4/backend

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Levantar servidor
uvicorn app.main:app --reload
```

**El servidor queda en:** `http://localhost:8000`  
**Docs interactivas:** `http://localhost:8000/docs`

---

## ⚛️ Frontend (React + Vite)

```bash
# 1. Ir al directorio del frontend
cd TP4/frontend

# 2. Instalar dependencias (ya instaladas, pero por si acaso)
npm install

# 3. Correr servidor de desarrollo
npm run dev
```

**El frontend queda en:** `http://localhost:5173`

---

## ✅ Orden de ejecución

1. **Primero** levantar el backend
2. **Después** levantar el frontend
3. Navegar a `http://localhost:5173` → redirige automáticamente a `/categorias`

---

## 🧪 Probar el backend

Usar el archivo `backend/requests.http` con la extensión **REST Client** de VS Code.

Endpoints disponibles:

| Método | URL | Descripción |
|--------|-----|-------------|
| GET | /categorias/ | Listar categorías |
| POST | /categorias/ | Crear categoría |
| PUT | /categorias/{id} | Actualizar categoría |
| DELETE | /categorias/{id} | Eliminar categoría |
| GET | /productos/ | Listar productos |
| POST | /productos/ | Crear producto |
| PUT | /productos/{id} | Actualizar producto |
| DELETE | /productos/{id} | Eliminar producto |
| POST | /productos/{id}/categorias | Vincular categoría |
| GET | /productos/{id}/categorias | Listar categorías del producto |
| DELETE | /productos/{id}/categorias/{cat_id} | Desvincular categoría |
