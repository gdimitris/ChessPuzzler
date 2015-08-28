
__author__ = 'dimitris'

import random

from Application import app, cache
from Application.models import ChessPuzzle
from flask import jsonify

MATE_IN_2_ID = 1
MATE_IN_3_ID = 2
MATE_IN_4_ID = 3
CACHE_TIMEOUT = 10000

@app.route('/mate2', methods=['GET'])
def mate2():
    all_mate2 = get_all_mate2()
    chosen_entry = pick_random_entry(all_mate2)
    return jsonify_puzzle_object(chosen_entry)


@app.route('/mate3', methods=['GET'])
def mate3():
    all_mate3 = get_all_mate3()
    chosen_entry = pick_random_entry(all_mate3)
    return jsonify_puzzle_object(chosen_entry)


@app.route('/mate4', methods=['GET'])
def mate4():
    all_mate4 = get_all_mate4()
    chosen_entry = pick_random_entry(all_mate4)
    return jsonify_puzzle_object(chosen_entry)


def jsonify_puzzle_object(puzzle_object):
    return jsonify(puzzle_id=puzzle_object.puzzle_id,
                   description=puzzle_object.description,
                   fen=puzzle_object.fen, solution=puzzle_object.solution)


def pick_random_entry(object_list):
    rand_int = random.randrange(0, len(object_list))
    return object_list[rand_int]


def get_all_mate2():
    return query_all_by_type_id(MATE_IN_2_ID)


def get_all_mate3():
    return query_all_by_type_id(MATE_IN_3_ID)


def get_all_mate4():
    return query_all_by_type_id(MATE_IN_4_ID)

@cache.memoize(timeout=CACHE_TIMEOUT)
def query_all_by_type_id(type_id):
    return ChessPuzzle.query.filter_by(type_id=type_id).all()