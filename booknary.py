class Booknary():

    def __init__(self, dict_attributes):
        self.attributes = self.compressAllToList(dict_attributes)

    def compressAllToList(self, param):
        dict_list = []

        dict_list.append(param)

        return dict_list

    def has(self, argument):
        for iten in self.attributes:
            if argument in iten:
                return True

        return False

    def get(self, argument):
        if not self.has(argument):
            return False

        for iten in self.attributes:
            return iten[argument]
