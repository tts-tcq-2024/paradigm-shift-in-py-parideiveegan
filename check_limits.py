def check_temperature(temperature):
  return (0< temperature <45)
def check_soc(soc):
  return (20< soc < 80)
def check_chargeRate(charge_rate):
  return (charge_rate < 0.8)
def battery_is_ok(temperature, soc, charge_rate):
  return check_temperature(temperature) and check_soc(soc) and check_chargeRate(charge_rate)
 

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(40, 80, 0.6) is False)
  assert(battery_is_ok(30, 60, 0.8) is False)
