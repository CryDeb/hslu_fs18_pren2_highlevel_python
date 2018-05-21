
class PositionAndStateChangeListener {
    constructor() {
        if(this.positionChanged === undefined) {
            throw new TypeError("Must override method");
        }
        if(this.stateChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}