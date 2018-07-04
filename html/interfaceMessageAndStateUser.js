/**
 * This interface should be implemented by classes
 * who have a use for state and message, typically models.
 * @type InterfaceMessageAndStateUser
 */
class InterfaceMessageAndStateUser {
    constructor() {
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.setMessage === undefined) {
            throw new TypeError("Must override method");
        }
    }
}