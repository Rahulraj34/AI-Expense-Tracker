import { useEffect, useState } from "react"
import axios from "axios"

import { Pie } from "react-chartjs-2"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js"

import "./style.css"

ChartJS.register(ArcElement, Tooltip, Legend)

function Dashboard(){

const [chartData,setChartData] = useState(null)
const [insights,setInsights] = useState(null)

useEffect(()=>{

axios.get("https://ai-expense-tracker-qif2.onrender.com/expenses")
.then(res=>{

const expenses = res.data

if(!expenses.length) return

let categoryTotals={}
let total=0

expenses.forEach(e=>{

total += e.amount

if(categoryTotals[e.category]){
categoryTotals[e.category]+=e.amount
}else{
categoryTotals[e.category]=e.amount
}

})

const highestCategory = Object.keys(categoryTotals).reduce((a,b)=>
categoryTotals[a]>categoryTotals[b]?a:b
)

setInsights({
total:total,
transactions:expenses.length,
highest:highestCategory
})

setChartData({

labels:Object.keys(categoryTotals),

datasets:[
{
data:Object.values(categoryTotals),
backgroundColor:[
"#f87171",
"#60a5fa",
"#fbbf24",
"#34d399",
"#a78bfa"
]
}
]

})

})

},[])

return(

<div className="card">

<h2>Expense Analytics</h2>

{chartData ? <Pie data={chartData}/> : <p>No expense data</p>}

{insights &&(

<div className="insight-box">

<h3>AI Spending Insights</h3>

<p>Total Spent: ₹{insights.total}</p>
<p>Total Transactions: {insights.transactions}</p>
<p>Highest Spending Category: {insights.highest}</p>

</div>

)}

</div>

)

}

export default Dashboard