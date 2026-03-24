from main import calculate_order_total, Product

# test carrello vuoto
def test_empty_cart():
	assert calculate_order_total([], "SAVE10", False) == 0
	assert calculate_order_total(None, "SAVE10", False) == 0


# test ordine normale CON coupon (con e senza VIP)
def test_coupon_no_vip():
	assert calculate_order_total([
		Product("Scarpe", 25.0, 4),
		Product("Sciarpa", 10.0, 3)
	], "SAVE10", False) == 120

def test_coupon_vip():
	assert calculate_order_total([
		Product("Scarpe", 25.0, 1),
		Product("Sciarpa", 10.0, 1)
	], "SAVE10", True) == 37


# test ordine normale SENZA coupon (con e senza VIP)
def test_no_coupon_vip():
	assert calculate_order_total([
		Product("Scarpe", 25.0, 3),
		Product("Sciarpa", 10.0, 1)
	], "", True) == 85

def test_no_coupon_no_vip():
	assert calculate_order_total([
		Product("Scarpe", 25.0, 3),
		Product("Sciarpa", 10.0, 1)
	], "", False) == 85


# test appositamente con calcolo errato
def test_no_coupon_no_vip_err():
	assert calculate_order_total([
		Product("Scarpe", 25.0, 1),
		Product("Sciarpa", 10.0, 1)
	], "", False) == 35


# test per verificare che ad esattamente 100 euro venga applicato lo sconto del coupon
def test_coupon_exactly_100():
    assert calculate_order_total([
        Product("Giacca", 50.0, 2)
    ], "SAVE10", False) == 90.0

def test_just_below_100():
    assert calculate_order_total([
        Product("Borsa2", 99.9, 1)
    ], "SAVE10", False) == 99.9


# test per verificare che lo sconto venga applicato SOLO all'inserimento del coupon corretto
def test_invalid_coupon():
    assert calculate_order_total([
        Product("Jeans", 60.0, 2)
    ], "WRONG_CODE", False) == 120.0


# test per verificare la corretta applicazione dei costi di spedizione
def test_shipping_exactly_50():
    assert calculate_order_total([
        Product("Scarpe", 25.0, 2)
    ], "", False) == 50.0

def test_shipping_just_below_50_vip():
    assert calculate_order_total([
        Product("Borsa", 49.9, 1)
    ], "", True) == 51.9

def test_shipping_just_below_50_no_vip():
    assert calculate_order_total([
        Product("Borsa", 49.9, 1)
    ], "", False) == 54.9