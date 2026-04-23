export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white shadow-md px-6 py-4 flex items-center justify-between">
      <div className="flex items-center gap-3">
        <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
          <span className="text-white font-bold text-sm">TP3</span>
        </div>
        <span className="text-lg font-semibold tracking-tight">
          Gestión de Categorías
        </span>
      </div>
      <span className="text-gray-400 text-sm hidden sm:block">
        Programación IV
      </span>
    </nav>
  )
}
