//zielmasten erreicht: stage clear
//package picket up: power up
//device stoppet ohne würfel abgesetz: mammamia
//startsignal: herewego
//parcour geschafft: theend
//http://www.mariomayhem.com/downloads/sounds/
class ControlUnit {
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
        this.timePrinters = [];
        this.registerStateUser(new Audioplayer());
        if(generatePrinters) {
            logPrinter = new LogPrinter();
            logPrinter.registrateModel(this);
            statePrinter = new StatePrinter();
            statePrinter.registrateModel(this);
            positionPrinter = new PositionPrinter();
            positionPrinter.registrateModel(this);
        }
    }
    
    run() {
        let self = this;
        self.connector.request(self, 0, 0);
        self.running = setInterval(function(){ 
            self.connector.request(self ,0, -1);
        }, 50);
        if(this.stopRequest) {
            clearInterval(self.running);
        }
    }
    
    startTrolley() {
        this.stopRequest = false;
        this.connector.request(this, 1, -1);
        this.run();
    }
    
    stopTrolley() {
        this.connector.request(this, 2, -1);
        this.stopRequest = true;
    }
    
    fetchResponse(response) {
        this.lastResponse = response;
        this.parseResponse(response);
    }
    
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
                this.setState(State[this.currentState]);
            }
            if(this.currentX !== item.x || this.currentY !== item.y) {
                this.currentX = item.x;
                this.currentY = item.y;
                console.log("new coordinates: x="+item.x+", y="+item.y);
                this.setCoordinates(item.x, item.y);
            }
            if(this.currentMessage !== item.message) {
                this.currentMessage = item.message;
                this.setMessage(item.message);
            }
        }
    }
    
    setState(state) {
        if(state >= State["DEVICE_STARTED"] && state <= State["DEVICE_STOPPED"]) {
            this.state = state;
            this.stateUsers.forEach(function(item) {
                item.setState(state);
            });
        }
    }
    
    setCoordinates(x, y) {
        this.coordinatesUsers.forEach(function(item) {
            item.setCoordinates(x, y);
        });
    }
    
    setMessage(message) {
        //ToDo: implement
    }
    
    //could be realised this way or directly in printState
    setTime(time) {
        this.timePrinters.forEach(function(item) {
            item.printTime(time);
        });
    }
    
    registerStateUser(obj) {
        if(obj instanceof InterfaceStateUser || obj instanceof InterfaceCoordinatesAndStateUser) {
            this.stateUsers.push(obj);
            console.log("New stateUser in controlUnit");
        }
    }
    
    registerCoordinatesUser(obj) {
        if(obj instanceof InterfaceCoordinatesUser || obj instanceof InterfaceCoordinatesAndStateUser) {
            this.coordinatesUsers.push(obj);
            console.log("New positionUser in controlUnit");
        }
    }
    
    registerTimePrinter(obj) {
        if(obj instanceof InterfaceTimePrinter || obj instanceof InterfaceCoordinatesAndStateUserAndTimePrinter) {
            this.timePrinters.push(obj);
            console.log("New timePrinter in controlUnit");
        }
    }
}