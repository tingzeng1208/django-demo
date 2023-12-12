// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       {/* <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"j
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header> */}
//       <p>This is my react front</p>
//     </div>
//   );
// }

// 

import axios from 'axios';
import React from 'react'


class App extends React.Component {
  
  state = {
    employees: [],
    firms: []
  }

  componentDidMount() {
    let employee_url = 'http://127.0.0.1:8000/hubzone/api/employee/';
    let firm_url = 'http://127.0.0.1:8000/hubzone/api/firm/';
    axios.get(employee_url).then(res => {
      console.log(res);
      this.setState({ employees: res.data });
    }).catch(err => { console.log(err) });
    axios.get(firm_url).then(res => {
      console.log(res);
      this.setState({ firms: res.data });
    }).catch(err => { console.log(err)});
  }

  render() {
    return (
      <html>
        <header className="App-header">Employee and firm list</header>
      <p>Employee List</p>
      <div>
        <ul>
            {this.state.employees.map(employee => <li>{employee.first_name} {employee.last_name} {employee.email} {employee.firm.name}</li>)}
        </ul>
        </div>
        <p>Firm List</p>
      <div>
        <ul>
          {this.state.firms.map(firms => <li>{firms.name}</li>)}
        </ul>
        </div>
      </html>
    )
  }

}

export default App;