
class StatePrinterModel extends StateUserInterface {
    constructor() {
        super();
        this.state = State["DEVICE_STARTED"];
        this.stateChangeListeners = [];
    }
    
    registerStateChangeListener(obj) {
        if(obj instanceof StateChangeListener || obj instanceof PositionAndStateChangeListener) {
            this.stateChangeListeners.push(obj);
            console.log("New stateChangeListener in StatePrinterModel" + obj);
        }
    }
    
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