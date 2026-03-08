import { useState } from "react"
import axios from "axios"
import "./style.css"

function Chatbot(){

const [message,setMessage] = useState("")
const [chat,setChat] = useState([])
const [loading,setLoading] = useState(false)

const sendMessage = async ()=>{

if(message.trim()==="") return

const userMessage = message

setChat([...chat,{type:"user",text:userMessage}])

setMessage("")
setLoading(true)

try{

const res = await axios.post(
"https://ai-expense-tracker-qif2.onrender.com/chat",
{message:userMessage}
)

setChat(prev=>[
...prev,
{type:"bot",text:res.data.response}
])

}catch(error){

setChat(prev=>[
...prev,
{type:"bot",text:"Server error"}
])

}

setLoading(false)

}

return(

<div className="card">

<h2>AI Chatbot</h2>

<div style={{
maxHeight:"250px",
overflowY:"auto",
marginBottom:"15px"
}}>

{chat.map((c,i)=>(

<div key={i} style={{marginBottom:"8px"}}>

{c.type==="user" ? (

<div className="chat-user">
You: {c.text}
</div>

) : (

<div className="chat-bot">
Bot: {c.text}
</div>

)}

</div>

))}

{loading && (

<div className="chat-bot">
Bot is typing...
</div>

)}

</div>

<div style={{
display:"flex",
justifyContent:"center"
}}>

<input
value={message}
onChange={(e)=>setMessage(e.target.value)}
placeholder="Example: I spent 200 on food"
/>

<button onClick={sendMessage}>
Send
</button>

</div>

</div>

)

}

export default Chatbot