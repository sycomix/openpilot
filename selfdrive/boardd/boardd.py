# pylint: skip-file
import os
import subprocess

# Cython
boardd_api_dir = os.path.dirname(os.path.abspath(__file__))
subprocess.check_call(["make", "boardd_api_impl.so"], cwd=boardd_api_dir)
from selfdrive.boardd.boardd_api_impl import can_list_to_can_capnp
assert can_list_to_can_capnp


def can_capnp_to_can_list(can, src_filter=None):
  return [(msg.address, msg.busTime, msg.dat, msg.src) for msg in can
          if src_filter is None or msg.src in src_filter]
