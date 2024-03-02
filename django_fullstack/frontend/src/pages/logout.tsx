import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as constants from "../components/constants";
import * as utils from "../components/utils";

export default function Page() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  useEffect(() => {
    dispatch({ type: constants.login.reset });
    dispatch({ type: constants.register.reset });

    utils.LocalStorage.remove("login.data.access");
    utils.LocalStorage.remove("login.data.refresh");

    navigate("/");
  }, []);

  return <div></div>;
}
