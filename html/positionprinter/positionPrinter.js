/**
 * This class is a controller class. It takes coordinates and states and
 * prints them in a positionView.
 * @type PositionPrinter
 */
class PositionPrinter extends CoordinatesAndStateChangeListener {
    /**
     * This method creates a new instance of PositionPrinter
     * @returns {PositionPrinter}
     */
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
    
    /**
     * This method is used to registrate the model in a provider.
     * @param {Object} provider : an object that provides new coordinates and new state
     */
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
        provider.registerStateUser(this.model);
    }
    
    /**
     * This method is used to convert coordinates given from the server
     * into coordinates, which can be printed in a 750x450 canvas.
     * @param {int} x
     * @param {int} y
     */
    convertCoordinates(x, y) {
        this.xCanvas = 50 + (x * 600 / 350);
        this.yCanvas = 450 - 155 - (y * 105 / 110);
        console.log("new coords: "+x+", "+y);
        this.view.moveTo(this.xCanvas, this.yCanvas);
    }
    
    /**
     * This method is called, when the coordinates of the model change.
     * @param {int} x
     * @param {int} y
     */
    coordinatesChanged(x, y) {
        this.convertCoordinates(x, y);
    }
    
    /**
     * This method is called, when the State of the model changes.
     * @param {State} state
     */
    stateChanged(state) {
        if(state === State["PACKAGE_PICKED_UP"]) {
            this.view.setCubePicketUp(true);
            this.view.setCubeDropped(false);
        } else if(state === State["PACKAGE_DROPPED"]) {
            this.view.setCubePicketUp(false);
            this.view.setCubeDropped(true);
            this.view.setFinalCoordinates(this.xCanvas, this.yCanvas);
        }
    }
}