import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Login = () => {
  const { store, actions } = useContext(Context);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const token = sessionStorage.getItem("token");

  console.log("this is your token", token);

  const handleClick = () => {
    const requestOptions = {
      method: "Post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    };

    fetch(
      "https://fluffy-enigma-wwg6pp764q43g4xv-3001.app.github.dev/api/token",
      requestOptions
    )
      .then((resp) => {
        if (resp.status === 200) return resp.json();
      })
      .then((data) => {
        console.log("this came from the backend", data);
        sessionStorage.setItem("token", data.access_token); //I know it's access_token cos I saw it in Postman/Google Network tool
      })
      .catch((error) => {
        console.log("There was an error!!!", error);
      });
  };

  return (
    <div className="text-center mt-5 home_max-width container">
      <h1>Login</h1>
      {token && (token != "") & (token != undefined) ? (
        "You are logged in with this token" + token
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
          <button onClick={handleClick} className="btn btn-dark mt-5">Login</button>
        </div>
      )}
    </div>
  );
};
