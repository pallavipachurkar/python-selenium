import softest


class Utils(softest.TestCase):
    def assertListItemText(self, list, value):
        for stop in list:
            print("The text is: " + stop.text)
            self.soft_assert(self.assertEquals,stop.text,value)
            if stop.text == value:
                print("assert pass")
            else:
                print("assert failed")
        self.assert_all()

