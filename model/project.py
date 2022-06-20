class Project:
    def __init__(self, name=None, status=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return '%s' % self.name

    def __eq__(self, other):
        return self.name == other.name

    def name_sort(self):
        if self.name:
            return str(self.name)

