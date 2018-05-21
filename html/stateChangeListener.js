
class StateChangeListener {
    constructor() {
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}