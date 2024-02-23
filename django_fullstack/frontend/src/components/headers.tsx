import { Link, useLocation } from "react-router-dom";

const navigation = [
  { id: 1, name: "Главное", slug: "/" },
  { id: 2, name: "Аудио", slug: "/audio" },
  { id: 3, name: "Комиксы", slug: "/comics" },
  { id: 4, name: "Детям", slug: "/kids" },
  { id: 5, name: "Мои книги", slug: "/my-books" },
];

function isActive(slug: string, path: string): boolean {
  return path === slug ? true : false;
}

export function Header() {
  const location = useLocation();

  return (
    <header className="bg-white">
      <ul className="flex items-end gap-4 px-4 pt-4">
        <li>
          <Link to="/">
            <img className="mr-2 mb-2.5 h-8 w-auto" src="/icon.svg" />
          </Link>
        </li>
        <ul className="flex gap-6">
          {navigation.map((item) => (
            <li>
              <Link className="group" to={item.slug} key={item.id}>
                <div
                  className={`transform transition-transform duration-100 active:scale-95 border-b-2 ${
                    isActive(item.slug, location.pathname)
                      ? "border-blue-600"
                      : "border-transparent group-hover:border-blue-600"
                  }`}
                >
                  <p
                    className={`pb-3 font-semibold ${
                      isActive(item.slug, location.pathname)
                        ? "text-blue-600"
                        : "group-hover:text-blue-600"
                    }`}
                  >
                    {item.name}
                  </p>
                </div>
              </Link>
            </li>
          ))}
        </ul>
        <li className="ml-1.5">
          <Link className="group" to="/search">
            <div
              className={`transform transition-transform duration-100 active:scale-95 border-b-2 ${
                isActive("/search", location.pathname)
                  ? "border-blue-600"
                  : "border-transparent group-hover:border-blue-600"
              }`}
            >
              <svg
                className={`mb-2.5 ${
                  isActive("/search", location.pathname)
                    ? "stroke-blue-600"
                    : "group-hover:stroke-blue-600"
                }`}
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#000000"
                strokeWidth="1.5"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </div>
          </Link>
        </li>
      </ul>
    </header>
  );
}
