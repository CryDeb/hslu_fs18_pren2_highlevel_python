/**
 * This interface should be implemented by classes
 * who have a use for coordinates, typically models.
 * @type InterfaceCoordinatesUser
 */
class InterfaceCoordinatesUser {
    constructor() {
        if(this.setCoordinates === undefined) {
            throw new TypeError("Must override method");
        }
    }
}