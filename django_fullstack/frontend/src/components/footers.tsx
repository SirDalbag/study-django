import { Link } from "react-router-dom";

const navigation = [
  { id: 1, name: "Пользовательское соглашение", slug: "/legal/user-agreement" },
  { id: 2, name: "Условия подписки", slug: "/legal/subscription-terms" },
  { id: 3, name: "Правила рекомендаций", slug: "/legal/recommendation-rules" },
  { id: 4, name: "Справка", slug: "/legal/help" },
  { id: 5, name: "Форум пожеланий", slug: "/wish-forum" },
];

export function Footer() {
  return (
    <footer className="border-t-2">
      <ul className="flex items-center justify-between list-none">
        <ul className="flex items-center">
          {navigation.map((item) => (
            <Link key={item.id} to={item.slug}>
              <li className="p-4 mt-2 text-gray-500 hover:text-gray-900">
                {item.name}
              </li>
            </Link>
          ))}
        </ul>
        <li className="p-4 mt-2 text-gray-500">© 2024, ООО «Букмейт»</li>
      </ul>
    </footer>
  );
}
