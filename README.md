# Python Cache Simulator

This is a simulator for a CPU cache that I wrote for a college course. It's
meant to demonstrate some of the different
[replacement](https://en.wikipedia.org/wiki/CPU_cache#Replacement_policies),
[write](https://en.wikipedia.org/wiki/CPU_cache#Write_policies), and [mapping
policies](https://en.wikipedia.org/wiki/CPU_cache#Associativity) that CPUs can
implement.


To run the CPU cache simulator:

    simulator.py [-h] TRACE_FILE_NAME MEMORY CACHE BLOCK MAPPING REPLACE WRITE


Once you start the simulator, you can enter commands to modify and read from the
memory (which is randomized on initilization), and therefore indirectly modify
the cache. You can also print the contents of the memory and cache, as well as
view statistics about the cache's performance.

The arguments and commands, along with their descriptions, are listed below.


### Arguments

**MEMORY** - size of main memory in 2^N bytes

**CACHE** - size of the cache in 2^N bytes

**BLOCK** - size of a block of memory in 2^N bytes

**MAPPING** - mapping policy for cache in 2^N ways
*   0 - direct mapping
*   \>0 - 2^N way associative

**REPLACE** - replacement policy for cache
*   LRU - least recently used
*   LFU - least frequently used
*   FIFO - first-in, first-out
*   RAND - random

**WRITE** - write policy for cache
*   WB - write back
*   WT - write through

## Example

Here is an example run:

    python simulator.py trace.tr 10 7 3 2 LRU WT

This creates a simulation with 2^10 bytes of memory, 2^7 bytes of cache, uses
8-way (2^3) associate mapping, least-recently used replacement policy, and
write-through write policy.

### Generating Trace File

Run the generate_trace.py for generating a tracefile. This code needs a random seed. The seed will be your PSU ID.

options:
  -h, --help         show this help message and exit
  --fname FNAME      Path to the trace file to be generated.
  --numcmds NUMCMDS  Number of commands to generate.
  --maxamt MAXAMT    Maximum value for the AMOUNT parameter in commands.
  --seed SEED        Seed for the random number generator to ensure reproducibility.

    usage: generate_trace.py [-h] [--fname FNAME] [--numcmds NUMCMDS] [--maxamt MAXAMT] [--seed SEED]

Example:

    python generate_trace.py --fname trace.tr --seed 123456789

It genrates a trace file of 1 million size. To get started with simulation, start with a smaller trace and then proceed with a larger trace. 
