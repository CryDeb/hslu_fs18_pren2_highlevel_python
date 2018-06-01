
class PositionPrinterModel extends InterfaceCoordinatesAndStateUser {
    constructor() {
        super();
        this.stateChangeListeners = [];
        this.coordinatesChangeListeners = [];
        this.state = State["START_REACHED"];
        this.x = 0;
        this.y = 0;
    }
    
    registerStateChangeListener(obj) {
        if(obj instanceof StateChangeListener || obj instanceof CoordinatesAndStateChangeListener) {
            this.stateChangeListeners.push(obj);
            console.log("New stateChangeListener in LogPrinterModel" + obj);
        }
    }
    
    registerCoordinatesChangeListener(obj) {
        if(obj instanceof CoordinatesChangeListener || obj instanceof CoordinatesAndStateChangeListener) {
            this.coordinatesChangeListeners.push(obj);
            console.log("New coordinatesChangeListener in LogPrinterModel");
        }
    }
    
    setState(state) {
        if(state > 0 && state <8) {
            this.state = state;
            this.stateChangeListeners.forEach(function(item) {
                item.stateChanged(state);
            });
        }
    }
    
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