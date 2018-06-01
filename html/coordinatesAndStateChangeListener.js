
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