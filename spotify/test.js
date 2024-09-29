// GET REQUEST TEST


async function makeRequest(url, method, body ){
    let headers = {
         'X-Requested-With': 'XMLHttpRequest',
         'Content-Type': 'application/json',
     }

     if (method == "post") {
         const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
         headers['X-CSRFToken'] = csrf
     }

     let response = await fetch("ajax", {

        method: method,
        headers: headers,
        body: body
    })

    if (!response.ok) {
        console.error('Error fetching data:', response.statusText);
        return;
    }

    return await response.json()

}

async function getNumber() {

    console.log('worked')

    const data = await makeRequest("ajax", "get")

    console.log(data);
}

async function getData(e) {
    let name = e.target.innerText

    let data = await makeRequest("ajax", method="post", body=JSON.stringify({number: name}))

    let htmlName = document.getElementById('track')

}