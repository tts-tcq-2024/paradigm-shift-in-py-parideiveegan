"""def check_parameter_breach(parameter_value, parameter_name, min, max):
  breach_status = "Normal
  range_status = "is in range"
  if (parameter_value < min):
    breach_status = "Low"
    range_status = "is out of range"
  elif(parameter_value > max):
    breach_status = "High"
    range_status = "is out of range"
  printf(parameter_name+" "+range_status+", the value is "+breach_status)"""
  
def check_parameter_range(parameter_value, parameter_name, min, max):
  breach_status = "Normal
  range_status = "is in range"
  if (parameter_value < min):
    breach_status = "Low"
    range_status = "is out of range"
  elif(parameter_value > max):
    breach_status = "High"
    range_status = "is out of range"
  printf(parameter_name+" "+range_status+", the value is "+breach_status)
  #check_parameter_breach(parameter_value, parameter_name, min, max)
  return(min<parameter_value<max)
  
def battery_is_ok(temperature, soc, charge_rate):  
  return check_parameter_range(temperature,"Temperature",0,45) and check_parameter_range(soc,"SOC",20,80) and check_parameter_range(charge_rate,"charge_rate",0,0.8)
 

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(40, 80, 0.6) is False)
  assert(battery_is_ok(30, 60, 0.8) is False)
