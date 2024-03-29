import { Link } from "react-router-dom";
import Spinner from "./spinner";

const Categories = ({
  content,
  className,
}: {
  content: any;
  className?: string;
}) => {
  if (content === null || content === undefined) {
    return <Spinner />;
  }
  return (
    <div className={`flex flex-wrap gap-2 ${className}`}>
      {content.map((item: any) => (
        <Link to={`http://localhost:3000/category/${item.slug}`} key={item.id}>
          <p className="uppercase tracking-wide border-2 rounded-full py-1 px-2.5 bg-white hover:border-blue-600 hover:text-blue-600">
            {item.name}
          </p>
        </Link>
      ))}
    </div>
  );
};

export default Categories;
