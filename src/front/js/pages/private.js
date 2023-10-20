import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";

export const Private = (props) => {
  const [color, setColor] = useState("");
  const [pet, setPet] = useState("");
  const [meal, setMeal] = useState("");
  const { store, actions } = useContext(Context);
  //   const params = useParams();

  useEffect(() => {
    if (store.token && store.token !== "" && store.token !== undefined)
      actions.getMessage();
  }, [store.token]);

  const handleClick = (e) => {
    e.preventDefault();
    actions.completeFavs(color, pet, meal);
    actions.setRegistrationInProgress(true);

    // CONDITIONALS with FRONTEND messages (below in the jsx):
    setTimeout(() => {
      actions.setRegistrationInProgress(false);
    }, 2000);
  };

  return (
    <div className="text-center mt-5 container home_max-width">
      <h1>This is your private area{store.message}</h1>

      <p className="fs-5 mt-4 mb-5">Complete your personal information:</p>

      <form onSubmit={handleClick}>
        <input
          type="text"
          placeholder="Favorite color"
          value={color}
          onChange={(e) => setColor(e.target.value)}
          className="form-control mt-3"
        />
        <input
          type="text"
          placeholder="Favorite pet"
          value={pet}
          onChange={(e) => setPet(e.target.value)}
          className="form-control mt-3"
        />
        <input
          type="text"
          placeholder="Favorite meal"
          value={meal}
          onChange={(e) => setMeal(e.target.value)}
          className="form-control mt-3"
        />
        <button
          type="submit"
          className="btn btn-dark mt-5"
          disabled={store.registrationInProgress}
        >
          Save
        </button>
        {store.registrationSuccess && <div className="fs-3">Saved!</div>}
      </form>
    </div>
  );
};

//////////////////////////////////////////////////////////////que es esto?:
Private.propTypes = {
  match: PropTypes.object,
};
