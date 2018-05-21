
class PositionChangeListener {
    constructor() {
        if(this.positionChanged === undefined) {
            throw new TypeError("Must override method");
        }
    }
}