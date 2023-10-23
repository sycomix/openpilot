import os
from nose.tools import nottest

def phone_only(x):
  return x if os.path.isfile("/init.qcom.rc") else nottest(x)

