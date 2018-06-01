
class InterfaceTimePrinter {
    constructor() {
        if(this.printTime === undefined) {
            throw new TypeError("Must override method");
        }
    }
}