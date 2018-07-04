/**
 * This interface should be implemented by classes
 * which are interested in state changes, typically controllers.
 * @type StateChangeListener
 */
class StateChangeListener {
    constructor() {
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}