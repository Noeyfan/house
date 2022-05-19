import React from 'react';
import { Nav, Card, Alert, Container, Row, Col, Image, Tabs, Tab} from 'react-bootstrap';
import './App.css';

// load images from dir
const ctx = require.context('./img', false, /.png/)
const images:any = [];
for (const key of ctx.keys()) {
  images.push(<Row><Image src={ctx(key)} fluid={true}/></Row>)
}

class House extends React.Component {
  render() {
    return (
      <Col>
      <br/>
      <Card>
        <Card.Header>
        <Card.Subtitle>2.5M-, 3B+, SFH Sold in Last 5 Years</Card.Subtitle>
        <Card.Text>
          <i className="text-muted" style={{fontSize: 9}}>$/SQUARE FEET Adjusted = $/SQUARE FEET + (2022 - YEAR BUILT)</i>
        </Card.Text>
        </Card.Header>
        <Card.Body>
        {images}
        </Card.Body>
      </Card>

      </Col>
    )
  }
}

export default House;
