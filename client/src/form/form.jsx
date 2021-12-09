import React,{useState} from 'react'
import "./form.css";
import Multiselect from 'multiselect-react-dropdown';
import {restCon} from "./restCon";

const cuisines=require('./cuisines.json')['list'];
function Form() {

    const [selectedCuisines,setSelectedCuisines]=useState([]);
    const [model,setModel]=useState("random_forest");
    const [hasTableBooking,setHasTableBooking]=useState("1");
    const [hasOnlineDelivery,setHasOnlineDelivery]=useState("1");
    const [isDeliveringNow,setIsDeliveringNow]=useState("1");
    const [switchToOrderMenu,setSwitchToOrderMenu]=useState("1");


    async function submit(event)
    {
        event.preventDefault();

        const payload={
            "cuisines":[],
            "model":model,
            "has_table_booking":parseInt(hasTableBooking),
            "has_online_delivery":parseInt(hasOnlineDelivery),
            "is_delivering_now":parseInt(isDeliveringNow),
            "switch_to_order_menu":parseInt(switchToOrderMenu),
            "longitude":parseFloat(event['target']['elements']["longitude"]['value']),
            "latitude":parseFloat(event['target']['elements']["latitude"]['value']),
            "average_cost_for_two":parseInt(event.target.elements[3].value),
            "price_range":parseInt(event.target.elements[8].value),
            "votes":parseInt(event['target']['elements']["votes"]['value'])
        }

        for(let i=0;i<selectedCuisines.length;i++)
            payload['cuisines'].push(selectedCuisines[i]['name']);

        const res=await restCon(payload);     
        const body=await res.json();
        console.log(body);


    }

    return (
        <form className="form"  onSubmit={submit} >

            <label>Model</label>
            <select name="model" onChange={(e)=>setModel(e.value)}>
            <option value="random_forest">Random Forest</option>
            <option value="knn">K-NN</option>
            <option value="logistic_regression">Logistic Regression</option>
            <option value="svm">SVM</option>
            <option value="naive_bayes">Naive Bayes</option>
            </select>


            <label>Longitude</label>
            <input type="number" name="longitude"  min="-180" max="180" required/>

            <label>Latitude</label>
            <input type="number" name="latitude"  min="-90" max="90" required/>

            <label>Average Cost For Two</label>
            <input type="number" name="averageCostForTwo" min="0" required />

            <label>Has Table Booking</label>
            <select name="hasTableBooking" onChange={(e)=>setHasTableBooking(e.value)} >
            <option value="1">Yes</option>
            <option value="0">No</option>
            </select>

            <label>Has Online Delivery</label>
            <select name="hasOnlineDelivery" onChange={(e)=>{setHasOnlineDelivery(e.value)}} >
            <option value="1">Yes</option>
            <option value="0">No</option>
            </select>

            <label>Is Delivering Now</label>
            <select name="isDeliveringNow" onChange={(e)=>setIsDeliveringNow(e.value)}>
            <option value="1">Yes</option>
            <option value="0">No</option>
            </select>

            <label>Switch To Order Menu</label>
            <select name="switchToOrderMenu" onChange={(e)=>setSwitchToOrderMenu(e.value)}>
            <option value="1">Yes</option>
            <option value="0">No</option>
            </select>

            <label>Price Range</label>
            <input type="number" name="priceRange"  min="0" required />

            <label>Votes</label>
            <input type="number" name="votes"  min="0" required />


            <label>Cuisines</label>
            <Multiselect 
            onSelect={(selectedList)=>setSelectedCuisines(selectedList)} 
            onRemove={(selectedList)=>setSelectedCuisines(selectedList)}
            name="cuisines" options={cuisines} displayValue="name" 
            />

        
            
            <input type="submit" value="Submit" />

        </form>
    )
}

export default Form;