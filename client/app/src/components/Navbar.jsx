// Navbar.js
import React from 'react';
import styled from 'styled-components';

const Nav = styled.nav`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background-color: #007bff;
  color: white;
  height: 60px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
`;

const NavLogo = styled.div`
  font-size: 24px;
  font-weight: bold;
`;

const NavLinks = styled.div`
  display: flex;
  align-items: center;

  @media (max-width: 768px) {
    display: none;
  }
`;

const NavLink = styled.a`
  margin: 0 15px;
  text-decoration: none;
  color: white;
  font-size: 18px;
  transition: color 0.3s ease;

  &:hover {
    color: #ffdd57;
  }
`;

const MenuButton = styled.button`
  display: none;
  background: none;
  border: none;
  color: white;
  font-size: 24px;
  cursor: pointer;

  @media (max-width: 768px) {
    display: block;
  }
`;

const Navbar = () => {
  const handleMenuClick = () => {
    const links = document.getElementById('nav-links');
    if (links.style.display === 'flex') {
      links.style.display = 'none';
    } else {
      links.style.display = 'flex';
      links.style.flexDirection = 'column';
    }
  };

  return (
    <Nav>
      <NavLogo>MyApp</NavLogo>
      <NavLinks id="nav-links">
        <NavLink href="#home">Home</NavLink>
        <NavLink href="#about">About</NavLink>
        <NavLink href="#contact">Contact</NavLink>
      </NavLinks>
      <MenuButton onClick={handleMenuClick}>&#9776;</MenuButton>
    </Nav>
  );
};

export default Navbar;
