import unittest


def remove_duplicates(in_list):

    if not len(in_list):
        raise Exception("in list can not be empty")
    out_list = []
    for i in in_list:
        if i not in out_list:
            out_list.append(i)
    return out_list


class RemoveDuplicatesTesting(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 1, 2, 4, 5, 1]), [1, 2, 3, 4, 5])

    def test_empty_in_list(self):
        self.assertRaises(Exception, remove_duplicates, [])


if __name__ == "__main__":
    unittest.main()