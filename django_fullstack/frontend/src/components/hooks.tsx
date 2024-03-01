import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import * as components from "../components/components";

const useConstructor = (
  constantObject: any,
  stateObject: any,
  url: any,
  many: boolean = true
) => {
  const dispatch = useDispatch();
  const objects = useSelector((state: any) => state[stateObject]);

  async function getObjects() {
    if (!objects.load) {
      components.constructorWebAction(dispatch, constantObject, url, "GET");
    }
  }

  useEffect(() => {
    getObjects();
  }, []);

  return many ? objects.data?.message : objects.data?.message[0];
};

export { useConstructor };
