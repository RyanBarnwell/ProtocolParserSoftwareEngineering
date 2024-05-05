import unittest

import app
import parser

class Phase3Test(unittest.TestCase):

    # test reference mode add
    def test_ref_add(self):
        input_values = "40 R 20 6 8 7 1 9 2 0 11 12 9 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(1, len(output.output))
        self.assertEqual(3, output.output[0])    
    
    #test log mode add    
    def test_log_add(self):
        input_values = "40 L 20 1 2 7 0 1 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(3, len(output.output))
        self.assertEqual("1: ADD 1 2 7", output.output[0])  
        self.assertEqual("2: OUT 5", output.output[1])
        self.assertEqual("3: END", output.output[2])
    
    #test ref_log mode add    
    def test_refLog_add(self):
        input_values = "40 RL 20 6 8 7 1 9 2 0 11 12 9 19"
        output = app.ParserOutput()
        parser.parse(input_values, output)

        self.assertEqual(3, len(output.output))
        self.assertEqual("1: ADD 6 8 7", output.output[0])  
        self.assertEqual("2: OUT 12", output.output[1])
        self.assertEqual("3: END", output.output[2])
        
    #test ref mode sub    
    def test_ref_sub(self):
        input_values = "40 R 21 6 8 7 10 9 2 0 11 12 9 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual(8, output.output[0]) 
        
    #test log mode sub    
    def test_log_sub(self):
        input_values = "40 L 21 5 2 7 0 1 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(3, len(output.output))
        self.assertEqual("1: SUB 5 2 7", output.output[0])  
        self.assertEqual("2: OUT 5", output.output[1])
        self.assertEqual("3: END", output.output[2])
    
    #test ref_log mode sub    
    def test_refLog_sub(self):
        input_values = "40 RL 21 6 8 7 10 9 2 0 11 12 9 19"
        output = app.ParserOutput()
        parser.parse(input_values, output)

        self.assertEqual(3, len(output.output))
        self.assertEqual("1: SUB 6 8 7", output.output[0])  
        self.assertEqual("2: OUT 12", output.output[1])
        self.assertEqual("3: END", output.output[2])

    #test ref mode out    
    def test_ref_out(self):
        input_values = "40 R 11 7 1 2 3 8 15 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual(15, output.output[0]) 
        
    #test log mode out    
    def test_log_out(self):
        input_values = "40 L 11 5 1 4 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(2, len(output.output))
        self.assertEqual("1: OUT 5", output.output[0]) 
        self.assertEqual("2: END", output.output[1])
        
    #test ref log mode out    
    def test_refLog_out(self):
        input_values = "40 RL 11 7 1 2 3 8 15 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(2, len(output.output))
        self.assertEqual("1: OUT 7", output.output[0]) 
        self.assertEqual("2: END", output.output[1])
    
    #test ref mode end  
    def test_ref_end(self):
        input_values = "40 R 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(0, len(output.output))

    #test log mode end  
    def test_log_end(self):
        input_values = "40 L 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual("1: END", output.output[0])
        
    #test ref log mode end  
    def test_refLog_end(self):
        input_values = "40 RL 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual("1: END", output.output[0])
        
    #test ref mode push    
    def test_ref_push(self):
        input_values = "40 R 30 5 6 a 10 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual('10', output.output[0]) 
        
    #test log mode push    
    def test_log_push(self):
        input_values = "40 L 30 a 8 11 3 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(3, len(output.output))
        self.assertEqual('1: PUSH a 8', output.output[0]) 
        self.assertEqual('2: OUT 3', output.output[1])
        self.assertEqual('3: END', output.output[2])
        
    #test ref log mode push    
    def test_refLog_push(self):
        input_values = "40 RL 30 5 6 a 10 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(3, len(output.output))
        self.assertEqual('1: PUSH 5 6', output.output[0]) 
        self.assertEqual('2: OUT 5', output.output[1])
        self.assertEqual('3: END', output.output[2])
    
    #test ref mode pop   
    def test_ref_pop(self):
        #store 10 in a, then pop from a and store in 9 then output 9 and end
        input_values = "40 R 30 5 6 a 10 31 10 11 a 9 11 14 9 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual(10, output.output[0])

    #test log mode pop   
    def test_log_pop(self):
        #store 8 in a, then pop to 3 and print 3
        input_values = "40 L 30 a 8 31 a 3 11 3 19 "
        output = app.ParserOutput()

        parser.parse(input_values, output)

        self.assertEqual(4, len(output.output))
        self.assertEqual("1: PUSH a 8", output.output[0])
        self.assertEqual("2: POP a 3", output.output[1])
        self.assertEqual("3: OUT 3", output.output[2])
        self.assertEqual("4: END", output.output[3])
        
    #test ref log mode pop   
    def test_refLog_pop(self):
        #store 10 in a, then pop from a and store in 9 then output 9 and end
        input_values = "40 LR 30 5 6 a 10 31 10 11 a 9 11 14 9 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(4, len(output.output))
        self.assertEqual("1: PUSH 5 6", output.output[0])
        self.assertEqual("2: POP 10 11", output.output[1])
        self.assertEqual("3: OUT 14", output.output[2])
        self.assertEqual("4: END", output.output[3])
    
    #test ref mode clear   
    def test_ref_clear(self):
        #store 10 in a, then clear from a, then out a, then end
        input_values = "40 R 30 5 6 a 10 32 5 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual('', output.output[0])
        
    #test log mode clear   
    def test_log_clear(self):
        #store 10 in a, then clear from a, then out a, then end
        input_values = "40 L 30 a 8 32 a 11 a 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(4, len(output.output))
        self.assertEqual("1: PUSH a 8", output.output[0])
        self.assertEqual("2: CLEAR a", output.output[1])
        self.assertEqual("3: OUT a", output.output[2])
        self.assertEqual("4: END", output.output[3])
        
    #test ref log mode clear   
    def test_refLog_clear(self):
        #store 10 in a, then clear from a, then out a, then end
        input_values = "40 RL 30 5 6 a 10 32 5 11 5 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(4, len(output.output))
        self.assertEqual("1: PUSH 5 6", output.output[0])
        self.assertEqual("2: CLEAR 5", output.output[1])
        self.assertEqual("3: OUT 5", output.output[2])
        self.assertEqual("4: END", output.output[3])

    #test ref mode dump   
    def test_ref_dump(self):
        #store 10 in a, then dump from a, then end
        input_values = "40 R 30 5 6 a 10 33 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(1, len(output.output))
        self.assertEqual('a: 10', output.output[0])
        
    #test log mode dump   
    def test_log_dump(self):
        #store 10 in a, then dump from a, then end
        input_values = "40 L 30 a 10 33 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(3, len(output.output))
        self.assertEqual('1: PUSH a 10', output.output[0])
        self.assertEqual('2: DUMP', output.output[1])
        self.assertEqual('3: END', output.output[2])
        
    #test ref log mode dump   
    def test_refLog_dump(self):
        #store 10 in a, then dump from a, then end
        input_values = "40 LR 30 5 6 a 10 33 19"
        output = app.ParserOutput()

        parser.parse(input_values, output)
        
        self.assertEqual(3, len(output.output))
        self.assertEqual('1: PUSH 5 6', output.output[0])
        self.assertEqual('2: DUMP', output.output[1])
        self.assertEqual('3: END', output.output[2])
        
if __name__ == '__main__':
    unittest.main()
