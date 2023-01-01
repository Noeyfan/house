import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Navbar, NavDropdown } from 'react-bootstrap';
import HouseChart from './HouseChart';

function App() {
  return (
    <div>
    <Navbar bg="light" expand="lg">
    <Container>
    <Navbar.Brand href="/">Houses.fyi</Navbar.Brand>
    <NavDropdown title="Seattle" id="basic-nav-dropdown">
      <NavDropdown.Item disabled={true}>Coming Soon</NavDropdown.Item >
    </NavDropdown>
    </Container>
    </Navbar>
    <div>
      <Container>
        <HouseChart />
      </Container>
    </div>
    </div>
  );
}

export default App;
