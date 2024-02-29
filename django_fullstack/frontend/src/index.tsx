import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import "./index.css";
import store from "./components/store";
import Router from "./components/router";

const container = document.getElementById("root")!;

createRoot(container).render(
  <Provider store={store}>
    <Router />
  </Provider>
);
