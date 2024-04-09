from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):
    # by defining the setup as a classmethod the class will be initiatied only once
    # @classmethod
    # def setUpClass(cls):
    #     cls.printer = Printer(pages_per_s=2.00, capacity=300)

    #new class initiated for each test
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)
    
    def test_print_within_capacity(self):
        
        self.printer.print(25)
        
        #Alternatively testing for the exact message: 
        # message = self.printer.print(25)
        # self.assertEqual(f"Printed 25 pages in 12.50 seconds.", message)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)
    
    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)

    def test_printer_speed(self):
        pages = 10
        expected = "Printed 10 pages in 5.00 seconds."

        result = self.printer.print(pages)
        self.assertEqual(result, expected)

    def test_speed_always_two_decimals(self):
        fast_printer = Printer(pages_per_s=3.0, capacity=300)
        pages = 11
        
        expected = "Printed 11 pages in 3.67 seconds."
        result = fast_printer.print(pages)

        self.assertEqual(result, expected)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)
    
    def test_multiple_runs_until_error(self):
        with self.assertRaises(PrinterError):
            self.printer.print(25)
            self.printer.print(50)
            self.printer.print(226)

