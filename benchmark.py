#!/usr/bin/env python2

import timeit
import argparse
import os

from decimal import Decimal

# ==============================================================================
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--iterations", dest="iterations", default=10000, type=int,
						help="Number of iterations to loop over profiling functions. Default: 10000.")
	parser.add_argument("-r", "--repeat", dest="repeats", default=3, type=int,
						help="Number of times to repeat the iterations as separate profiling runs. Default: 3.")
	parser.add_argument("--samples-dir", dest="samples_dir", default="samples",
						help="Specify alternate directory containing python sample files. Defualt: 'samples'.")
	args = parser.parse_args()

	# Read in all sample files into array so we can call each one.
	sample_path = os.path.abspath(os.path.expanduser(args.samples_dir))
	sample_data = []
	for filename in os.listdir(sample_path):
		# Each sample must have a "sample =" in it.
		exec file(os.path.join(sample_path, filename), "r").read()
		sample_data.append({
			"name": filename,
			"data": sample,
		})

	# Find available serialization runners.
	formats = []
	for f in os.listdir("runners"):
		filename, ext = os.path.splitext(f)
		if filename.startswith("run") and ext == ".py":
			formats.append(filename.split("_")[1])

	# Benchmark.
	for format in formats:
		print "Benchmarking %s..." % format

		for sample_info in sample_data:
			print "Using sample %s..." % sample_info["name"]

			setup_statements = [
				"from runners import run_%s as runner" % format,
				"from decimal import Decimal",
				"data = %s" % sample_info["data"],
			]
			timings = timeit.repeat("runner.serialize(data)", setup="; ".join(setup_statements),
									repeat=args.repeats, number=args.iterations)
			show_results(args, format, sample_info["name"], timings)

		print
		print

# ==============================================================================
def show_results(args, format, sample, results):
	print
	print "Format: %s       Sample: %s" % (format, sample)
	print "-" * 50
	for index, result in enumerate(results):
		print "Pass ", index
		print "Per: %.2f ms" % ((1000000 * result) / args.iterations)
		print "Total: %.2f s" % result
		print
	print "Average: %.2f s" % (float(sum(results)) / float(len(results)))

# ==============================================================================
if __name__ == "__main__":
	main()
