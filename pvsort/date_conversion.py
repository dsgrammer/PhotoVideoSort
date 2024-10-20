from datetime import datetime

class DateProcessing():
    def __init__(self) -> None:
        pass

    def dateConversion(timestamp) -> datetime:
	    return datetime.utcfromtimestamp(timestamp).strftime('%Y%m%d_%H%M%S')