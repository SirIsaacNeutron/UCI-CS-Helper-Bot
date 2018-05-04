

import unittest
from uci_cs_helper import text_about_switching_to_cs as text

class TestBot(unittest.TestCase):
    """Note: these tests are based off real texts and posts from
    /r/UCI.
    """
    def test_detecting_texts_true(self):
        """Test the bot's ability to detect text that is
        legitimately about switiching into CS from another major.
        """
        self.assertTrue(text("Hello everyone. I'm a freshman at UCI and was admitted as Undecided/Undeclared but I really want to switch to Computer Science. Thing is, I need to take ICS 31 before I can change into that major. All classes are full and I can't really do much other than wait and hope people drop their classes. What can I do in case I'm unable to join this semester? Can I take it next semester? Summer school? Or do I have to wait until next year?"))
        
        self.assertTrue(text("Hi, I was admitted into uci but as an undeclared. I tried to switch into the computer science major right away but couldn't. Now I want to know if it is still even possible to switch into the computer science major and if so what are my chances of getting into the major?"))

        self.assertTrue(text("Hey guys I’ll be attending UCI in the fall and I got in for mech e, although I want to switch into the computer science major. Does anyone know if this is possible? Or how hard it is to do this?"))

        self.assertTrue(text("Howt difficult is it to switch into computer science major as undeclared?"))

        self.assertTrue(text("Current Undecided/Undeclared trying to change into Computer Science"))

        self.assertTrue(text("I got admitted to UC Irvine as a freshman to my second choice major. I plan to switch to decided and then to CS."))
        
        self.assertTrue(text("How Hard Is It To Transfer To Computer Science Major?"))

    def test_detecting_texts_false(self) -> None:
        """Test the bot to make sure it does not reply to text
        that is not about switiching to CS from another major.
        """
        self.assertFalse(text("Just got approved to switch to u/u earlier today. To those who were/currently are in u/u, what was the experience like? What do you think about the counselors? Just curious."))

        self.assertFalse(text("Is it hard switching from Undeclared to Cognitive Science?"))
        
        self.assertFalse(text("I want to go into kinesiology for grad school. I am currently a Bio sci major, but should I switch into public health?"))

        self.assertFalse(text("Should reply to comment: I was in your position, just switch out of the major and you'll be fine. Eventhough they say you may not be able to its not true - I was able to switch out of ICS into international studies / soc sci"))
        
        self.assertFalse(text("I knew someone who was fed up with the parties/drinking environment at UCSB and transfered to another UC succesfully but I don't know the process she went through, so it is possible."))

        self.assertFalse(text("Hi everyone. I’m a transfer student from SD and I’m trying to decide between uci and csuf for sociology. I get a pretty good financial aid package so cost isn’t really that big of a deal for me. Any Soc majors on this sub that can share their experience with the program? Thanks :)"))

        self.assertFalse(text("So I transferred here as a 3rd year CS major but then I had to switch to U/U because of Academic Probation."))

        self.assertFalse(text("I'm an incoming UCI transfer and have to take a lot of CS lower-division classes due to them not being articulated. I still have to do placement exams but, wanted to know what classes are usually available during the summer. Would they have classes for my major CS, or is it usually just GE classes. I already planned which classes i'd have to take depending on what placement exams I pass but I didn't factor in taking summer classes, which I hope will help speed up the process. Any feedback would be appreciated!"))

if __name__ == '__main__':
    unittest.main()



