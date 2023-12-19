import my_discount

def test_to_see_if_get_my_discount():
	assert my_discount.my_discount([15, 150]) == [127.5]

	