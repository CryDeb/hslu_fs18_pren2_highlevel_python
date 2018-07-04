/**
 * This interface should be implemented by classes
 * which are interested in state and coordinate changes, typically controllers.
 * @type CoordinatesAndStateChangeListener
 */
class CoordinatesAndStateChangeListener {
    constructor() {
        if(this.coordinatesChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}