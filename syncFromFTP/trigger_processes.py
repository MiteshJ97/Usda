from rest_framework.decorators import api_view
from . import step1, step2, step3, step4, step5, step6, step7, step8, step9, step10, step11
from rest_framework.response import Response
import time
from .wrapper import *


@timer
@api_view(['GET'])
def trigger_steps(request):
    res = step1.step_actions('test.txt', 'output.txt')
    res = step2.step_actions(res, 'output.txt')
    res = step3.step_actions(res, 'output.txt')
    res = step4.step_actions(res, 'output.txt')
    res = step5.step_actions(res, 'output.txt')
    res = step6.step_actions(res, 'output.txt')
    res = step7.step_actions(res, 'output.txt')
    res = step8.step_actions(res, 'output.txt')
    res = step9.step_actions(res, 'output.txt')
    res = step10.step_actions(res, 'output.txt')
    res = step11.step_actions(res, 'output.txt')
    time.sleep(1)
    print("All steps executed successfully.")
    time.sleep(1)
    return Response("All steps executed successfully.")