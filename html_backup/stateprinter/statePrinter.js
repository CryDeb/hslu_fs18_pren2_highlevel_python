
class StatePrinter extends StateChangeListener {
    constructor() {
        super();
        this.view = new StatePrinterView();
        this.model = new StatePrinterModel();
        this.model.registerStateChangeListener(this);
    }
    
    registrateModel(provider) {
        provider.registerStateUser(this.model);
    }
    
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