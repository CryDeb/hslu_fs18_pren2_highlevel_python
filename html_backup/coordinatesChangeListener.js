
class CoordinatesChangeListener {
    constructor() {
        if(this.coordinatesChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}