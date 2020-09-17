from .forms import LoginForm

def login_model_form(request):
    return {'login_model_form':LoginForm()}
