/**
 * This class is a controller class. It takes coordinates and states and
 * prints them in a logView.
 * @type LogPrinter
 */
class LogPrinter extends CoordinatesAndMessageAndStateChangeListener {
    /**
     * Creates a new instance of LogPrinter
     * @returns {LogPrinter}
     */
    constructor() {
        super();
        this.view = new LogPrinterView();
        this.model = new LogPrinterModel();
        this.model.registerStateChangeListener(this);
        this.model.registerCoordinatesChangeListener(this);
        this.model.registerMessageChangeListener(this);
    }
    
    /**
     * This method is used to registrate the model in a provider.
     * @param {Object} provider : an object that provides new coordinates and new state
     */
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
        provider.registerStateUser(this.model);
        provider.registerMessageUser(this.model);
    }
    
    /**
     * This method is called, when the coordinates of the model change.
     * @param {int} x
     * @param {int} y
     */
    coordinatesChanged(x, y) {
        this.view.print(x, y);
    }
    
    /**
     * This method is called, when the State of the model changes.
     * @param {State} state
     */
    stateChanged(state) {
        this.view.printState(state);
    }
    
    /**
     * This method is called, when the message of the model changes.
     * @param {String} message
     */
    messageChanged(message) {
        this.view.printMessage(message);
    }
}