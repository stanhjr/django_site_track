var stripe = Stripe('pk_test_51Lg4MyK6rkKpcwrpM9imgTsK4IupHl9BSeuzPgUQRWExpYnqHxr3Xe9juCUXGR10JXsiknlxoUeZGpTTw2lGG1UF00K0cn1Xv4');

let sub1Btn = document.getElementById('sub-12-month')

if (sub1Btn){
	sub1Btn.onclick = () => {
			getStripe("sub-1-truck")
		}
}

let sub12Btn = document.getElementById('sub-12-month')
if (sub12Btn){sub12Btn.onclick = () => {
			getStripe("sub-12-month")
		}}

let sub36Btn = document.getElementById('sub-36-month')
if (sub36Btn){sub36Btn.onclick = () => {
			getStripe("sub-36-month")
		}}


function getStripe(plane){
    let xhr = new XMLHttpRequest();
	xhr.open("GET", '/get_session_id?plan=' + plane)
	xhr.setRequestHeader("Accept", "application/json");
	xhr.setRequestHeader("Content-Type", "application/json")
	xhr.setRequestHeader("Access-Control-Allow-Origin", window.location.host)
	xhr.send()
	xhr.onload = () => {
		if (xhr.status === 200){
			let session_id = JSON.parse(xhr.responseText)["session_id"]
			console.log(session_id)
			stripe.redirectToCheckout({
			sessionId: session_id
			})
			.then(function(result) {
			console.log("STRIPE", result.error.message)
			let displayError = document.getElementById('error-message');
			displayError.textContent = result.error.message;});
	}}
}




