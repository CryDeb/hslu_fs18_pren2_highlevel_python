
class LogPrinter extends CoordinatesAndStateChangeListener {
    constructor() {
        super();
        this.view = new LogPrinterView();
        this.model = new LogPrinterModel();
        this.model.registerStateChangeListener(this);
        this.model.registerCoordinatesChangeListener(this);
    }
    
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
        provider.registerStateUser(this.model);
    }
    
    coordinatesChanged(x, y) {
        this.view.print(x, y);
    }
    
    stateChanged(state) {
        this.view.printState(state);
    }
}