import './App.css';
import Axios from 'axios';

function App() {
  Axios.get("http://127.0.0.1:5000")
        .then(response =>{
            console.log(response.data)
            })
  return (
    <>
    <div className="App">
      <body style={{color: "#add8e6"}}>
        <center><h1 style={{color: "black"}}>Welcome To This Or That !</h1></center>
        <center><h4 style={{color: "black"}}>Created by Vince Dionisio, Abegail Palad, Kalyan Pullela, and Andrew Emerson</h4></center>
        <p style={{color: "black"}}>Instructions: Choose one of the two options that you believe is the most searched!two options that you believe is the most searched!</p>
        <p style={{color: "black"}}>If you get it right, move on to the next question.</p>
      </body>
    </div>
    <div class="flex-parent jc-center">
        <span id="question"></span>
        {/* <button onclick={game(string1)} style={{text-align:"center"}} style = {{font-size:"30px"}} >Random Word 1</button>
        <button onclick={game(string2)} style={{text-align:"center"}} style = {{font-size:"30px"}} >Random Word 2</button> */}
        <font face="Tahoma" color="red"><span id="score"></span></font>
    </div>
    </>
  );
}

export default App;
