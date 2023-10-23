#!/usr/bin/env python
import time
from panda import Panda

if __name__ == "__main__":
  panda_serials = Panda.list()
  pandas = [Panda(serial=ps) for ps in panda_serials]
  if not pandas:
    print("No pandas connected")
    assert False

  while True:
    for panda in pandas:
      print(panda.health())
    print("\n")
    time.sleep(0.5)

