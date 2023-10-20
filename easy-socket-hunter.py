"""
  MIT License

  Copyright (c) 2023 CoffeeeAtNight

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""

import sys
import re
import socket

top10 = False

def main():
  check_args_length()
  check_for_flag()
  is_args_valid_ip4_addr()
  iter_ports_for_connection()
  sys.exit(0)

############################################################
  
def check_args_length():
  if (args_count := len(sys.argv)) > 3:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
  elif args_count < 2:
    print("You must specify the taget IP")
    print("For help use the -h flag")
    raise SystemExit(2)

def check_for_flag():
  if sys.argv[1] == "-h" or sys.argv[2] == "-h":
    print("Help")  # TODO PRINT HELP FOR SCRIPT
    sys.exit(0)
  if sys.argv[2] == "-s":
    top10 = True

def is_args_valid_ip4_addr():
  match = re.search(r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$", sys.argv[1])
  if not match:
    print("The first arugment is not a valid IPv4 address")
    raise SystemExit(2)
  
def exec_port_scan(port):
  try:
    socket.setdefaulttimeout(1)
    c = socket.socket()
    c.connect((sys.argv[1], port))
    print(f"Port {port} is open")
    c.close()
  except:
    print(f"Port {port} is closed")
    pass
  
def iter_ports_for_connection():
  if top10:
    for port in range(1, 10):
      exec_port_scan(port)
  else:
    for port in range(1, 65536):
      exec_port_scan(port)

if __name__ == "__main__":
  main()