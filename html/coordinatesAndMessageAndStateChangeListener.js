/**
 * This interface should be implemented by classes
 * which are interested in message, coordinate and state changes, typically controllers.
 * @type CoordinatesAndMessageAndStateChangeListener
 */
class CoordinatesAndMessageAndStateChangeListener {
    constructor() {
        if(this.coordinatesChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.messageChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}