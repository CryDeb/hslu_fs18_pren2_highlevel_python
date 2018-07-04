/**
 * This class is a model class. It holds the data for a LogPrinter.
 * @type LogPrinterModel
 */
class LogPrinterModel extends InterfaceCoordinatesAndMessageAndStateUser {
    /**
     * This method creates a new instance of LogPrinterModel
     * @returns {LogPrinterModel}
     */
    constructor() {
        super();
        this.stateChangeListeners = [];
        this.coordinatesChangeListeners = [];
        this.messageChangeListeners = [];
        this.state = State["START_REACHED"];
        this.x = 0;
        this.y = 0;
        this.message = "";
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in state changes, typically controllers.
     * @param {object} obj
     */
    registerStateChangeListener(obj) {
        if(obj instanceof StateChangeListener || obj instanceof CoordinatesAndStateChangeListener ||
                obj instanceof MessageAndStateChangeListener || obj instanceof CoordinatesAndMessageAndStateChangeListener) {
            this.stateChangeListeners.push(obj);
            console.log("New stateChangeListener in LogPrinterModel" + obj);
        }
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in coordiante changes, typically controllers.
     * @param {object} obj
     */
    registerCoordinatesChangeListener(obj) {
        if(obj instanceof CoordinatesChangeListener || obj instanceof CoordinatesAndMessageChangeListener || 
                obj instanceof CoordinatesAndStateChangeListener || obj instanceof CoordinatesAndMessageAndStateChangeListener) {
            this.coordinatesChangeListeners.push(obj);
            console.log("New coordinatesChangeListener in LogPrinterModel");
        }
    }
    
    /**
     * This method is used for registrating objects
     * who are interested in message changes, typically controllers.
     * @param {object} obj
     */
    registerMessageChangeListener(obj) {
        if(obj instanceof MessageChangeListener || obj instanceof CoordinatesAndMessageChangeListener || 
                obj instanceof MessageAndStateChangeListener || obj instanceof CoordinatesAndMessageAndStateChangeListener) {
            this.messageChangeListeners.push(obj);
            console.log("New messageChangeListener in LogPrinterModel");
        }
    }
    
    /**
     * This method is used to notify all stateUsers
     * @param {State} state
     */
    setState(state) {
        if(state > 0 && state <8) {
            this.state = state;
            this.stateChangeListeners.forEach(function(item) {
                item.stateChanged(state);
            });
        }
    }
    
    /**
     * This method is used to notify all messageUsers
     * @param {String} message
     */
    setMessage(message) {
        this.message = message;
        this.messageChangeListeners.forEach(function(item) {
            item.messageChanged(message);
        });
    }
    
    /**
     * This method is used to notify all coordinateUsers
     * @param {int} x
     * @param {int} y
     */
    setCoordinates(x, y) {
        if(!isNaN(x) && !isNaN(y)) {
            this.x = x;
            this.y = y;
            this.coordinatesChangeListeners.forEach(function(item) {
                console.log("logPrinterModel calls coordinatesChanged");
                item.coordinatesChanged(x, y);
            });
        }
    }
}