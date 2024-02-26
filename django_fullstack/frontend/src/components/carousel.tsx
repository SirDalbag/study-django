import { Link } from "react-router-dom";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function NextArrow(props: any) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, display: "block" }}
      onClick={onClick}
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        viewBox="0 0 24 24"
        fill="none"
        stroke="#000000"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M9 18l6-6-6-6" />
      </svg>
    </div>
  );
}

function PrevArrow(props: any) {
  const { className, style, onClick } = props;
  return (
    <div
      className={className}
      style={{ ...style, display: "block" }}
      onClick={onClick}
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        viewBox="0 0 24 24"
        fill="none"
        stroke="#000000"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M15 18l-6-6 6-6" />
      </svg>
    </div>
  );
}

const Carousel = ({ content }: { content: any }) => {
  const settings = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 2,
    slidesToScroll: 1,
    nextArrow: <NextArrow />,
    prevArrow: <PrevArrow />,
  };

  const elements = content.map((item: any) => (
    <div key={item.id}>
      <Link to={`/book/${item.id}`}>
        <div className="flex">
          <img
            className="w-72 h-96"
            src={`http://127.0.0.1:8000${item.cover_image}`}
          />
          <div className="flex items-center bg-white w-80">
            <div className="flex flex-col justify-center gap-6 p-4">
              <p className="font-semibold text-2xl tracking-wide">
                {item.title}
              </p>
              <p className="font-normal text-xl tracking-wide">
                {item.short_description}
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
    </div>
  ));

  return <Slider {...settings}>{elements}</Slider>;
};

export default Carousel;
