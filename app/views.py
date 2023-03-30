from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def procesar(request):
    #recuperando datos de la pagina index.html
    n1=float(request.GET['num1'])
    n2=float(request.GET['num2'])
    ope=request.GET.get('operador')
    res=0
    #procesar datos
    match ope:
        case '+':
            res=n1+n2
        case '-':
            res=n1-n2
        case '/':
            if n2==0:
                sw=True
                return render(request,"app/resultado.html",{'msg':'No se puede dividir entre cero','sw':sw})
            else:
                res=n1/n2
        case 'x':
            res=n1*n2
        case _:
            res=0
    return render(request,'app/resultado.html',{'result':res})


