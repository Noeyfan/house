import React from 'react';
import { Nav, Card, Alert, Container, Row, Col, Image, Tabs, Tab} from 'react-bootstrap';
import './App.css';

// load images from dir
const ctx = require.context('./img', false, /.png/)
const images:any = [];
for (const key of ctx.keys()) {
  images.push(<Image src={ctx(key)} fluid={true}/>)
}

class House extends React.Component {
  render() {
    return (
      <Col>
      <br/>
      <Card>
        <Card.Header>
        <Card.Title>Seattle Housing Data</Card.Title>
        </Card.Header>
        <Card.Body>
        <Card.Subtitle className="mb-2">2.5M-, 3B+, SFH sold in last 5 Years</Card.Subtitle>
        <i className="text-muted" style={{fontSize: 12}}>$/SQUARE FEET Adjusted = $/SQUARE FEET + (2022 - YEAR BUILT)</i>
        {images}
        </Card.Body>
      </Card>

      </Col>
    )
  }
}

export default House;
