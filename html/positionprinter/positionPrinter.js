
class PositionPrinter extends PositionChangeListener {
    constructor() {
        super();
        this.view = new PositionPrinterView();
        this.model = new PositionPrinterModel();
        this.model.registerPositionChangeListener(this);
        this.view.moveToStart();
    }
    
    registrateModel(provider) {
        provider.registerCoordinatesUser(this.model);
    }
    
    positionChanged(x, y) {
        this.view.moveTo(x, y);
    }
}