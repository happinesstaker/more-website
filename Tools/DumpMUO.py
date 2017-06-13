'''This module dumps data from SERF website and save in json format

Purpose of this function is for better demonstrative effect.
Note that we can save the whole database file in csv format for later import

'''

from muo.models import MisuseCase, MUOContainer, UseCase
from cwe.models import CWE

import json

def buildMUO():
    for muo in MUOContainer.objects.approved():
        name = muo.name
        muo_json = {"name": name}
        muo_json["cwes"] = list()
        for cwe in muo.cwes.all():
            muo_json["cwes"].append({"code": cwe.code,
                                     "name": cwe.name,
                                     "description": cwe.description})

        misuse = muo.misuse_case
        muo_json["misuse_case"] = {"name": misuse.name,
                                   "description": misuse.misuse_case_description,
                                   "primary": misuse.misuse_case_primary_actor,
                                   "secondary": misuse.misuse_case_secondary_actor,
                                   "precondition": misuse.misuse_case_precondition,
                                   "flow": misuse.misuse_case_flow_of_events,
                                   "postcondition": misuse.misuse_case_postcondition,
                                   "assumption": misuse.misuse_case_assumption,
                                   "source": misuse.misuse_case_source}
        muo_json["use_cases"] = list()
        for use in misuse.usecase_set.approved():
            muo_json["use_cases"].append({"name": use.name,
                                   "description": use.use_case_description,
                                   "primary": use.use_case_primary_actor,
                                   "secondary": use.use_case_secondary_actor,
                                   "precondition": use.use_case_precondition,
                                   "flow": use.use_case_flow_of_events,
                                   "postcondition": use.use_case_postcondition,
                                   "assumption": use.use_case_assumption,
                                   "source": use.use_case_source})
        with open('MUO_json/' + name, 'w') as output:
            output.write(json.dumps(muo_json, indent=4, sort_keys=True))

def run():
    print "Start dumping MUOs from SERF"
    buildMUO()
