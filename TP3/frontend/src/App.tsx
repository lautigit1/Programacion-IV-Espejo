import { useState, useEffect } from 'react'
import type { Categoria } from './types/categoria'
import type { Producto } from './types/producto'
import {
  getCategorias,
  createCategoria,
  updateCategoria,
  deleteCategoria,
} from './api/categorias'
import {
  getProductos,
  createProducto,
  updateProducto,
  deleteProducto,
} from './api/productos'
import Navbar from './components/Navbar'
import CategoriaList from './components/CategoriaList'
import CategoriaModal from './components/CategoriaModal'
import ProductoList from './components/ProductoList'
import ProductoModal from './components/ProductoModal'

type Tab = 'categorias' | 'productos'

export default function App() {
  // ── Estado global ──────────────────────────────────────
  const [activeTab, setActiveTab] = useState<Tab>('categorias')

  // Categorías
  const [categorias, setCategorias] = useState<Categoria[]>([])
  const [catModalOpen, setCatModalOpen] = useState(false)
  const [selectedCategoria, setSelectedCategoria] = useState<Categoria | null>(null)

  // Productos
  const [productos, setProductos] = useState<Producto[]>([])
  const [prodModalOpen, setProdModalOpen] = useState(false)
  const [selectedProducto, setSelectedProducto] = useState<Producto | null>(null)

  const [error, setError] = useState<string | null>(null)

  // ── Carga inicial ──────────────────────────────────────
  useEffect(() => {
    fetchCategorias()
    fetchProductos()
  }, [])

  async function fetchCategorias() {
    try {
      const data: Categoria[] = await getCategorias()
      setCategorias(data)
      setError(null)
    } catch {
      setError('No se pudo conectar con el servidor. ¿Está corriendo el backend?')
    }
  }

  async function fetchProductos() {
    try {
      const data: Producto[] = await getProductos()
      setProductos(data)
      setError(null)
    } catch {
      setError('No se pudo conectar con el servidor. ¿Está corriendo el backend?')
    }
  }

  // ── CRUD Categorías ────────────────────────────────────
  async function handleCreateCategoria(data: { nombre: string; descripcion: string }) {
    try {
      const nueva: Categoria = await createCategoria(data)
      setCategorias((prev) => [...prev, nueva])
      setCatModalOpen(false)
    } catch {
      setError('Error al crear la categoría')
    }
  }

  async function handleUpdateCategoria(data: { nombre: string; descripcion: string }) {
    if (!selectedCategoria) return
    try {
      const actualizada: Categoria = await updateCategoria(selectedCategoria.id, data)
      setCategorias((prev) =>
        prev.map((c) => (c.id === actualizada.id ? actualizada : c))
      )
      setCatModalOpen(false)
      setSelectedCategoria(null)
    } catch {
      setError('Error al actualizar la categoría')
    }
  }

  async function handleDeleteCategoria(id: number) {
    if (!confirm('¿Estás seguro de que querés eliminar esta categoría?')) return
    try {
      await deleteCategoria(id)
      setCategorias((prev) => prev.filter((c) => c.id !== id))
    } catch {
      setError('Error al eliminar la categoría')
    }
  }

  function handleCatModalSubmit(data: { nombre: string; descripcion: string }) {
    if (selectedCategoria) handleUpdateCategoria(data)
    else handleCreateCategoria(data)
  }

  // ── CRUD Productos ─────────────────────────────────────
  async function handleCreateProducto(data: Omit<Producto, 'id'>) {
    try {
      const nuevo: Producto = await createProducto(data)
      setProductos((prev) => [...prev, nuevo])
      setProdModalOpen(false)
    } catch {
      setError('Error al crear el producto')
    }
  }

  async function handleUpdateProducto(data: Omit<Producto, 'id'>) {
    if (!selectedProducto) return
    try {
      const actualizado: Producto = await updateProducto(selectedProducto.id, data)
      setProductos((prev) =>
        prev.map((p) => (p.id === actualizado.id ? actualizado : p))
      )
      setProdModalOpen(false)
      setSelectedProducto(null)
    } catch {
      setError('Error al actualizar el producto')
    }
  }

  async function handleDeleteProducto(id: number) {
    if (!confirm('¿Estás seguro de que querés eliminar este producto?')) return
    try {
      await deleteProducto(id)
      setProductos((prev) => prev.filter((p) => p.id !== id))
    } catch {
      setError('Error al eliminar el producto')
    }
  }

  function handleProdModalSubmit(data: Omit<Producto, 'id'>) {
    if (selectedProducto) handleUpdateProducto(data)
    else handleCreateProducto(data)
  }

  // ── Render ─────────────────────────────────────────────
  const isCategoriasTab = activeTab === 'categorias'

  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Tabs */}
        <div className="flex gap-2 mb-8 border-b border-gray-200">
          <button
            onClick={() => setActiveTab('categorias')}
            className={`px-5 py-2.5 font-medium text-sm rounded-t-xl transition-colors duration-150 cursor-pointer ${
              isCategoriasTab
                ? 'bg-white text-blue-600 border border-b-white border-gray-200 -mb-px'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            Categorías
          </button>
          <button
            onClick={() => setActiveTab('productos')}
            className={`px-5 py-2.5 font-medium text-sm rounded-t-xl transition-colors duration-150 cursor-pointer ${
              !isCategoriasTab
                ? 'bg-white text-blue-600 border border-b-white border-gray-200 -mb-px'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            Productos
          </button>
        </div>

        {/* Header de sección */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
          <div>
            <h1 className="text-2xl font-bold text-gray-800">
              {isCategoriasTab ? 'Categorías' : 'Productos'}
            </h1>
            <p className="text-gray-500 text-sm mt-0.5">
              {isCategoriasTab
                ? `${categorias.length} ${categorias.length === 1 ? 'categoría registrada' : 'categorías registradas'}`
                : `${productos.length} ${productos.length === 1 ? 'producto registrado' : 'productos registrados'}`}
            </p>
          </div>
          <button
            onClick={() => {
              if (isCategoriasTab) {
                setSelectedCategoria(null)
                setCatModalOpen(true)
              } else {
                setSelectedProducto(null)
                setProdModalOpen(true)
              }
            }}
            className="bg-blue-500 hover:bg-blue-600 text-white rounded-xl px-5 py-2.5 font-medium text-sm transition-colors duration-150 cursor-pointer shadow-sm"
          >
            {isCategoriasTab ? '+ Nueva Categoría' : '+ Nuevo Producto'}
          </button>
        </div>

        {/* Error */}
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 rounded-xl px-4 py-3 mb-6 text-sm flex items-center gap-2">
            <svg className="w-4 h-4 shrink-0" fill="currentColor" viewBox="0 0 20 20">
              <path
                fillRule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                clipRule="evenodd"
              />
            </svg>
            {error}
          </div>
        )}

        {/* Contenido del tab activo */}
        {isCategoriasTab ? (
          <CategoriaList
            categorias={categorias}
            onEdit={(cat) => {
              setSelectedCategoria(cat)
              setCatModalOpen(true)
            }}
            onDelete={handleDeleteCategoria}
          />
        ) : (
          <ProductoList
            productos={productos}
            onEdit={(prod) => {
              setSelectedProducto(prod)
              setProdModalOpen(true)
            }}
            onDelete={handleDeleteProducto}
          />
        )}
      </main>

      {/* Modal Categoría */}
      <CategoriaModal
        isOpen={catModalOpen}
        onClose={() => {
          setCatModalOpen(false)
          setSelectedCategoria(null)
        }}
        onSubmit={handleCatModalSubmit}
        initial={selectedCategoria}
      />

      {/* Modal Producto */}
      <ProductoModal
        isOpen={prodModalOpen}
        onClose={() => {
          setProdModalOpen(false)
          setSelectedProducto(null)
        }}
        onSubmit={handleProdModalSubmit}
        initial={selectedProducto}
      />
    </div>
  )
}
