/**
 * This class is a controller class. It takes states and
 * prints them in a stateView.
 * @type StatePrinter
 */
class StatePrinter extends StateChangeListener {
    /**
     * Creates a new instance of StatePrinter
     * @returns {StatePrinter}
     */
    constructor() {
        super();
        this.view = new StatePrinterView();
        this.model = new StatePrinterModel();
        this.model.registerStateChangeListener(this);
    }
    
    /**
     * This method is used to registrate the model in a provider.
     * @param {Object} provider : an object that provides new state
     */
    registrateModel(provider) {
        provider.registerStateUser(this.model);
    }
    
    /**
     * This method is called, when the State of the model changes.
     * @param {State} state
     */
    stateChanged(state) {
        let currentState = typeof State[state] === "undefined" ? state : State[state];
        console.log("state bevor viewCall: "+currentState);
        switch(currentState) {
            case 1:
                this.view.printDeviceStartet();
                break;
            case 2:
                this.view.printPackagePickedUp();
                break;
            case 3:
                this.view.printObstaclePassed();
                break;
            case 4:
                this.view.printTargetDetected();
                break;
            case 5:
                this.view.printTargetDropped();
                break;
            case 6:
                this.view.printDestinationReached();
                break;
            case 7:
                this.view.printDeviceStopped();
                break;
        }
    }
    
}