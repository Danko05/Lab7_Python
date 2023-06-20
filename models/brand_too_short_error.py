class BrandTooShortError(Exception):
    def __init__(self, message="Brand too short"):
        self.message = message
        super().__init__(self.message)
