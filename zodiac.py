import misc

class zodiac_keys:
    western = {
        1: ["January 20 - February 16"],
        2: ["February 16 - March 11"],
        3: ["March 11 - April 18"],
        4: ["April 18 - May 13"],
        5: ["May 13 - June 21"],
        6: ["June 21- July 20"],
        7: ["July 20 - August 10"],
        8: ["August 10 - September 16"],
        9: ["September 16 - October 30"],
        10: ["October 30 - November 23"],
        11: ["November 23 - 29"],
        12: ["November 29 - December 17"],
        13: ["December 17 - January 20"],
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

    def hindu(self):
        pass

    def chinese(self):
        pass

    def egyptian(self):
        pass

    def celtic(self):
        pass