import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate, Link } from "react-router-dom";
import "../../styles/home.css";

export const Login = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  console.log("this is your token", store.token);

  const handleClick = (e) => {
    e.preventDefault();
    // if (!store.token || store.token == "" || store.token == undefined) {
    //   alert("email or password wrong");
    // }

    actions.login(email, password);
  };

  if (store.token && (store.token != "") & (store.token != undefined)) {
    navigate("/");
  }

  return (
    <div className="text-center mt-5 home_max-width container">
      <h1>Log In</h1>
      {store.token && (store.token != "") & (store.token != undefined) ? (
        "You are logged in with this token" + store.token
      ) : (
        <div>
          <form onSubmit={handleClick}>
            <input
              type="email"
              placeholder="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="form-control mt-3"
            />
            <input
              type="password"
              placeholder="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="form-control mt-3"
            />
            <button type="submit" className="btn btn-dark mt-5">
              Login
            </button>
          </form>

          <p className="mt-3 mb-5">
            Are you new here? <Link to="/signup">Sign up first </Link>
          </p>
        </div>
      )}
    </div>
  );
};
