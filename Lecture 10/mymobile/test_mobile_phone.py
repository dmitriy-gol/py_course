from modile_phone_class import Phone


iphone = Phone("12345")

def test_turn_on():
    iphone.turn_on()
    assert iphone.turn_on() == 'mobile phone 12345 is enabled'


def test_turn_off():
    iphone.turn_off()
    assert iphone.turn_off() == 'mobile phone 12345 is turned off'


def test_call_if_on():
    iphone.turn_on()
    assert iphone.call('12345') == 'calling 12345'


def test_call_if_off():
    iphone.turn_off()
    assert iphone.call('12345') == 'mobile phone 12345 is turned off'
