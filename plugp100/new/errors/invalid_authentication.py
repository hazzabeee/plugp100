class InvalidAuthentication(Exception):
    def __init__(self, host: str, device_type: str):
        self.message = f"Invalid authentication error for ${host}, ${device_type}"
        super(InvalidAuthentication, self).__init__(self.message)
