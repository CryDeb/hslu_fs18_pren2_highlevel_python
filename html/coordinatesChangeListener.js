/**
 * This interface should be implemented by classes
 * which are interested in coordinate changes, typically controllers.
 * @type CoordinatesChangeListener
 */
class CoordinatesChangeListener {
    constructor() {
        if(this.coordinatesChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}