from chateaubriand.app.views import BaseView


class PersonalAssignmentView(BaseView):
    def __init__(self, class_):
        self.class_ = class_

    def get_data(self):
        # query
        pass

    def get_view(self):
        get_data()
        return dict()