"""users routes"""
from flask import current_app as app, jsonify, request
from models import SliderTraining, BaseObject, db
from collections import OrderedDict
import numpy as np
import json
import glob

@app.route('/slider_training/<user_id>/<study_part>', methods=['GET'])

def get_slidertraining(user_id,study_part):


    query = SliderTraining.query.filter(SliderTraining.user_id==user_id, SliderTraining.study_part==study_part)
    if query != None:
        print('Exists')

    block  = query.first_or_404()




    result                   = {}

    arr_id                   = block.get_id() # .replace('  ',' ').split(' ')
    result['id']             = arr_id


    study_part               = block.get_study_part() # [0] # .replace('  ',' ').split(' ')
    result['study_part']   = arr_study_part

    # arr_user               = block.get_startTime().replace('  ',' ').split(' ')
    # result['startTime']   = arr_user

    arr_user            = block.get_user_id().replace('  ',' ').split(' ')
    result['user_id']   = arr_user

    app.logger.info(result)
    return jsonify(result), 200



@app.route('/slider_training/create/<user_id>/<study_part>', methods=['POST', 'GET'])

def post_slidertraining(user_id,study_part):

    content     = request.json
    user = SliderTraining()

    user.user_id          = str(user_id)

    user.study_part     = int(study_part)
    user.startTime       = str(content['startTime'])

    user.sectionStartTime   = str(content['sectionStartTime'])
    user.practSgmMu   = str(content['practSgmMu'])

        # participant.chosen_rewards    = str(content['chosen_rewards'])
        # participant.unchosen_rewards  = str(content['unchosen_rewards'])
        # participant.reaction_time     = str(content['reaction_times'])
        # participant.game_id           = int(content['game_id'])


        # Add the performance metrics here
        # participant.block_perf = content['block_perf']
        # participant.completed  = str(content['completed']) # could take up three values: "no" for the all but the last pushed block,
        # "yes" for the last finished block
        # " aborted" : if the user closes the browser or is idle for more than 10 min on the task, the task window closes itseld

        # participant.date       = content['date']
        # participant.date_time  = str(content['date_time'])

    BaseObject.check_and_save(user)

    result = dict({"success": "yes"})

    return jsonify(result)
