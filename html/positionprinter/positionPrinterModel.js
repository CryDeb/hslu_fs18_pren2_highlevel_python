/**
 * This class is a model class. It holds the data for a PositionPrinter.
 * @type PositionPrinterModel
 */
class PositionPrinterModel extends InterfaceCoordinatesAndStateUser {
    /**
     * This method creates a new instance of PositionPrinterModel. 
     * @returns {PositionPrinterModel}
     */
    constructor() {
        super();
        this.stateChangeListeners = [];
        this.coordinatesChangeListeners = [];
        this.state = State["START_REACHED"];
        this.x = 0;
        this.y = 0;
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
            console.log("New stateChangeListener in PositionPrinterModel" + obj);
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
            console.log("New coordinatesChangeListener in PositionPrinterModel");
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