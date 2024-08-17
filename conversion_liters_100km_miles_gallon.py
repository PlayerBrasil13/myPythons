# 1 milha americana = 1609,344 metros;
# 1 galão americano = 3,785411784 litros.

def liters_100km_to_miles_gallon(liters):
    l_km = liters / 100
    km_l = 1 / l_km
    m_l = km_l / 1.609344
    m_g = m_l * 3.785411784
    return m_g

def miles_gallon_to_liters_100km(miles):
    g_m = 1 / miles
    l_m = g_m * 3.785411784
    l_km = l_m / 1.609344
    l_100km = l_km * 100
    return l_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
