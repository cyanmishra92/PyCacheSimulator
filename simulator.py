import argparse
import random
import util
from cache import Cache
from memory import Memory

def read(address, memory, cache):
    """Read a byte from cache."""
    cache_block = cache.read(address)
    if cache_block:
        global hits
        hits += 1
    else:
        block = memory.get_block(address)
        victim_info = cache.load(address, block)
        cache_block = cache.read(address)
        global misses
        misses += 1
        if victim_info:
            memory.set_block(victim_info[0], victim_info[1])
    return cache_block[cache.get_offset(address)]

def write(address, byte, memory, cache):
    """Write a byte to cache."""
    written = cache.write(address, byte)
    if written:
        global hits
        hits += 1
    else:
        global misses
        misses += 1
    if args.WRITE == Cache.WRITE_THROUGH:
        block = memory.get_block(address)
        block[cache.get_offset(address)] = byte
        memory.set_block(address, block)
    elif args.WRITE == Cache.WRITE_BACK:
        if not written:
            block = memory.get_block(address)
            cache.load(address, block)
            cache.write(address, byte)

replacement_policies = ["LRU", "LFU", "FIFO", "RAND"]
write_policies = ["WB", "WT"]

parser = argparse.ArgumentParser(description="Simulate the cache of a CPU.")
parser.add_argument("TRACE_FILE", type=str, help="Path to the trace file containing commands")
parser.add_argument("MEMORY", type=int, help="Size of main memory in 2^N bytes")
parser.add_argument("CACHE", type=int, help="Size of the cache in 2^N bytes")
parser.add_argument("BLOCK", type=int, help="Size of a block of memory in 2^N bytes")
parser.add_argument("MAPPING", type=int, help="Mapping policy for cache in 2^N ways")
parser.add_argument("REPLACE", choices=replacement_policies, help="Replacement policy for cache")
parser.add_argument("WRITE", choices=write_policies, help="Write policy for cache")

args = parser.parse_args()

mem_size = 2 ** args.MEMORY
cache_size = 2 ** args.CACHE
block_size = 2 ** args.BLOCK
mapping = 2 ** args.MAPPING

hits = 0
misses = 0

memory = Memory(mem_size, block_size)
cache = Cache(cache_size, mem_size, block_size, mapping, args.REPLACE, args.WRITE)

with open(args.TRACE_FILE, 'r') as file:
    for line in file:
        command, param = line.strip().split()
        param = int(param)
        if command == "randread":
            for _ in range(param):
                address = random.randint(0, mem_size - 1)
                read(address, memory, cache)
        elif command == "randwrite":
            for _ in range(param):
                address = random.randint(0, mem_size - 1)
                byte = util.rand_byte()
                write(address, byte, memory, cache)

# After processing all commands, print statistics
ratio = (hits / ((hits + misses) if misses else 1)) * 100
print("\nHits: {0} | Misses: {1}".format(hits, misses))
print("\nHit Rate: {0:.2f}%".format(ratio) + "\n")

