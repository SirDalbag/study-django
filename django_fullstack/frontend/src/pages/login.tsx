// external
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import * as bases from "../components/bases";
import * as utils from "../components/utils";
import * as constants from "../components/constants";
import * as components from "../components/components";

export default function Page() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const login = useSelector((state: any) => state.login);
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  function sendForm(event: any) {
    event.preventDefault();

    if (form.password !== "" && !login.load) {
      components.constructorWebAction(
        dispatch,
        constants.login,
        `${constants.host}/api/token/`,
        "POST",
        { username: form.username, password: form.password }
      );
    } else {
      window.alert("Заполните пароль!");
    }
  }

  useEffect(() => {
    if (login && login.data) {
      utils.LocalStorage.set("login.data.access", login.data.access);
      utils.LocalStorage.set("login.data.refresh", login.data.refresh);
      setTimeout(() => {
        navigate("/");
      }, 2000);
    }
  }, [login]);

  useEffect(() => {
    if (constants.isDebug) {
      console.log("login: ", login);
    }
  }, [login]);

  return (
    <bases.Base>
      <div className={"flex flex-col justify-center items-center p-12 gap-2"}>
        <p className="font-semibold text-xl">Вход в аккаунт</p>
        <article>
          {login.error && (
            <div className="font-semibold text-lg text-red-600">
              {login.error}
            </div>
          )}
          {login.fail && (
            <div className="font-semibold text-lg text-yellow-400">
              {login.fail}
            </div>
          )}
          {login.data && (
            <div className="font-semibold text-lg text-green-500">
              Вы успешно вошли в аккаунт!
            </div>
          )}
        </article>

        <form
          className={"flex flex-col justify-center items-center gap-2"}
          onSubmit={sendForm}
        >
          <div className="relative mt-2 rounded-md shadow-sm">
            <input
              type="email"
              name="email"
              id="email"
              className="block w-[500px] rounded-md border-0 py-4 pl-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600"
              placeholder="Логин"
              value={form.username}
              onChange={(event) => {
                setForm({ ...form, username: event.target.value });
              }}
            />
          </div>
          <div className="relative mt-2 rounded-md shadow-sm">
            <input
              type={"password"}
              placeholder={"Пароль"}
              className="block w-[500px] rounded-md border-0 py-4 pl-4 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600"
              value={form.password}
              onChange={(event) => {
                setForm({
                  ...form,
                  password: utils.Regex.inputPassword(event.target.value),
                });
              }}
            />
          </div>
          <button
            type="submit"
            className="mt-4 rounded-md bg-blue-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-blue-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
            disabled={login.load}
          >
            Войти
          </button>
        </form>
      </div>
    </bases.Base>
  );
}
