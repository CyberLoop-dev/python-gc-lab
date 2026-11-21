#!/usr/bin/env python3
"""Inspect Python's cyclic garbage collector with a controlled self-cycle demo."""
from __future__ import annotations

import argparse
import gc
import json
import weakref


class Cycle:
    """A tiny object that references itself so cyclic GC can reclaim it."""

    def __init__(self, marker: int) -> None:
        self.marker = marker
        self.loop = self


def run_demo(count: int = 100) -> dict[str, object]:
    if not isinstance(count, int) or count < 0 or count > 100_000:
        raise ValueError("cycles must be an integer between 0 and 100000")
    before_count = gc.get_count()
    objects = [Cycle(i) for i in range(count)]
    tracked = sum(gc.is_tracked(item) for item in objects)
    references = [weakref.ref(item) for item in objects]
    del objects
    collected = gc.collect(2)
    reclaimed = sum(reference() is None for reference in references)
    return {
        "created_cycles": count,
        "tracked_before_release": tracked,
        "collected_objects": collected,
        "reclaimed_cycles": reclaimed,
        "generation_counts_before": before_count,
        "generation_counts_after": gc.get_count(),
        "thresholds": gc.get_threshold(),
        "collector_stats": gc.get_stats(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Explore Python cyclic garbage collection.")
    parser.add_argument("--cycles", type=int, default=100, help="number of self-referencing objects to create (0-100000)")
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument("--no-demo", action="store_true", help="show collector settings without creating cycles")
    args = parser.parse_args()
    try:
        result = run_demo(0 if args.no_demo else args.cycles)
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Python garbage collector snapshot")
        print(f"Created self-cycles:       {result['created_cycles']}")
        print(f"GC-tracked before release: {result['tracked_before_release']}")
        print(f"Objects collected:         {result['collected_objects']}")
        print(f"Cycles reclaimed:          {result['reclaimed_cycles']}")
        print(f"Generation thresholds:     {result['thresholds']}")
        print(f"GC counts before:          {result['generation_counts_before']}")
        print(f"GC counts after:           {result['generation_counts_after']}")
        print("\nThis demo only creates short-lived Python objects; it does not inspect or alter other processes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
