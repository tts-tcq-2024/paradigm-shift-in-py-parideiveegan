def set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status, tolerance):
  if (min < parameter_value < min+tolerance):
    breach_status = "Warning"
    range_status = "Approaching discharge"
    
  elif(max-tolerance < parameter_value < max):
    breach_status = "Warning"
    range_status = "Approaching charge-peak"
  return [breach_status, range_status]
  
def get_warning(parameter_value, parameter_name, min, max, key, breach_status, range_status):
  if not key:
    return [breach_status, range_status]
  tolerance = (parameter_value*5)/100
  if not (min+tolerance < parameter_value < max-tolerance):
    return set_warning_status(parameter_value, parameter_name, min, max,breach_status, range_status, tolerance)
  return [breach_status, range_status]
