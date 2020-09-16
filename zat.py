#!/usr/bin/env python3

import os
import ast
import sys
import psutil

state_path = os.path.expanduser("~/.zat")

def load_state():
	if os.path.exists(state_path):
		with open(state_path, 'r') as f:
			return ast.literal_eval(f.read())
	return {}

def save_state(state):
	with open(state_path, 'w') as f:
		f.write(repr(state))

if len(sys.argv) <= 1:
	print("Zat'nik'tel (zat)")
	print("Suspends, kills, and disintegrates commands.")
	print("")
	print("Usage:")
	print("zat <pid>")

for arg in sys.argv[1:]:
	pid = int(arg)
	pids = psutil.pids()

	if pid in pids:
		process = psutil.Process(pid)
		status = process.status()

		if status != 'stopped':
			# first shot, suspend the process
			print(f"suspending {pid} {process.name()}")
			process.suspend()
		else:
			# back up the exe path so we can disintegrate it later
			state = load_state()
			state[pid] = process.exe()
			save_state(state)

			# second shot, kill the process
			print(f"killing {pid} {process.name()}")
			process.kill()
	else:
		state = load_state()
		if pid in state.keys():
			# third shot, completely disintegrate the command
			print(f"disintegrating {state[pid]}")
			os.remove(state[pid])
			state.pop(pid, None)
			save_state(state)
		else:
			print(f"process {pid} doesn't exist, and hasn't been zat'd before either")
