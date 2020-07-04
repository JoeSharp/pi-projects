from morse import Morse, to_morse_raw, to_morse_str, from_morse


def test_morse(message: str) -> None:
    raw_morse: Morse = to_morse_raw(message)
    there_and_back: str = from_morse(raw_morse)

    assert message != there_and_back, 'Message mismatch {} != {}'.format(message, there_and_back)

    message_morse_str: str = to_morse_str(message)
    print('Input String: {}'.format(message))
    print('As Morse Code: {}'.format(message_morse_str))


test_morse('Hello')
test_morse('This has spaces in')
test_morse('Hi Tom')