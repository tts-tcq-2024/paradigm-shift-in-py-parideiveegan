import unittest
from CheckBattetyParameterStatus import battery_is_ok
class CheckBattry(unittest.TestCase):
  def test_BatteryStatus(self):
    self.assert(battery_is_ok(25, 70, 0.7) is True)
    self.assert(battery_is_ok(50, 85, 0) is False)
    self.assert(battery_is_ok(40, 80, 0.6) is False)
    self.assert(battery_is_ok(30, 60, 0.8) is False)
    self.assert(battery_is_ok(90,85, 0.9) is False)
    self.assert(battery_is_ok(-2,18,-1) is False)
    self.assert(battery_is_ok(44 ,22 , 0.78) is True) # testcase for warning level

if __name__ == '__main__':
    unittest.main()
