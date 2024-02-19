import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import Router from "./components/router";

const container = document.getElementById('root')!;
const root = createRoot(container);

createRoot(document.getElementById("root")!).render(
  <Router />,
);
