import { Link } from "react-router-dom";
import * as bases from "../components/bases";
import Categories from "../components/categories";
import Carousel from "../components/carousel";

const categories = [
  { id: 1, name: "САМОРАЗВИТИЕ", slug: "/books/self-development" },
  { id: 2, name: "ФАНТАСТИКА", slug: "/books/fiction" },
  { id: 3, name: "РОМАНТИКА", slug: "/books/romance" },
  { id: 4, name: "ПСИХОЛОГИЯ", slug: "/books/psychology" },
  { id: 5, name: "ДЕТЕКТИВЫ", slug: "/books/detectives" },
  { id: 6, name: "ПРОЗА", slug: "/books/prose" },
  { id: 7, name: "ТРИЛЛЕРЫ И ХОРРОРЫ", slug: "/books/thrillers-and-horror" },
  { id: 8, name: "ФЭНТЕЗИ", slug: "/books/fantasy" },
  { id: 9, name: "НОН-ФИКШН", slug: "/books/non-fiction" },
  { id: 10, name: "КЛАССИКА", slug: "/books/classic" },
  { id: 11, name: "YOUNG ADULT", slug: "/books/young-adult" },
  { id: 12, name: "БИЗНЕС", slug: "/books/business" },
  { id: 13, name: "ИСТОРИЯ", slug: "/books/history" },
  { id: 14, name: "ЗДОРОВЬЕ", slug: "/books/health" },
  {
    id: 15,
    name: "БИОГРАФИИ И МЕМУАРЫ",
    slug: "/books/biographies-and-memoirs",
  },
];

const content = [
  <div key={1}>
    <Link to="">
      <div className="flex">
        <img className="w-72 h-96" src="static\MQa1yxXZ.jpeg" />
        <div className="flex items-center bg-white w-80">
          <div className="flex flex-col justify-center gap-6 p-4">
            <p className="font-semibold text-2xl tracking-wide">
              История отечественного кино
            </p>
            <p className="font-normal text-xl tracking-wide">
              Узнайте всю историю отечественного кино в аудиоформате: от
              рождения до революции до российского кино XXI века
            </p>
            <Link to="">
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
          </div>
        </div>
      </div>
    </Link>
  </div>,
  <Link to="" key={2}>
    <div className="flex">
      <img className="w-72 h-96" src="static\HneHQX1H.jpeg" />
      <div className="flex items-center bg-white w-80">
        <div className="flex flex-col justify-center gap-6 p-4">
          <p className="font-semibold text-2xl tracking-wide">Когната</p>
          <p className="font-normal text-xl tracking-wide">
            Девочка-дракон возвращается домой. Сериал о встрече двух миров
            читает Сергей Гилев
          </p>
          <Link to="">
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
        </div>
      </div>
    </div>
  </Link>,
  <Link to="" key={3}>
    <div className="flex">
      <img className="w-72 h-96" src="static\NECAyPFn.jpeg" />
      <div className="flex items-center bg-white w-80">
        <div className="flex flex-col justify-center gap-6 p-4">
          <p className="font-semibold text-2xl tracking-wide">Я тебя прощаю</p>
          <p className="font-normal text-xl tracking-wide">
            Как проработать семеные травмы и понять себя
          </p>
          <Link to="">
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
        </div>
      </div>
    </div>
  </Link>,
];

export default function Page() {
  return (
    <bases.Base>
      <div className="container mx-auto px-32 py-12">
        <div className="flex flex-col gap-8">
          <p className="font-semibold text-5xl tracking-wide">Все аудиокниги</p>
          <Categories content={categories} />
          <Carousel content={content} />
        </div>
      </div>
    </bases.Base>
  );
}