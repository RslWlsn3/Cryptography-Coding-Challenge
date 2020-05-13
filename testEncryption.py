import unittest
import Encryption

class TestSum(unittest.TestCase):
    
    # Encode tests from part 2
    def test1(self):
        self.assertEqual(Encryption.encode("tacocat"), [267487694, 125043731])

    def test2(self):
        self.assertEqual(Encryption.encode("never odd or even"),
        [267657050, 233917524, 234374596, 250875466, 17830160])

    def test3(self):
        self.assertEqual(Encryption.encode("lager, sir, is regal"),
        [267394382, 167322264, 66212897, 200937635, 267422503])

    def test4(self):
        self.assertEqual(Encryption.encode("go hang a salami, I'm a lasagna hog"),
        [200319795, 133178981, 234094669, 267441422, 78666124, 99619077,
         267653454, 133178165, 124794470])    

    def test5(self):
        self.assertEqual(Encryption.encode("egad, a base tone denotes a bad age"),
        [267389735, 82841860, 267651166, 250793668, 233835785, 267665210,
         99680277, 133170194, 124782119])
  
    # Encode tests from part 1
    def test6(self):
        self.assertEqual(Encryption.encode("foo"), [124807030])

    def test7(self):
        self.assertEqual(Encryption.encode(" foo"), [250662636])

    def test8(self):
        self.assertEqual(Encryption.encode("foot"), [267939702])

    def test9(self):
        self.assertEqual(Encryption.encode("BIRD" ), [251930706])

    def test10(self):
        self.assertEqual(Encryption.encode("...." ), [15794160])

    def test11(self):
        self.assertEqual(Encryption.encode("^^^^" ), [252706800])

    def test12(self):
        self.assertEqual(Encryption.encode("Woot" ), [266956663])

    def test13(self):
        self.assertEqual(Encryption.encode("no" ), [53490482])
    
    #Decode tests from part 2 
    def test14(self):
        self.assertEqual(Encryption.decode([267487694, 125043731]), "tacocat")

    def test15(self):
        self.assertEqual(Encryption.decode([267657050, 233917524, 234374596, 250875466,
         17830160]), "never odd or even")    

    def test16(self):       
        self.assertEqual(Encryption.decode([267394382, 167322264, 66212897, 200937635,
         267422503]), "lager, sir, is regal")

    def test17(self):
        self.assertEqual(Encryption.decode([200319795, 133178981, 234094669, 267441422,
         78666124, 99619077, 267653454, 133178165, 124794470]), 
         "go hang a salami, I'm a lasagna hog")

    def test18(self):
        self.assertEqual(Encryption.decode([267389735, 82841860, 267651166, 250793668,
         233835785, 267665210, 99680277, 133170194, 124782119]), 
         "egad, a base tone denotes a bad age")
    
    #Decode tests form part 1
    def test19(self):
        self.assertEqual(Encryption.decode([124807030]), "foo")

    def test20(self):
        self.assertEqual(Encryption.decode([250662636]), " foo")

    def test21(self):
        self.assertEqual(Encryption.decode([267939702]), "foot")

    def test22(self):
        self.assertEqual(Encryption.decode([251930706]), "BIRD")

    def test23(self):
        self.assertEqual(Encryption.decode([15794160]), "....")

    def test24(self):
        self.assertEqual(Encryption.decode([252706800]), "^^^^")

    def test25(self):
        self.assertEqual(Encryption.decode([266956663]), "Woot")

    def test26(self):
        self.assertEqual(Encryption.decode([53490482]), "no")
    
    # Test ability to assert s == decode(encode(s))
    def test27(self):
        self.assertEqual(Encryption.decode(Encryption.encode("tacocat")) , "tacocat")

    def test28(self):
        self.assertEqual(Encryption.decode(Encryption.encode("never odd or even")),
         "never odd or even")

    def test29(self):
        self.assertEqual(Encryption.decode(Encryption.encode("lager, sir, is regal")),
         "lager, sir, is regal")

    def test30(self):
        self.assertEqual(Encryption.decode(Encryption.encode("go hang a salami, I'm a lasagna hog")),
         "go hang a salami, I'm a lasagna hog")

    def test31(self):
        self.assertEqual(Encryption.decode(Encryption.encode("egad, a base tone denotes a bad age"))
        , "egad, a base tone denotes a bad age")

    def test32(self):
        self.assertEqual(Encryption.decode(Encryption.encode("foo")) , "foo")

    def test33(self):
        self.assertEqual(Encryption.decode(Encryption.encode(" foo")) , " foo")

    def test34(self):
        self.assertEqual(Encryption.decode(Encryption.encode("foot")) , "foot")

    def test35(self):
        self.assertEqual(Encryption.decode(Encryption.encode("BIRD")) , "BIRD")

    def test36(self):
        self.assertEqual(Encryption.decode(Encryption.encode("....")) , "....")

    def test37(self):
        self.assertEqual(Encryption.decode(Encryption.encode("^^^^")) , "^^^^")

    def test38(self):
        self.assertEqual(Encryption.decode(Encryption.encode("Woot")) , "Woot")
        
    def test39(self):
        self.assertEqual(Encryption.decode(Encryption.encode("no")) , "no")

    


if __name__ == '__main__':
    unittest.main()