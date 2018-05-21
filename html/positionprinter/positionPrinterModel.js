
class PositionPrinterModel extends CoordinatesUserInterface {
    constructor() {
        super();
        this.positionChangeListeners = [];
        this.x = 0;
        this.y = 0;
    }
    
    registerPositionChangeListener(obj) {
        if(obj instanceof PositionChangeListener || obj instanceof PositionAndStateChangeListener) {
            this.positionChangeListeners.push(obj);
            console.log("New positionChangeListener in PositionPrinterModel");
        }
    }
    
    setCoordinates(x, y) {
        if(!isNaN(x) && !isNaN(y)) {
            this.x = x;
            this.y = y;
            this.positionChangeListeners.forEach(function(item) {
                console.log("positionPrinterModel calls positionChanged");
                item.positionChanged(x, y);
            });
        }
    }
}