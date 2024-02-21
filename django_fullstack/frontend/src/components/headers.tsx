import { Link, useLocation } from "react-router-dom";

const navigation = [
  { name: "Главное", slug: "/" },
  { name: "Аудио", slug: "/audio" },
  { name: "Комиксы", slug: "/comics" },
  { name: "Детям", slug: "/kids" },
  { name: "Мои книги", slug: "/my-books" },
  { name: "Поиск", slug: "/search" },
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
        {navigation.map((item, index) => (
          <Link
            key={index}
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
