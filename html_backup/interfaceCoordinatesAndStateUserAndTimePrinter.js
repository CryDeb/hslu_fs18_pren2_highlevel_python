
class InterfaceCoordinatesAndStateUserAndTimePrinter {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.printTime === undefined) {
            throw new TypeError("Must override method");
        }
    }
}