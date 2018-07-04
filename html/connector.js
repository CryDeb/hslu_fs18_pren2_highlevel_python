/**
 * This class is used for sending requests.
 * The responses can be catched with callbacks.
 * @type Connector
 */
class Connector {
    /**
     * This method creates a new instance of Connector
     * @param {string} host
     * @returns {Connector}
     */
    constructor(host) {
        this.host = host;
    }
    
    /**
     * This method is used for sending a request
     * to the given host.
     * @param {function} callback
     * @param {int} action
     * @param {int} index
     */
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