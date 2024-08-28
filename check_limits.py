def check_temperature(temperature):
  return (0< temperature <45)
def check_soc(soc):
  return (20< soc < 80)
def check_chargeRate(charge_rate):
  return (charge_rate < 0.8)
def battery_is_ok(temperature, soc, charge_rate):
  return check_temperature(temperature) and check_soc(soc) and check_chargeRate(charge_rate)
 
  
  

'''  
if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  elif soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  elif charge_rate > 0.8:
    print('Charge rate is out of range !')
    return False 
'''
  


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
