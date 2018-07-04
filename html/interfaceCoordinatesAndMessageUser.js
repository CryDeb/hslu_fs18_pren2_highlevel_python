/**
 * This interface should be implemented by classes
 * who have a use for coordinates and message, typically models.
 * @type InterfaceCoordinatesAndMessageUser
 */
class InterfaceCoordinatesAndMessageUser {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setMessage === undefined) {
            throw new TypeError("Must override method");
        }
    }
}