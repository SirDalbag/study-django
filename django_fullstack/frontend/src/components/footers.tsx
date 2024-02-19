import { Link } from "react-router-dom";

export function Footer() {
    return (
      <footer className="border-t-2">
        <ul className="flex items-center  justify-between list-none">
            <ul className="flex items-center">
                <Link to="">
                <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">Пользовательское соглашение</li>
                </Link>
                <Link to="">
                    <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">Условия подписки</li>
                </Link>
                <Link to="">
                    <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">Правила рекомендаций</li>
                </Link>
                <Link to="">
                    <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">Справка</li>
                </Link>
                <Link to="">
                    <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">Форум пожеланий</li>
                </Link>
            </ul>
          <Link to="">
            <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">© 2024, ООО «Букмейт»</li>
          </Link>
        </ul>
      </footer>
    );
  }