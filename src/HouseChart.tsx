import React from 'react';
import ReactECharts from 'echarts-for-react';
import { Card, Col} from 'react-bootstrap';
import './App.css';
import charts from './charts.json'

class HouseChart extends React.Component {
  build() {
    const echarts = [];
    for (const region in charts) {
      const regionChart = (charts as any)[region];
      echarts.push(
        <div>
        <Card>
          <Card.Header>
          <Card.Title>{region[0].toUpperCase() + region.slice(1)} (2.5M-, 3B+) </Card.Title>
          <Card.Text>
            <i className="text-muted" style={{fontSize: 9}}>$/Square Feet (Adjusted) = $/Square Feet + (2022 - Year Built)</i>
          </Card.Text>
          </Card.Header>
          <Card.Body>
            <ReactECharts option={{
              xAxis: {
                data: regionChart.x,
              },
              yAxis: {
              },
              tooltip: {
                trigger: 'axis',
              },
              series: [
              {
                name: '$/Square Feet (Adjusted)',
                data: regionChart.series[0],
                smooth: true,
                type: 'line'
                },
              {
                name: 'Sales Volume',
                data: regionChart.series[1],
                type: 'bar'
                }
              ]
            }} />
          </Card.Body>
        </Card>
        <br/>
        </div>
      );
    }
    return echarts;
  }

  render() {
    return (
      <Col>
      <br/>
      {this.build()}
      </Col>
    )
  }
}

export default HouseChart;
