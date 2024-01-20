// GET request and takes the text provided by the user as input

let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    //initializes a request
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze"+"="+textToAnalyze, true);
    //sends the request 
    xhttp.send();
}
