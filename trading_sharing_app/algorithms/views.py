from django.shortcuts import render, redirect, get_object_or_404
from .forms import TradingAlgorithmForm
from .models import TradingAlgorithm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def upload_algo(request):
    if request.method == "POST":
        form = TradingAlgorithmForm(request.POST)
        if form.is_valid():
            algo = form.save(commit=False)
            algo.owner = request.user
            algo.save()
            messages.success(request, "Algorithm uploaded successfully!")
            return redirect('list_algos')
    else:
        form = TradingAlgorithmForm()
        # If there's some custom error or validation you check for
        messages.error(
            request, "There was a problem with your upload. Please try again.")
    return render(request, 'algorithms/upload.html', {'form': form})


@login_required
def list_algos(request):
    algos = TradingAlgorithm.objects.all()
    return render(request, 'algorithms/list.html', {'algos': algos})


@login_required
def my_algorithms(request):
    my_algos = TradingAlgorithm.objects.filter(owner=request.user)
    return render(request, 'algorithms/my_algorithms.html', {'algorithms': my_algos})


@login_required
def delete_algo(request, algo_id):
    algo = get_object_or_404(Algorithm, id=algo_id, owner=request.user)
    algo.delete()
    messages.success(request, "Algorithm deleted successfully!")
    return redirect('my_algorithms')
