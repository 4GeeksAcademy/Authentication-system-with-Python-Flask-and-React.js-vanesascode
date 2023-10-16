import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
	
			<div className="container">
				<div className="d-flex justify-content-between mt-4">
				<Link to="/" className="text-decoration-none">
					<span className="navbar-brand mb-0 h1 ">4Geeks Authentication</span>
				</Link>
			
					<Link to="/login">
						<button className="btn btn-primary">Login</button>
					</Link>
			
				</div>
			</div>
		
	);
};
