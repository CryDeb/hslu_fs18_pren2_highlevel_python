/**
 * This interface should be implemented by classes
 * which are able to be printed.
 * @type InterfacePrintable
 */
class InterfacePrintable {
    constructor() {
        if(this.print === undefined) {
            throw new TypeError("Must override method");
        }
    }
}