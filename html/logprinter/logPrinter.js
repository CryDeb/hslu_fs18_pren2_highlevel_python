
class LogPrinter extends PositionAndStateChangeListener {
    constructor() {
        super();
        this.view = new LogPrinterView();
        this.model = new LogPrinterModel();
        this.model.registerStateChangeListener(this);
        this.model.registerPositionChangeListener(this);
    }
    
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
        provider.registerStateUser(this.model);
    }
    
    positionChanged(x, y) {
        this.view.print(x, y);
    }
    
    stateChanged(state) {
        this.view.printState(state);
    }
    
    test(s) {
        this.model.setState(s);
        this.model.setCoordinates(10, 12);
    }
}