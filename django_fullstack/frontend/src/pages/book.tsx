import { Link, useLocation } from "react-router-dom";
import * as bases from "../components/bases";
import Categories from "../components/categories";

const categories = [
  { id: 1, name: "ХУДОЖЕСТВЕННАЯ ЛИТЕРАТУРА", slug: "/books/fiction" },
  {
    id: 2,
    name: "МИФОЛОГИЯ И ФОЛЬКЛОР",
    slug: "/books/mythology-and-folklore",
  },
];

const navigation = [
  { id: 1, name: "О книге", slug: "/book/1" },
  { id: 2, name: "Впечатления", slug: "/book/reviews/:id" },
  { id: 3, name: "Похожие книги", slug: "/similar-books" },
];

function isActive(slug: string, path: string): boolean {
  return path === slug ? true : false;
}

export default function Page() {
  const location = useLocation();
  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex gap-8">
          <img className="w-80 h-full" src="../static/Tf5WHMUo.jpeg" />
          <div className="flex flex-col gap-2">
            <Link to="">
              <p className="text-lg underline tracking-wide hover:text-blue-600">
                Иллюстрации Антейку
              </p>
            </Link>
            <p className="font-semibold text-3xl">Русские народные сказки</p>
            <Link to="" className="pt-6">
              <button className="bg-blue-600 rounded-md hover:bg-blue-700 transform transition-transform duration-100 active:scale-95">
                <div className="flex items-center gap-2 py-2 px-6">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="#ffffff"
                    stroke="#ffffff"
                    strokeWidth="1.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polygon points="5 3 19 12 5 21 5 3"></polygon>
                  </svg>
                  <span className="font-semibold text-lg text-white tracking-wide">
                    Слушать
                  </span>
                </div>
              </button>
            </Link>
            <ul className="flex gap-6 mt-8">
              {navigation.map((item) => (
                <li key={item.id}>
                  <Link className="group" to={item.slug}>
                    <div
                      className={`transform transition-transform duration-100 active:scale-95 border-b-2 ${
                        isActive(item.slug, location.pathname)
                          ? "border-blue-600"
                          : "border-transparent group-hover:border-blue-600"
                      }`}
                    >
                      <p
                        className={`pb-3 text-lg ${
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
            <p className="text-lg pt-6 pb-6">
              Сборник русских народных сказок, записанных Афанасьевым. Необычная
              интерпретация образов любимых героинь — Марьи Моревны, Василисы
              Прекрасной, Бабы-яги — с привязкой к архетипам. Атмосферные
              иллюстрации Антейку.
            </p>
            <Categories content={categories} />
          </div>
        </div>
      </div>
    </bases.Base>
  );
}
