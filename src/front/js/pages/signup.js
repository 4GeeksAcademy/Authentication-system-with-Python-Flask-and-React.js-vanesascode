import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate, Link } from "react-router-dom";
import "../../styles/home.css";

export const Signup = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  console.log("this is your token", store.token);

  const handleClick = () => {
    actions.login(email, password);
    // .then(() => {
    //This will only take place if the login() function returns true.
    // navigate("/");
    // });
  };

  if (store.token && (store.token != "") & (store.token != undefined))
    navigate("/");

  return (
    <div className="text-center mt-5 home_max-width container">
      <h1>Create account</h1>
      {store.token && (store.token != "") & (store.token != undefined) ? (
        "You are logged in with this token" + store.token
      ) : (
        <div>
          <input
            type="text"
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
          <button onClick={handleClick} className="btn btn-dark mt-5">
            Sign up
          </button>

          <p className="mt-3 mb-5">
            You already have an account? <Link to="/login"> Log In then </Link>
          </p>
        </div>
      )}
    </div>
  );
};
