export function restCon(payload)
{
    payload=JSON.stringify(payload);
    return fetch("http://localhost:5000 ", {
        method: "POST",
        body:payload,
           headers: {
               "Content-Type": "application/json"
           }
})
}