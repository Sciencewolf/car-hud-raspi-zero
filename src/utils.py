import obd


class Utils:
    def __init__(self):
        self.connection = obd.OBD('') # port neve
    

    def get_speed(self):
        cmd = obd.commands.SPEED

        response = self.connection.query(cmd)

        print(response.value)
