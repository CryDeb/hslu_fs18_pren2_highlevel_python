
class Connector {
    constructor(host) {
        this.host = host;
    }
    
    request(callback, action, index) {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                    callback.fetchResponse(this.responseText);
               }
            };
        xhttp.open("GET", this.host+"/api?action="+action+"&index="+index, true);
        xhttp.send();
    }
}