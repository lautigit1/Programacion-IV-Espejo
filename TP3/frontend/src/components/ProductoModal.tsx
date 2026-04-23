import { useState, useEffect } from 'react'
import type { Producto } from '../types/producto'

type FormData = Omit<Producto, 'id'>

interface Props {
  isOpen: boolean
  onClose: () => void
  onSubmit: (data: FormData) => void
  initial: Producto | null
}

const EMPTY: FormData = {
  nombre: '',
  descripcion: '',
  precio_base: 0,
  imagen_url: [],
  disponible: true,
}

export default function ProductoModal({ isOpen, onClose, onSubmit, initial }: Props) {
  const [form, setForm] = useState<FormData>(EMPTY)
  // imagen_url se edita como string separada por comas
  const [imagenesRaw, setImagenesRaw] = useState('')

  useEffect(() => {
    if (initial) {
      setForm({
        nombre: initial.nombre,
        descripcion: initial.descripcion,
        precio_base: initial.precio_base,
        imagen_url: initial.imagen_url,
        disponible: initial.disponible,
      })
      setImagenesRaw(initial.imagen_url.join(', '))
    } else {
      setForm(EMPTY)
      setImagenesRaw('')
    }
  }, [initial, isOpen])

  if (!isOpen) return null

  function handleChange(
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) {
    const { name, value, type } = e.target
    if (type === 'checkbox') {
      setForm((prev) => ({
        ...prev,
        [name]: (e.target as HTMLInputElement).checked,
      }))
    } else if (name === 'precio_base') {
      setForm((prev) => ({ ...prev, precio_base: parseFloat(value) || 0 }))
    } else {
      setForm((prev) => ({ ...prev, [name]: value }))
    }
  }

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (!form.nombre.trim() || !form.descripcion.trim()) return
    const urls = imagenesRaw
      .split(',')
      .map((u) => u.trim())
      .filter((u) => u.length > 0)
    onSubmit({ ...form, imagen_url: urls })
  }

  return (
    <div
      className="bg-black bg-opacity-40 fixed inset-0 flex items-center justify-center z-50"
      onClick={onClose}
    >
      <div
        className="bg-white rounded-2xl p-6 shadow-lg w-full max-w-md mx-4 max-h-[90vh] overflow-y-auto"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="text-xl font-semibold text-gray-800 mb-5">
          {initial ? 'Editar Producto' : 'Nuevo Producto'}
        </h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          {/* Nombre */}
          <div className="flex flex-col gap-1">
            <label htmlFor="nombre" className="text-sm font-medium text-gray-700">
              Nombre
            </label>
            <input
              id="nombre"
              name="nombre"
              type="text"
              value={form.nombre}
              onChange={handleChange}
              placeholder="Ej: Notebook Lenovo"
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
              autoFocus
            />
          </div>

          {/* Descripción */}
          <div className="flex flex-col gap-1">
            <label htmlFor="descripcion" className="text-sm font-medium text-gray-700">
              Descripción
            </label>
            <textarea
              id="descripcion"
              name="descripcion"
              value={form.descripcion}
              onChange={handleChange}
              placeholder="Describe el producto..."
              rows={3}
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition resize-none"
            />
          </div>

          {/* Precio */}
          <div className="flex flex-col gap-1">
            <label htmlFor="precio_base" className="text-sm font-medium text-gray-700">
              Precio base ($)
            </label>
            <input
              id="precio_base"
              name="precio_base"
              type="number"
              min="0"
              step="0.01"
              value={form.precio_base}
              onChange={handleChange}
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
            />
          </div>

          {/* Imágenes */}
          <div className="flex flex-col gap-1">
            <label htmlFor="imagenes" className="text-sm font-medium text-gray-700">
              URLs de imágenes{' '}
              <span className="text-gray-400 font-normal">(separadas por coma)</span>
            </label>
            <input
              id="imagenes"
              type="text"
              value={imagenesRaw}
              onChange={(e) => setImagenesRaw(e.target.value)}
              placeholder="https://..., https://..."
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
            />
          </div>

          {/* Disponible */}
          <label className="flex items-center gap-3 cursor-pointer select-none">
            <input
              type="checkbox"
              name="disponible"
              checked={form.disponible}
              onChange={handleChange}
              className="w-4 h-4 accent-blue-500"
            />
            <span className="text-sm font-medium text-gray-700">Disponible</span>
          </label>

          {/* Botones */}
          <div className="flex gap-3 pt-2">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
            >
              Cancelar
            </button>
            <button
              type="submit"
              className="flex-1 bg-blue-500 hover:bg-blue-600 text-white rounded-xl px-4 py-2 font-medium text-sm transition-colors duration-150 cursor-pointer"
            >
              {initial ? 'Guardar cambios' : 'Crear'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
