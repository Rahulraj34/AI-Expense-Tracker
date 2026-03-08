import { useEffect, useState } from "react"
import axios from "axios"

import "./style.css"

function ExpenseHistory(){

const [expenses,setExpenses] = useState([])

useEffect(()=>{

axios.get("https://ai-expense-tracker-qif2.onrender.com/expenses")
.then(res=>{

setExpenses(res.data)

})

},[])

return(

<div className="card">

<h2>Expense History</h2>

<table>

<thead>

<tr>

<th>Category</th>
<th>Amount</th>

</tr>

</thead>

<tbody>

{expenses.map((e,i)=>(

<tr key={i}>

<td>{e.category}</td>
<td>{e.amount}</td>

</tr>

))}

</tbody>

</table>

</div>

)

}

export default ExpenseHistory