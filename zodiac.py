import misc

class zodiac_keys:
    western = {
        1: ["January 20 - February 16", "Capricorn"],
        2: ["February 16 - March 11", "Aquarius"],
        3: ["March 11 - April 18", "Pisces"],
        4: ["April 18 - May 13", "Aries"],
        5: ["May 13 - June 21", "Taurus"],
        6: ["June 21- July 20", "Gemini"],
        7: ["July 20 - August 10", "Cancer"],
        8: ["August 10 - September 16", "Leo"],
        9: ["September 16 - October 30", "Virgo"],
        10: ["October 30 - November 23", "Libra"],
        11: ["November 23 - 29", "Scorpio"],
        12: ["November 29 - December 17", "Ophiuchus"],
        13: ["December 17 - January 20", "Sagittarius"],
    }
    hindu = {} 
    chinese = {}
    egyptian = {}
    celtic = {}


class astrology_systems:
    """Calculates astrological symbols based off preferred system

    """
    def western(self):
        misc.table_dict("Input", "When you were born",zodiac_keys.western)
        selection = misc.to_int("When were you born (Input): ", *range(1,14))
        misc.fetch_sign(selection, zodiac_keys.western)

    def hindu(self):
        pass

    def chinese(self):
        pass

    def egyptian(self):
        pass

    def celtic(self):
        pass