/**
 * This interface should be implemented by classes
 * which are interested in message and state changes, typically controllers.
 * @type MessageAndStateChangeListener
 */
class MessageAndStateChangeListener {
    constructor() {
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.messageChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}