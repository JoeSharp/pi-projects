from typing import Dict, List, TypeVar

# Here is an existing site we can test against
# https://morsecode.world/international/translator.html

DOT: int = 0
DASH: int = 1
LETTER_GAP: int = 2
WORD_GAP: int = 3

Morse = TypeVar('Morse', bound=List[int])

MorseCodesByInput: Dict[chr, Morse] = {
    'a': [DOT, DASH],
    'b': [DASH, DOT, DOT, DOT],
    'c': [DASH, DOT, DASH, DOT],
    'd': [DASH, DOT, DOT],
    'e': [DOT],
    'f': [DOT, DOT, DASH, DOT],
    'g': [DASH, DASH, DOT],
    'h': [DOT, DOT, DOT, DOT],
    'i': [DOT, DOT],
    'j': [DOT, DASH, DASH, DASH],
    'k': [DASH, DOT, DASH],
    'l': [DOT, DASH, DOT, DOT],
    'm': [DASH, DASH],
    'n': [DASH, DOT],
    'o': [DASH, DASH, DASH],
    'p': [DOT, DASH, DASH, DOT],
    'q': [DASH, DASH, DOT, DASH],
    'r': [DOT, DASH, DOT],
    's': [DOT, DOT, DOT],
    't': [DASH],
    'u': [DOT, DOT, DASH],
    'v': [DOT, DOT, DOT, DASH],
    'w': [DOT, DASH, DASH],
    'x': [DASH, DOT, DOT, DASH],
    'y': [DASH, DOT, DASH, DASH],
    'z': [DASH, DASH, DOT, DOT],
    '1': [DOT, DASH, DASH, DASH, DASH],
    '2': [DOT, DOT, DASH, DASH, DASH],
    '3': [DOT, DOT, DOT, DASH, DASH],
    '4': [DOT, DOT, DOT, DOT, DASH],
    '5': [DOT, DOT, DOT, DOT, DOT],
    '6': [DASH, DOT, DOT, DOT, DOT],
    '7': [DASH, DASH, DOT, DOT, DOT],
    '8': [DASH, DASH, DASH, DOT, DOT],
    '9': [DASH, DASH, DASH, DASH, DOT],
    '0': [DASH, DASH, DASH, DASH, DASH],
}

InputsByMorseCode: Dict[str, chr] = {str(value): key for (key, value) in MorseCodesByInput.items()}


def to_morse_raw(message: str) -> Morse:
    morse: Morse = []

    for m in message:
        if m == ' ':
            morse.append(WORD_GAP)
        else:
            code = MorseCodesByInput[m.lower()]

            for c in code:
                morse.append(c)
            morse.append(LETTER_GAP)

    return morse


def to_morse_str(message: str) -> str:
    morse: Morse = to_morse_raw(message)

    def get_char(c: int) -> str:
        if c == WORD_GAP:
            return ' / '
        elif c == LETTER_GAP:
            return ' '
        elif c == DOT:
            return '.'
        elif c == DASH:
            return '-'

        return ''

    return "".join([get_char(m) for m in morse])


def from_morse(morse: Morse) -> str:
    def handle_accum(acc: Morse, msg: List[chr]):
        if len(acc) > 0:
            plain_text: chr = InputsByMorseCode[str(acc)]
            if plain_text is not None:
                msg.append(plain_text)
            acc.clear()

    message: List[chr] = []
    accumulated: Morse = []

    for c in morse:
        if c == WORD_GAP or c == LETTER_GAP:
            handle_accum(accumulated, message)

            if c == WORD_GAP:
                message.append(' ')

        else:
            accumulated.append(c)

    handle_accum(accumulated, message)

    return "".join(message)

