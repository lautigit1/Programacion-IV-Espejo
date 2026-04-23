const BASE_URL = 'http://localhost:8000'

export async function getCategorias() {
  const res = await fetch(`${BASE_URL}/categorias/`)
  if (!res.ok) throw new Error('Error al obtener categorías')
  return res.json()
}

export async function createCategoria(data: { nombre: string; descripcion: string }) {
  const res = await fetch(`${BASE_URL}/categorias/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Error al crear categoría')
  return res.json()
}

export async function updateCategoria(
  id: number,
  data: { nombre: string; descripcion: string }
) {
  const res = await fetch(`${BASE_URL}/categorias/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  })
  if (!res.ok) throw new Error('Error al actualizar categoría')
  return res.json()
}

export async function deleteCategoria(id: number) {
  const res = await fetch(`${BASE_URL}/categorias/${id}`, {
    method: 'DELETE',
  })
  if (!res.ok) throw new Error('Error al eliminar categoría')
}
