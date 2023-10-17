import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Navbar = () => {
  const { store, actions } = useContext(Context);
  return (
    <div className="container">
      <div className="d-flex justify-content-between mt-4">
        <Link to="/" className="text-decoration-none">
          <span className="navbar-brand mb-0 h1 ">4Geeks Authentication</span>
        </Link>

        {!store.token ? (
          <Link to="/login">
            <button className="btn btn-primary">Log In</button>
          </Link>
        ) : (
          <button className="btn btn-primary" onClick={() => actions.logout()}>
            Log Out
          </button>
        )}
      </div>
    </div>
  );
};
