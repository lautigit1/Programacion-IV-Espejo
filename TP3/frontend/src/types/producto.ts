export interface Producto {
  id: number
  nombre: string
  descripcion: string
  precio_base: number
  imagen_url: string[]
  disponible: boolean
}

export interface ProductoCategoria {
  producto_id: number
  categoria_id: number
}
