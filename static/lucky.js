/** processForm: get data from form and make AJAX call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    let year = $("#year").val();
    const resp = await axios.post("/api/get-lucky-num",{year: `${year}`});
    
    handleResponse(resp)
}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
     let num =resp.data.num.num;
     let num_fact = resp.data.num.fact;
     let year = resp.data.year.year;
     let year_fact =resp.data.year.fact;
    $("#lucky-results").html(`Your lucky number is ${num}. ${num_fact}. Your birth year ${year} fact is ${year_fact}`)
}


$("#lucky-form").on("submit", processForm);
