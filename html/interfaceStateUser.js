
class InterfaceStateUser {
    constructor() {
        if(this.setState === undefined) {
            throw new TypeError("Must override method");
        }
    }
}