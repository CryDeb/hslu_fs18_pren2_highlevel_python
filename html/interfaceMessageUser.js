/**
 * This interface should be implemented by classes
 * who have a use for messages typically models.
 * @type InterfaceMessageUser
 */
class InterfaceMessageUser {
    constructor() {
        if(this.setMessage === undefined) {
            throw new TypeError("Must override method");
        }
    }
}