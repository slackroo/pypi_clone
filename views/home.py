import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/')
# @template(template_file='home/index.pt')
# changing the file from .HTML to .py, the template decorator has a convention that will look at module name home and it will look for method name index
# we use below  due to change to.pt else the abovce # out line 7 @template
@template()
def index(user: str = 'anon'):
    return {
        'user_name': user
    }

@router.get('/about')
@template()
def about():
    return {}