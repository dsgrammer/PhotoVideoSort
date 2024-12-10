from datetime import datetime

class DateProcessing():
    def __init__(self) -> None:
        pass

    def dateConversion(timestamp) -> datetime:
	    return datetime.fromtimestamp(timestamp).strftime('%Y%m%d_%H%M%S')