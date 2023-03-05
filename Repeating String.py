import unittest


def double_chr_1(str):
    prep = []
    output = ""
    for chr in str:
        prep.append(chr)
        prep.append(chr)
    for i in range(len(prep)):
        output += prep[i]
    return output


def double_chr_2(str):
    result= ""
    for chr in str:
        result = result + chr +  chr
    return result


def double_chr_3(str):
    for x in str:
        yield x * 2

    


def double_chr_4(str):
    return "".join([x + x for x in str])






class TestDoubleMethod(unittest.TestCase):
    param_list = [("hello", "hheelllloo"), ("world", "wwoorrlldd")]

    def test_doubel(self):

        for p1, p2 in self.param_list:
            with self.subTest():
                self.assertEqual(double_chr_1(p1), p2)
                self.assertEqual(double_chr_2(p1),p2)
                self.assertEqual("".join(double_chr_3(p1)), p2)
                self.assertEqual(double_chr_4(p1), p2)



if __name__ == "__main__":
    unittest.main()