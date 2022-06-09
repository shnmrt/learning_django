from django.shortcuts import render


# Create your views in here 

def example_view(request):
    # first_app/templates/first_app/example.html
    return render(request,'first_app/example.html')

def variable_view(request):

    my_var = {
        'first_name': 'Rosalind',
        'last_name' : 'Franklin',
        'some_list' : [1,2,3],
        'some_dict' : {
            'inside_key':'inside_value'
        }
    }
    return render(request, 'first_app/variable.html', context=my_var)