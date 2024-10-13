def set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status):
  if (parameter_value <= min):
    breach_status = "Warning"
    range_status = "Approaching discharge"
    
  elif(parameter_value >= max):
    breach_status = "Warning"
    range_status = "Approaching charge-peak"
  return [breach_status, range_status]
  
def get_warning(parameter_value, parameter_name, min, max, key, breach_status, range_status):
  if not key:
    return [breach_status, range_status]
  parameter_value_tolerance = (parameter_value*5)/100
  min = min + parameter_value_tolerance
  max = max - parameter_value_tolerance
  if not (min<parameter_value<max):
    return set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status)
  return [breach_status, range_status]
