import { Link } from "react-router-dom";

const navigation = [
  { name: "Пользовательское соглашение", slug: "/legal/user-agreement" },
  { name: "Условия подписки", slug: "/legal/subscription-terms" },
  { name: "Правила рекомендаций", slug: "/legal/recommendation-rules" },
  { name: "Справка", slug: "/legal/help" },
  { name: "Форум пожеланий", slug: "/wish-forum" },
];

export function Footer() {
  return (
    <footer className="border-t-2">
      <ul className="flex items-center justify-between list-none">
        <ul className="flex items-center">
          {navigation.map((item, index) => (
            <Link key={index} to={item.slug}>
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
