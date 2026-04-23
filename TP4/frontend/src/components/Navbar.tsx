import { NavLink } from "react-router-dom";

export default function Navbar() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `px-4 py-2 rounded-xl font-medium transition-colors duration-200 ${
      isActive
        ? "bg-blue-500 text-white"
        : "text-gray-600 hover:bg-gray-100 hover:text-gray-900"
    }`;

  return (
    <nav className="bg-white shadow-sm sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center gap-4">
        <span className="text-blue-500 font-bold text-lg tracking-tight">
          TP4 App
        </span>
        <div className="flex gap-2">
          <NavLink to="/categorias" className={linkClass}>
            Categorías
          </NavLink>
          <NavLink to="/productos" className={linkClass}>
            Productos
          </NavLink>
        </div>
      </div>
    </nav>
  );
}
