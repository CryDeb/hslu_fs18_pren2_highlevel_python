/**
 * This class is the controlUnit of the Webclient. It is responsible
 * for sending request, defining callbacks and call the different changeListeners(users)
 * @type ControlUnit
 */
class ControlUnit {
    /**
     * This method creates a new instance of ConrolUnit
     * @param {string} host : the address of the server
     * @param {boolean} generatePrinters : if true, the different printers
     * will be generated automatically
     * @returns {ControlUnit} 
     */
    constructor(host, generatePrinters) {
        this.currentIndex = 0;
        this.currentX = 0;
        this.currentY = 0;
        this.currentState = null;
        this.currentMessage = null;
        this.stopRequest = false;
        this.lastResponse = "";
        this.connector = new Connector(host);
        this.stateUsers = [];
        this.coordinatesUsers = [];
        this.messageUsers = [];
        this.registerStateUser(new Audioplayer());
        this.startTime = null;
        this.destinationReached = false;
        this.packageDropped = false;
        if(generatePrinters) {
            logPrinter = new LogPrinter();
            logPrinter.registrateModel(this);
            statePrinter = new StatePrinter();
            statePrinter.registrateModel(this);
            positionPrinter = new PositionPrinter();
            positionPrinter.registrateModel(this);
        }
    }
    
    /**
     * This method sends requests in an intervall
     * to retrieve new jsonObjects from the server. This method
     * should be called only once while the programm is running.
     */
    run() {
        let self = this;
        self.connector.request(self, 0, 0);
        self.running = setInterval(function(){ 
            self.connector.request(self, 0, -1);
            self.setTime(new Date().getTime());
        }, 200);
        if(this.stopRequest) {
            clearInterval(self.running);
        }
    }
    
    /**
     * This method sends a request to start the trolley
     * and calls run()
     */
    startTrolley() {
        this.stopRequest = false;
        this.connector.request(this, 1, -1);
        this.startTime = new Date().getTime();
        this.run();
    }
    
    /**
     * This method sends a request to stop the trolley
     */
    stopTrolley() {
        this.connector.request(this, 2, -1);
        this.stopRequest = true;
        this.destinationReached = true;
    }
    
    /**
     * This method sets the last response to the current response
     * @param {Object} response : a jsonObject with either
     *  history
     *  and index
     *  or an error
     */
    fetchResponse(response) {
        this.lastResponse = response;
        this.parseResponse(response);
    }
    
    /**
     * This method parses a jsonObject
     * @param {object} response : a jsonObject with either
     *  history
     *  and index
     *  or an error
     */
    parseResponse(response) {
        let jsonObject = typeof response === "object" ? response : JSON.parse(response);
        if(jsonObject.hasOwnProperty("error")) {
            if(jsonObject.error !== null) {
                throw new Error("Error from Server: "+jsonObject.error);
            }
        }
        else if(jsonObject.hasOwnProperty("history")) {
            this.parseHistory(jsonObject.history);
        } 
        else if(jsonObject.hasOwnProperty("index")) {
            if(this.currentIndex < jsonObject.index) {
                this.currentIndex = jsonObject.index;
                this.connector.request(this, 0, this.currentIndex);
            }
        }
    }
    
    /**
     * This method parses a jsonObject
     * @param {object} history : a jsonObject with 
     *  x coordinate
     *  y coordinate
     *  message
     *  and state
     */
    parseHistory(history) {
        if(typeof history !== "object" || history === null) {
            throw new TypeError("Invalid param. Expected Json object but was "+typeof history);
        }
        for (let i=0; i<history.length; i++) {
            let item = history[i];
            if(!item.hasOwnProperty("state") ||
                    !item.hasOwnProperty("x") ||
                    !item.hasOwnProperty("y") ||
                    !item.hasOwnProperty("message")) {
                throw new TypeError("Invalid param. Object should have properties: x, y, message and state. Item is:"+JSON.stringify(item));
            }
            if(this.currentState !== item.state) {
                console.log("new State: "+item.state);
                this.currentState = item.state;
                if(this.currentState === "DESTINATION_REACHED" || this.currentState === "DEVICE_STOPPED") {
                    this.destinationReached = true;
                    this.setState(State["DESTINATION_REACHED"]);
                }
                if(this.currentState === "PACKAGE_DROPPED") {
                    this.packageDropped = true;
                }
                this.setState(State[this.currentState]);
            }
            if(this.currentX !== item.x || this.currentY !== item.y) {
                this.currentX = Math.floor(item.x);
                this.currentY = Math.floor(item.y);
                console.log("new coordinates: x="+item.x+", y="+item.y);
                this.setCoordinates(Math.floor(item.x), Math.floor(item.y));
            }
            if(this.currentMessage !== item.message) {
                this.currentMessage = item.message;
                this.setMessage(item.message);
            }
        }
    }
    
    /**
     * This method is used to notify all stateUsers
     * @param {State} state
     */
    setState(state) {
        if(state >= State["DEVICE_STARTED"] && state <= State["DEVICE_STOPPED"]) {
            this.state = state;
            this.stateUsers.forEach(function(item) {
                item.setState(state);
            });
        }
    }
    
    /**
     * This method is used to notify all coordinateUsers
     * @param {int} x
     * @param {int} y
     */
    setCoordinates(x, y) {
        this.coordinatesUsers.forEach(function(item) {
            item.setCoordinates(x, y);
        });
        var outputArea = document.getElementById("coordinates");
        if(outputArea !== null && !this.packageDropped) {
            outputArea.innerHTML = "x: "+x+", y: "+y;
        }
    }
    
    /**
     * This method is called to notify all messageUsers
     * @param {string} message
     */
    setMessage(message) {
        this.messageUsers.forEach(function(item) {
            item.setMessage(message);
        });
    }

    /**
     * This method is used for setting a new time.
     * @param {timestamp} time
     */
    setTime(time) {
        var outputArea = document.getElementById("time");
        if(outputArea !== null && !this.destinationReached) {
            outputArea.innerHTML = time - this.startTime;
        }
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in state changes
     * @param {object} obj
     */
    registerStateUser(obj) {
        if(obj instanceof InterfaceStateUser || obj instanceof InterfaceCoordinatesAndStateUser || 
                obj instanceof InterfaceMessageAndStateUser || obj instanceof InterfaceCoordinatesAndMessageAndStateUser) {
            this.stateUsers.push(obj);
            console.log("New stateUser in controlUnit");
        }
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in coordinate changes
     * @param {object} obj
     */
    registerCoordinatesUser(obj) {
        if(obj instanceof InterfaceCoordinatesUser || obj instanceof InterfaceCoordinatesAndMessageUser || 
                obj instanceof InterfaceCoordinatesAndStateUser || obj instanceof InterfaceCoordinatesAndMessageAndStateUser) {
            this.coordinatesUsers.push(obj);
            console.log("New positionUser in controlUnit");
        }
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in message changes
     * @param {object} obj
     */
    registerMessageUser(obj) {
        if(obj instanceof InterfaceMessageUser || obj instanceof InterfaceCoordinatesAndMessageUser || 
                obj instanceof InterfaceMessageAndStateUser || obj instanceof InterfaceCoordinatesAndMessageAndStateUser) {
            this.messageUsers.push(obj);
            console.log("New messageUser in controlUnit");
        }
    }
}