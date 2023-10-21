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
import asyncio
import signal

topTen = False

def main():
  check_args_length()
  check_for_flag()
  is_args_valid_ip4_addr()
  asyncio.run(iter_ports_for_connection())
  sys.exit(0)

############################################################
  
def check_args_length():
  args_len = len(sys.argv)
  if args_len < 2:
      print("One argument expected.")
      print("For help, use the -h flag.")
      raise SystemExit(2)

def check_for_flag():
  global topTen 
  if "-h" in sys.argv:
    print("EasySocketHunter - Port Scanner")
    print("Usage: python easysockethunter.py <target_IP> [options]")
    print()
    print("Options:")
    print("-s   Scan only the top 10 common ports.")
    print("-h   Show this help message.")
    sys.exit(0)
  if "-s" in sys.argv:
    topTen = True

def is_args_valid_ip4_addr():
  match = re.search(r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}$", sys.argv[1])
  if not match:
    print("The first arugment is not a valid IPv4 address")
    print("You must specify the target IP")
    print("For help, use the -h flag")
    raise SystemExit(2)
  
def exec_port_scan(port):
  try:
    socket.setdefaulttimeout(1)
    c = socket.socket()
    c.connect((sys.argv[1], port))
    print(f"Port {port} is open")
    c.close()
  except:
    pass
  
async def iter_ports_for_connection():
  if topTen:
    print("Now scanning the top 10 Ports...")
    top_ports = [80, 443, 21, 22, 25, 110, 143, 993, 995, 3306]
    await asyncio.gather((exec_port_scan(port)) for port in top_ports)
  else:
    print("Now scanning all Ports...")
    await  asyncio.gather((exec_port_scan(port)) for port in range(1, 65536))
    
  print("Finished the scan, now exiting.\nThank you for using EasySocketHunter!")

def signal_handler(sig, frame):
  print("\nScan interrupted. Exiting...")
  sys.exit(0)
  
signal.signal(signal.SIGINT, signal_handler)
  
if __name__ == "__main__":
  main()