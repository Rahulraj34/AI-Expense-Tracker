import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login(){

const [username,setUsername] = useState("")
const [password,setPassword] = useState("")
const [message,setMessage] = useState("")

const navigate = useNavigate()

const handleLogin = async () => {

try{

const res = await axios.post(
"http://127.0.0.1:8000/login",
{
username:username,
password:password
}
)

if(res.data.message === "Login successful"){

navigate("/home")

}else{

setMessage(res.data.message)

}

}catch(error){

setMessage("Login failed")

}

}

return(

<div style={{textAlign:"center",marginTop:"100px"}}>

<h2>Login</h2>

<input
placeholder="Username"
onChange={(e)=>setUsername(e.target.value)}
/>

<br/><br/>

<input
type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}
/>

<br/><br/>

<button onClick={handleLogin}>
Login
</button>

<p>{message}</p>

</div>

)

}

export default Login