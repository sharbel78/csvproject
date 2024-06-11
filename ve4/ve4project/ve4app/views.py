import matplotlib.pyplot as plt
from django.shortcuts import render,redirect
import  pandas as pd
import  numpy as np

import  seaborn as sb
from .forms import csvFileform
from  .models  import CSVfile

# Create your views here.
def uploadfile(request):
    if request.method == 'POST':
        form = csvFileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('csvapp:result')
    else:
        form =csvFileform()
    return  render(request,'csvupload.html',{'form':form})
def result(request):
    csv_file = CSVfile.objects.last()
    df = pd.read_csv(csv_file.file.path)

    head= df.head()
    summary = df.describe()
    missing = df.isnull().sum()

    plt.figure()
    sb.histplot(df.select_dtypes(include=[np.number]))
    plt.savefig('static/plots/histogram.png')
    plt.close()

    context = {

        'head':head.to_html(),
        'summary':summary.to_html(),
        'missing':missing.to_dict(),
        'histogram':'static/plots/histogram.png'
    }
    return render(request,'result.html',context)