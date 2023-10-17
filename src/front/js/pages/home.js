import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import Logo from "../../img/logo.jpg";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);

  useEffect(() => {
    if (store.token && store.token !== "" && store.token !== undefined)
      actions.getMessage();
  }, [store.token]);

  return (
    <div className="text-center mt-5 container home_max-width">
      <h1>Welcome to our site!</h1>

      <img src={Logo} />

      <div className=" my-5 fs-5 fw-bold">
        {store.message || "Log in to get your private message"}
      </div>
      <p className="fs-5">
        This boilerplate comes with lots of documentation:{" "}
        <a href="https://start.4geeksacademy.com/starters/react-flask">
          Read documentation
        </a>
      </p>
    </div>
  );
};
