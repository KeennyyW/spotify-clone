async function getNumber() {
    let response = await fetch(``, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
    });

    if (!response.ok) {
        console.error('Error fetching data:', response.statusText);
        return;
    }

    let data = await response.json();
    console.log(data);
}

// Example call
getNumber('your_album_link_here');
