/**
 * This interface should be implemented by classes
 * who have a use for coordinates, message and state, typically models.
 * @type InterfaceCoordinatesAndMessageAndStateUser
 */
class InterfaceCoordinatesAndMessageAndStateUser {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setMessage === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
    }
}
