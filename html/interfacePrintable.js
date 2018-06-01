
class InterfacePrintable {
    constructor() {
        if(this.print === undefined) {
            throw new TypeError("Must override method");
        }
    }
}