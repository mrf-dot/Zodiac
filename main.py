# A simple program to calculate your zodiac symbol.
from colorama import init
from termcolor import cprint
import zodiac

init()

def main():
    print("""What zodiac system would you like to use?
        Western
        Hindu
        Chinese
        Egyptian
        Celtic
        """)
    while True:
        system = input("Enter the name of the system: ").lower()
        default = lambda: cprint(f"\"{system}\" is not a valid command.", "red"
                                 )
        astrology = zodiac.astrology_systems()
        getattr(astrology, system, lambda: default())()


if __name__ == "__main__":
    main()
"""Astrological signs
Capricorn: January 20 - February 16

Aquarius: February 16 - March 11

Pisces: March 11 - April 18

Aries: April 18 - May 13

Taurus: May 13 - June 21

Gemini: June 21- July 20

Cancer: July 20 - August 10

Leo: August 10 - September 16

Virgo: September 16 - October 30

Libra: October 30 - November 23

Scorpio: November 23 - 29

Ophiuchus: November 29 - December 17

Sagittarius: December 17 - January 20
"""
