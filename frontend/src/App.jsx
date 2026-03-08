import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

import Login from "./Login"
import Dashboard from "./Dashboard"
import ExpenseHistory from "./ExpenseHistory"
import Chatbot from "./Chatbot"

import "./style.css"

function Home(){

return(

<div className="layout">

{/* Sidebar */}

<div className="sidebar">

<div className="logo">
AI Tracker
</div>

<ul>

<li>Dashboard</li>
<li>Expense History</li>
<li>AI Chatbot</li>
<li style={{color:"#f87171"}}>Logout</li>

</ul>

</div>

{/* Main Content */}

<div className="main">

<h1 className="title">
AI Expense Tracker
</h1>

<Dashboard/>

<ExpenseHistory/>

<Chatbot/>

</div>

</div>

)

}

function App(){

return(

<Router>

<Routes>

<Route path="/" element={<Login/>}/>

<Route path="/home" element={<Home/>}/>

</Routes>

</Router>

)

}

export default App