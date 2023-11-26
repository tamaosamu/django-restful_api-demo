class Utils:
    
    @staticmethod
    def to_dict(params) -> dict[str: any]:
        dict = {}
        for item in params:
            dict[item[0]] = item[1]
        return dict
    
    @staticmethod
    def tuple_to_map(params: tuple) -> dict:
        dict = {}
        for item in params:
            key, value = item
            dict[key] = value
        return dict