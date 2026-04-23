import { useState, useEffect } from 'react'
import type { Categoria } from '../types/categoria'

interface Props {
  isOpen: boolean
  onClose: () => void
  onSubmit: (data: { nombre: string; descripcion: string }) => void
  initial: Categoria | null
}

export default function CategoriaModal({ isOpen, onClose, onSubmit, initial }: Props) {
  const [nombre, setNombre] = useState('')
  const [descripcion, setDescripcion] = useState('')

  // Sincronizar campos al abrir para edición
  useEffect(() => {
    if (initial) {
      setNombre(initial.nombre)
      setDescripcion(initial.descripcion)
    } else {
      setNombre('')
      setDescripcion('')
    }
  }, [initial, isOpen])

  if (!isOpen) return null

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    if (!nombre.trim() || !descripcion.trim()) return
    onSubmit({ nombre: nombre.trim(), descripcion: descripcion.trim() })
  }

  return (
    <div
      className="bg-black bg-opacity-40 fixed inset-0 flex items-center justify-center z-50"
      onClick={onClose}
    >
      <div
        className="bg-white rounded-2xl p-6 shadow-lg w-full max-w-md mx-4"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="text-xl font-semibold text-gray-800 mb-5">
          {initial ? 'Editar Categoría' : 'Nueva Categoría'}
        </h2>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <div className="flex flex-col gap-1">
            <label htmlFor="nombre" className="text-sm font-medium text-gray-700">
              Nombre
            </label>
            <input
              id="nombre"
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              placeholder="Ej: Electrónica"
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition"
              autoFocus
            />
          </div>

          <div className="flex flex-col gap-1">
            <label htmlFor="descripcion" className="text-sm font-medium text-gray-700">
              Descripción
            </label>
            <textarea
              id="descripcion"
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              placeholder="Describe la categoría..."
              rows={3}
              className="border border-gray-300 rounded-lg p-2 w-full text-sm focus:outline-none focus:ring-2 focus:ring-blue-400 transition resize-none"
            />
          </div>

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
