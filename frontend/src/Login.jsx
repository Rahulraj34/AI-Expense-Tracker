import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {

const [username, setUsername] = useState("");
const [password, setPassword] = useState("");

const navigate = useNavigate();

const handleLogin = (e) => {
e.preventDefault();

if(username === "rahul" && password === "1234"){
    navigate("/home");
}
else{
    alert("Invalid username or password");
}

};

return(

<div style={{
display:"flex",
justifyContent:"center",
alignItems:"center",
height:"100vh",
background:"#0f172a"
}}>

<div style={{
background:"#1e293b",
padding:"40px",
borderRadius:"10px",
width:"350px",
textAlign:"center",
color:"white"
}}>

<h2>AI Expense Tracker</h2>
<p>Login to continue</p>

<form onSubmit={handleLogin}>

<input
type="text"
placeholder="Username"
value={username}
onChange={(e)=>setUsername(e.target.value)}
style={{
width:"100%",
padding:"10px",
marginTop:"10px",
borderRadius:"5px",
border:"none"
}}
/>

<input
type="password"
placeholder="Password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
style={{
width:"100%",
padding:"10px",
marginTop:"10px",
borderRadius:"5px",
border:"none"
}}
/>

<button
type="submit"
style={{
width:"100%",
padding:"10px",
marginTop:"15px",
background:"#3b82f6",
color:"white",
border:"none",
borderRadius:"5px",
cursor:"pointer"
}}
>
Login
</button>

</form>

<p style={{marginTop:"15px",fontSize:"12px"}}>
Demo Login <br/>
Username: rahul <br/>
Password: 1234
</p>

</div>

</div>

);

}

export default Login;