def set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status):
  if (parameter_value < min):
    breach_status = "Warning"
    range_status = "Approaching discharge"
    
  elif(parameter_value > max):
    breach_status = "Warning"
    range_status = "Approaching charge-peak"
  return [breach_status, range_status]
  
def get_warning(parameter_value, parameter_name, min, max, key, breach_status, range_status):
  if not key:
    return
  parameter_value_tolerance = (parameter_value*5)/100
  min = min + parameter_value_tolerance
  max = max - parameter_value_tolerance
  if not (min<parameter_value<max):
    return set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status)
  
    
  

def check_parameter_range(parameter_value, parameter_name, min, max, key):
  breach_status = "Normal"
  range_status = "is in range"
  
  if (parameter_value < min):
    breach_status = "Low"
    range_status = "is out of range"
    
  elif(parameter_value > max):
    breach_status = "High"
    range_status = "is out of range"  
  status = get_warning(parameter_value, parameter_name, min, max, key, breach_status, range_status)
  breach_status = status[0]
  range_status = status[1]
  print(parameter_name+" "+range_status+", the value is at "+breach_status)
  
  return(min<parameter_value<max)
  
def battery_is_ok(temperature, soc, charge_rate):
  parameter_warning = {temperature:1, soc:1, charge_rate:1}
  return check_parameter_range(temperature,"Temperature",0,45,parameter_warning[temperature]) and check_parameter_range(soc,"SOC",20,80, parameter_warning[soc]) and check_parameter_range(charge_rate,"charge_rate",0,0.8, parameter_warning[charge_rate])
 

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(40, 80, 0.6) is False)
  assert(battery_is_ok(30, 60, 0.8) is False)
  assert(battery_is_ok(90,85, 0.9) is False)
  assert(battery_is_ok(-2,18,-1) is False)
