from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    user = {'slackUsername':'Benji', 'backend': True, 'age': 23, 'bio': 'My name is Ben, I am learning'
                                                                        ' backend programming with the hope of having '
                                                                        'better prospects in the future, Thank you'}
    return Response(user)