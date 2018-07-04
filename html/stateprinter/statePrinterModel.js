/**
 * This class is a model class. It holds the data for a StatePrinter.
 * @type StatePrinterModel
 */
class StatePrinterModel extends InterfaceStateUser {
    /**
     * This method creates a new instance of StatePrinterModel
     * @returns {StatePrinterModel}
     */
    constructor() {
        super();
        this.state = State["DEVICE_STARTED"];
        this.stateChangeListeners = [];
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
     * This method is used to notify all stateUsers
     * @param {State} state
     */
    setState(state) {
        if(state > 0 && state < 8) {
            this.state = state;
            this.stateChangeListeners.forEach(function(item) {
                console.log("statePrinterModel calls stateChanged");
                item.stateChanged(state);
            });
        }
    }
}