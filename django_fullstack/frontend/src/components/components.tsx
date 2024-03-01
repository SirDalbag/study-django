import axios from "axios";

export function constructorConstant(prefix: string) {
  return {
    load: `load${prefix}`,
    success: `success${prefix}`,
    fail: `fail${prefix}`,
    error: `error${prefix}`,
    reset: `reset${prefix}`,
  };
}

export function constructorReducer(constant: any) {
  return function (state = {}, action: { type: string; payload: any }) {
    switch (action.type) {
      case constant.load:
        return { load: true };
      case constant.success:
        return { load: false, data: action.payload };
      case constant.fail:
        return { load: false, fail: action.payload };
      case constant.error:
        return { load: false, error: action.payload };
      case constant.reset:
        return { load: false };
      default:
        return state;
    }
  };
}

export async function constructorWebAction(
  dispatch: any,
  constant: any,
  url: string,
  method: string = "GET",
  data: any = {},
  timeout: number = 5000
) {
  try {
    dispatch({ type: constant.load });
    const config: any = {
      url: url,
      method: method,
      timeout: timeout,
      data: data,
    };
    const response = await axios(config);
    if (response.status === 200 || response.status === 201) {
      dispatch({ type: constant.success, payload: response.data });
    } else {
      dispatch({ type: constant.error, payload: response.statusText });
    }
  } catch (error: any) {
    console.error(`constructorWebAction: ${url} ${method}`, error);
    dispatch({ type: constant.fail, payload: "Ошибка" });
  }
}
