
class PositionPrinter extends CoordinatesAndStateChangeListener {
    constructor() {
        super();
        this.xCanvas = 0;
        this.yCanvas = 0;
        this.view = new PositionPrinterView();
        this.model = new PositionPrinterModel();
        this.model.registerCoordinatesChangeListener(this);
        this.model.registerStateChangeListener(this);
        this.view.moveToStart();
    }
    
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
        provider.registerStateUser(this.model);
    }
    
    convertCoordinates(x, y) {
        this.xCanvas = 50 + (x * 600 / 350);
        this.yCanvas = 450 - 155 - (y * 105 / 110);
        console.log("new coords: "+x+", "+y);
        this.view.moveTo(this.xCanvas, this.yCanvas);
    }
    
    coordinatesChanged(x, y) {
        this.convertCoordinates(x, y);
    }
    
    stateChanged(state) {
        if(state === State["PACKAGE_PICKED_UP"]) {
            this.view.setCubePicketUp(true);
            this.view.setCubeDropped(false);
        } else if(state === State["PACKAGE_DROPPED"]) {
            this.view.setCubePicketUp(false);
            this.view.setCubeDropped(true);
        }
        this.view.printState(state);
    }
}