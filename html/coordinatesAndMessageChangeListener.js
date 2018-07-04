/**
 * This interface should be implemented by classes
 * which are interested in message and coordinate changes, typically controllers.
 * @type CoordinatesAndMessageChangeListener
 */
class CoordinatesAndMessageChangeListener {
    constructor() {
        if(this.coordinatesChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.messageChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}