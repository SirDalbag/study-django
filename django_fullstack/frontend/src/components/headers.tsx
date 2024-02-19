import { Link } from "react-router-dom";

export function Header() {
    return (
      <header className="bg-white">
        <ul className="flex items-center list-none">
          <Link to="">
            <li className="px-4">
                <img className="h-8 w-auto" src="/icon.svg"/>
            </li>
          </Link>
          <Link to="">
            <li className="p-4 mt-2 font-semibold border-b-[3px] border-transparent hover:text-blue-600 hover:border-blue-600">Главное</li>
          </Link>
          <Link to="">
            <li className="p-4 mt-2 font-semibold border-b-[3px] border-transparent hover:text-blue-600 hover:border-blue-600">Аудио</li>
          </Link>
          <Link to="">
            <li className="p-4 mt-2 font-semibold border-b-[3px] border-transparent hover:text-blue-600 hover:border-blue-600">Комиксы</li>
          </Link>
          <Link to="">
            <li className="p-4 mt-2 font-semibold border-b-[3px] border-transparent hover:text-blue-600 hover:border-blue-600">Детям</li>
          </Link>
          <Link to="">
            <li className="p-4 mt-2 font-semibold border-b-[3px] border-transparent hover:text-blue-600 hover:border-blue-600">Мои книги</li>
          </Link>
        </ul>
      </header>
    );
  }