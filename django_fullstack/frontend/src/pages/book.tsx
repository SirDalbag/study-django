import { Link, useLocation, useParams } from "react-router-dom";
import { useConstructor } from "../components/hooks";
import * as constants from "../components/constants";
import * as bases from "../components/bases";

function isActive(slug: string, path: string): boolean {
  return path === slug ? true : false;
}

export default function Page() {
  const location = useLocation();
  const { id } = useParams();
  const book = useConstructor(
    constants.book,
    "book",
    `http://127.0.0.1:8000/api/book/${id}/`,
    false
  );

  const navigation = [
    { id: 1, name: "О книге", slug: `/book/${book?.id}` },
    { id: 2, name: "Впечатления", slug: "/book/reviews/:id" },
    { id: 3, name: "Похожие книги", slug: "/similar-books" },
  ];

  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex gap-8">
          <img
            className="w-80 h-full"
            src={`http://127.0.0.1:8000${book?.cover_image}`}
          />
          <div className="flex flex-col gap-2">
            <p className="text-lg underline tracking-wide">
              <Link to="" className="hover:text-blue-600">
                {book?.author}
              </Link>
            </p>
            <p className="font-semibold text-3xl">{book?.title}</p>
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
            <p className="text-lg pt-6 pb-6">{book?.description}</p>
          </div>
        </div>
      </div>
    </bases.Base>
  );
}
