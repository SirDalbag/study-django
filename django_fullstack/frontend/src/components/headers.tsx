import { Link, useLocation } from "react-router-dom";

const navigation = [
  { id: 1, name: "Главное", slug: "/" },
  { id: 2, name: "Аудио", slug: "/audio" },
  { id: 3, name: "Комиксы", slug: "/comics" },
  { id: 4, name: "Детям", slug: "/kids" },
  { id: 5, name: "Мои книги", slug: "/my-books" },
  { id: 6, name: "Поиск", slug: "/search" },
];

export function Header() {
  const location = useLocation();

  return (
    <header className="bg-white">
      <ul className="flex items-center list-none">
        <Link to="/">
          <li className="px-4 mt-2.5">
            <img className="h-8 w-auto" src="/icon.svg" />
          </li>
        </Link>
        {navigation.map((item) => (
          <Link
            key={item.id}
            to={item.slug}
            className="transform transition-transform duration-100 active:scale-95"
          >
            <li className="p-4 mt-2">
              <span
                className={`py-4 font-semibold border-b-[3px] hover:border-blue-600 hover:text-blue-600 
              ${
                location.pathname === item.slug
                  ? "text-blue-600 border-blue-600"
                  : "border-transparent"
              }`}
              >
                {item.name}
              </span>
            </li>
          </Link>
        ))}
      </ul>
    </header>
  );
}
