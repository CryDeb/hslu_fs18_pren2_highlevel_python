
class LogPrinterModel extends StateAndCoordinatesUserInterface {
    constructor() {
        super();
        this.stateChangeListeners = [];
        this.positionChangeListeners = [];
        this.state = State["START_REACHED"];
        this.x = 0;
        this.y = 0;
    }
    
    registerStateChangeListener(obj) {
        if(obj instanceof StateChangeListener || obj instanceof PositionAndStateChangeListener) {
            this.stateChangeListeners.push(obj);
            console.log("New stateChangeListener in LogPrinterModel" + obj);
        }
    }
    
    registerPositionChangeListener(obj) {
        if(obj instanceof PositionChangeListener || obj instanceof PositionAndStateChangeListener) {
            this.positionChangeListeners.push(obj);
            console.log("New positionChangeListener in LogPrinterModel");
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
            this.positionChangeListeners.forEach(function(item) {
                console.log("logPrinterModel calls stateChanged");
                item.positionChanged(x, y);
            });
        }
    }
}