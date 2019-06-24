# This module provides an implementation of the heap queue algorithm,
# also known as the priority queue algorithm.
import heapq


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return heapq.nlargest(3, scores)

