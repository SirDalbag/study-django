import { createRoot } from "react-dom/client";
import "./index.css";
import Router from "./components/router";

const container = document.getElementById("root")!;

createRoot(document.getElementById("root")!).render(<Router />);
