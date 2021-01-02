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

function monitor_enable() {
	var button = document.getElementById('monitor-enable-button');
	button.value = "Loading...";

	fetch('/monitor_mode_enable')
		.then(response => response.json())
		.then(data => { 
			console.log(data);
		})
		.catch(e => console.error(e))
		.finally(function() {
			button.value = "Monitor Mode Enable";
		});
}


function monitor_disable() {
	var button = document.getElementById('monitor-disable-button');
	button.value = "Loading...";

	fetch('/monitor_mode_disable')
		.then(response => response.json())
		.then(data => { 
			console.log(data);
		})
		.catch(e => console.error(e))
		.finally(function() {
			button.value = "Monitor Mode Disable";
		});
}

function show_network_interfaces() {
	var button = document.getElementById('show-network-interfaces')
	button.value = "Loading...";

	fetch('/show_network_interfaces')
		.then(response => response.json())
		.then(data => { 
			console.log(data);
		})
		.catch(e => console.error(e))
		.finally(function() {
			button.value = "Show Network Interfaces";
		});

}
