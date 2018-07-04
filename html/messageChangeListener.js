/**
 * This interface should be implemented by classes
 * which are interested in message changes, typically controllers.
 * @type MessageChangeListener
 */
class MessageChangeListener {
    constructor() {
        if(this.messageChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}