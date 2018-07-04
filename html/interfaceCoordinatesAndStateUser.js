/**
 * This interface should be implemented by classes
 * who have a use for coordinates and state, typically models.
 * @type InterfaceCoordinatesAndStateUser
 */
class InterfaceCoordinatesAndStateUser {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
    }
}