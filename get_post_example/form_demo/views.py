# views.py
from django.shortcuts import render
from .forms import CalculatorForm

def calculator_view(request):
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            operation = form.cleaned_data['operation']
            
            if operation == '+':
                result = number1 + number2
            elif operation == '-':
                result = number1 - number2
            elif operation == '*':
                result = number1 * number2
            elif operation == '/':
                result = number1 / number2 if number2 != 0 else 'Error: Division by zero'
    else:
        form = CalculatorForm()

    return render(request, 'calculator.html', {'form': form, 'result': result})
