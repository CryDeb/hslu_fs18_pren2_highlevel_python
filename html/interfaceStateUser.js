/**
 * This interface should be implemented by classes
 * who have a use for state objects, typically models.
 * @type InterfaceStateUser
 */
class InterfaceStateUser {
    constructor() {
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
    }
}