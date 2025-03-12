function generatePassword() {
    let length = document.getElementById("length").value;
    let complexity = document.getElementById("complexity").value;

    fetch(`http://127.0.0.1:5000/generate?length=${length}&complexity=${complexity}`)
    .then(response => response.json())  // Parse JSON response
    .then(data => {
        document.getElementById("password").value = data.password;
        checkStrength(data.password);
    })
    .catch(error => console.error("Error:", error));
}
