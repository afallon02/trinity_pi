function show_networks() {
	var button = document.getElementById('wifi-networks-button');
	button.value = "Loading...";

	fetch('/wifi_networks')
		.then(response => response.json())
		.then(data => { 
			document.getElementById('main').innerHTML = data['response'] + "</br>";
		})
		.catch(e => console.error(e))
		.finally(function() {
			button.value = "Show WiFi Networks";
		});

}
