Testing a regex

Use the .test() method
let testString = "My test string";
let testRegex = /string/;
testRegex.test(testString);
Testing multiple patterns

Use the OR operator (|)
const regex = /yes|no|maybe/;
Ignoring case

Use the i flag for case insensitivity
const caseInsensitiveRegex = /ignore case/i;
const testString = 'We use the i flag to iGnOrE CasE';
caseInsensitiveRegex.test(testString); // true
Extracting the first match to a variable

Use the .match() function
const match = "Hello World!".match(/hello/i); // "Hello"
Extracting all of the matches in an array

Use the g flag
const testString = "Repeat repeat rePeAT";
const regexWithAllMatches = /Repeat/gi;
testString.match(regexWithAllMatches); // ["Repeat", "repeat", "rePeAT"]
Matching any character

Use the wildcard character . to be a placeholder for any character
// To match "cat", "BAT", "fAT", "mat"
const regexWithWildcard = /.at/gi;
const testString = "cat BAT cupcake fAT mat dog";
const allMatchingWords = testString.match(regexWithWildcard); // ["cat", "BAT", "fAT", "mat"]
Matching a single character with multiple possibilities

Use character classes, which allow you to define a group of characters you wish to match
You place them inside square brackets []
// Match "cat" "fat" and "mat" but not "bat"
const regexWithCharClass = /[cfm]at/g;
const testString = "cat fat bat mat";
const allMatchingWords = testString.match(regexWithCharClass); // ["cat", "fat", "mat"]
Match letters of the alphabet

Use a range within the character set [a-z]
const regexWithCharRange = /[a-e]at/;
const catString = "cat";
const batString = "bat";
const fatString = "fat";

regexWithCharRange.test(catString); // true
regexWithCharRange.test(batString); // true
regexWithCharRange.test(fatString); // false
Match specific numbers and letters

You can also use the hyphen to match numbers
const regexWithLetterAndNumberRange = /[a-z0-9]/ig;
const testString = "Emma19382";
testString.match(regexWithLetterAndNumberRange) // true
Match a single, unknown character

To match a set of characters you don't want to have, use the negated character set
To negate a character set, use a caret ^
const allCharsNotVowels = /[^aeiou]/gi;
const allCharsNotVowelsOrNumbers = /[^aeiou0-9]/gi;
Match characters that occur one or more times in a row

Use the + symbol
const oneOrMoreAsRegex = /a+/gi;
const oneOrMoreSsRegex = /s+/gi;
const cityInFlorida = "Tallahassee";

cityInFlorida.match(oneOrMoreAsRegex); // ['a', 'a', 'a'];
cityInFlorida.match(oneOrMoreSsRegex); // ['ss'];
Matches characters that occur zero or more times in a row

Use the asterisk *
const zeroOrMoreOsRegex = /hi*/gi;
const normalHi = "hi";
const happyHi = "hiiiiii";
const twoHis = "hiihii";
const bye = "bye";

normalHi.match(zeroOrMoreOsRegex); // ["hi"]
happyHi.match(zeroOrMoreOsRegex); // ["hiiiiii"]
twoHis.match(zeroOrMoreOsRegex); // ["hii", "hii"]
bye.match(zeroOrMoreOsRegex); // null
Lazy Matching

The smallest part of a string that matches the given requirements
Regex, by default, are greedy (matches the longest portion of a string meeting the given requirements)
Use the ? character to lazy match
const testString = "catastrophe";
const greedyRexex = /c[a-z]*t/gi;
const lazyRegex = /c[a-z]*?t/gi;

testString.match(greedyRexex); // ["catast"]
testString.match(lazyRegex); // ["cat"]
Match starting string patterns

To test for a match of characters at the beginning of a string, use the caret ^, but outside of the character set
const emmaAtFrontOfString = "Emma likes cats a lot.";
const emmaNotAtFrontOfString = "The cats Emma likes are fluffy.";
const startingStringRegex = /^Emma/;

startingStringRegex.test(emmaAtFrontOfString); // true
startingStringRegex.test(emmaNotAtFrontOfString); // false
Match ending string patterns

Use the dollar sign $ at the end of a regex to check whether a pattern exists at the end of a string
const emmaAtBackOfString = "The cats do not like Emma";
const emmaNotAtBackOfString = "Emma loves the cats";
const startingStringRegex = /Emma$/;

startingStringRegex.test(emmaAtBackOfString); // true
startingStringRegex.test(emmaNotAtBackOfString); // false
Matching all letters and numbers

Use the \word shorthand
const longHand = /[A-Za-z0-9_]+/;
const shortHand = /\w+/;
const numbers = "42";
const myFavoriteColor = "magenta";

longHand.test(numbers); // true
shortHand.test(numbers); // true
longHand.test(myFavoriteColor); // true
shortHand.test(myFavoriteColor); // true
Match everything except letters & numbers

You can use for the opposite of \w with \W
const noAlphaNumericCharRegex = /\W/gi;
const weirdCharacters = "!_$!!";
const alphaNumericCharacters = "ab283AD";

noAlphaNumericCharRegex.test(weirdCharacters); // true
noAlphaNumericCharRegex.test(alphaNumericCharacters); // false

Match all numbers

You can use a character set [0-9], or use the shorthand \d
const digitsRegex = /\d/g;
const stringWithDigits = "My cat eats $20.00 worth of food a week.";

stringWithDigits.match(digitsRegex); // ["2", "0", "0", "0"]
Match all non-numbers

You can use the opposite of \d with \D
const nonDigitsRegex = /\D/g;
const stringWithLetters = "101 degrees";

stringWithLetters.match(nonDigitsRegex); // [" ", "d", "e", "g", "r", "e", "e", "s"]
Matching whitespace

Use \s to match white space and carriage returns
const sentenceWithWhitespace = "I like cats!"
var spaceRegex = /\s/g;
whiteSpace.match(sentenceWithWhitespace); // [" ", " "]
Matching non-whitespace

You can use the opposite of \s with \S
const sentenceWithWhitespace = "C a t"
const nonWhiteSpaceRegex = /\S/g;
sentenceWithWhitespace.match(nonWhiteSpaceRegex); // ["C", "a", "t"]
Matching character counts

You can specify a specific number of characters in a row using {lowerBound, upperBound}
const regularHi = "hi";
const mediocreHi = "hiii";
const superExcitedHey = "heeeeyyyyy!!!";
const excitedRegex = /hi{1,4}/;

excitedRegex.test(regularHi); // true
excitedRegex.test(mediocreHi); // true
excitedRegex.test(superExcitedHey); //false
Matching lowest number of character counts

You can define only a minimum number of character requirements with {lowerBound,}
This is called a quantity specifier
const regularHi = "hi";
const mediocreHi = "hiii";
const superExcitedHey = "heeeeyyyyy!!!";
const excitedRegex = /hi{2,}/;

excitedRegex.test(regularHi); // false
excitedRegex.test(mediocreHi); // true
excitedRegex.test(superExcitedHey); //false
Matching an exact number of character counts

You can specify the exact number of character requirements with {requiredCount}
const regularHi = "hi";
const bestHi = "hii";
const mediocreHi = "hiii";
const excitedRegex = /hi{2}/;

excitedRegex.test(regularHi); // false
excitedRegex.test(bestHi); // true
excitedRegex.test(mediocreHi); //false
Matching all or none of a character

To check whether a character exists, use the ?
const britishSpelling = "colour";
const americanSpelling = "Color";
const languageRegex = /colou?r/i;

languageRegex.test(britishSpelling); // true
languageRegex.test(americanSpelling); // true