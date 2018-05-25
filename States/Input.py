class Input:
    def __init__(self, action):
        self.action = action

    def __str__(self):
        return "    -> new input: " + self.action


Input.stop_command_received = Input("stop command received")
Input.start_command_received = Input("start command received")
Input.initialized = Input("initialized")
Input.destination_reached = Input("destination reached")
Input.clutch_destination_reached = Input("clutch destination reached")
Input.clutch_descended = Input("clutch descended")
Input.cube_grabbed = Input("cube grabbed")
Input.clutch_ascended = Input("clutch ascended")
Input.target_recognized = Input("target recognized")
Input.cube_released = Input("cube released")
Input.contact_switch_triggered = Input("contact switch triggered")


