from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    ctx ={'title':'welcome'}
    return render(request,'index.html',context= ctx)

@login_required
def profileview(request):
    try:
        profile = Profile.objects.get(user=request.user)
        ctx ={
            'title':'profile',
            'profile':profile,
        }
        return render(request,'users/view_profile.html',context= ctx)
    except Exception as e:
        print(e)
        ctx ={'title':'profile'}
        messages.success(request,'You have not created a profile yet')
        return redirect('profile_edit')

@login_required
def profile_edit(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
    except:
        profile = None
        form = ProfileForm()

    if request.method == 'POST':
        if profile:
            form = ProfileForm(request.POST,request.FILES,instance=profile)
        else:
            form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            
            messages.success(request,'Profile updated successfully')
            return redirect('profile_view')
        else:
            print(form.errors)
            messages.error(request,'Error updating your profile')
    ctx ={
        'title':'profile edit',
        'form':form,
    }
    return render(request,'users/edit_profile.html',context= ctx)

@login_required
def add_pets(request):
    form = PetForm()
    if request.method == 'POST':
        form = PetForm(request.POST,request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user   
            pet.save()
            messages.success(request,'Pet added successfully')
            return redirect('view_pets')
        else:
            print(form.errors)
            messages.error(request,'Error adding pet')
    ctx ={
        'title':'add pet',
        'form':form,
    }       
    return render(request,'pets/add_pet.html',context= ctx)       

@login_required
def view_pets(request):
    try:
        pets = Pet.objects.filter(user=request.user)
        ctx = {'title':'view pets', 'pets':pets}
        return render(request, 'pets/view_pets.html',context=ctx)
    except Exception as e:
        print(e)
        messages.error(request,'You have no pets')
        return redirect('add_pets')

@login_required
def delete_pets(request,pk):
    try:
        Pet.objects.get(id=pk).delete()
        messages.success(request,'Pet successfully deleted')
    except Exception as e:
        print(e)
        messages.error(request,'Error deleting pet') 
    return redirect('view_pets')

@login_required
def edit_pets(request,pk):
    try:
        pet = Pet.objects.get(id=pk)
        form = PetForm(instance=pet)
        if request.method =="POST":
            form = PetForm(request.POST,request.FILES,instance=pet)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                messages.success(request,'Pet updated successfully')
                return redirect('view_pet',pk=pet.id)
            else:
                messages.error(request,'Error updating your pet')
        ctx = {'title':'edit pets','form':form}
        return render(request, 'pets/edit_pets.html',context=ctx)
    except Exception as e:
        return redirect('view_pets')

@login_required
def view_pet_by_id(request,pk):
    try:
        pet = Pet.objects.get(id=pk)
        ctx = {
            'title':'view pet',
            'pet':pet,        
        }
        return render(request, 'pets/view_pet.html',context=ctx)   
    except Exception as e:
        print(e)
        messages.error(request,'Pet not found')
        return redirect('view_pets')

@login_required
def board_pet(request):
    try:
        form = BoardingForm()
        pets = Pet.objects.filter(user=request.user)
        if len(pets) > 0:
            if request.method == 'POST':       
                form = BoardingForm(request.POST)       
                if form.is_valid():       
                    board = form.save(commit=False)       
                    board.status = 'requested'
                    board.user = request.user    
                    board.chargeamount = board.generate_charge_amount()
                    board.save()  
                         
                    messages.success(request,'Boarding information added, Please pay charge to complete request')       
                    return redirect('view_boarding')       
                else:       
                    messages.error(request,'Error updating pet boarding info')
            ctx = {'title':'view pets', 'pets':pets, 'form':form}
            return render(request, 'pets/board_pet.html',ctx)
        else:
            messages.error(request,'No pets to board, register some pets first')
            return redirect('dashboard')
    except Exception as e:
        print(e)
        messages.error(request,e)
        return redirect('dashboard')

@login_required
def delete_boarding(request,pk):
    try:
        Boarding.objects.get(id=pk).delete()
        messages.success(request,'successfully cancelled your request')
    except Exception as e:
        print(e)
        messages.error(request,'Error deleting request') 
    return redirect('view_pets')


@login_required
def view_boarding(request):
    try:
        boardings = Boarding.objects.filter(user=request.user)       
        ctx = {'title':'view boarding', 'boardings':boardings}       
        return render(request, 'pets/view_boarding.html',context=ctx)
    except Exception as e:
        print(e)
        messages.error(request,"Please board a pet first")
        return redirect("board_pets")

@login_required
def view_payment(request):
    return render(request, 'payment/view_payment.html')

@login_required
def make_payment(request,pk):
    try:
        boarding = Boarding.objects.get(id=pk)
        form = PaymentForm()
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                payment = form.save(commit=False)
                payment.user = request.user
                payment.boarding = boarding
                payment.amountpaid = boarding.chargeamount      
                boarding.status = 'preparing'
                payment.save()
                boarding.save()
                messages.success(request,'Payment added successfully')
                return redirect('view_payments')
        ctx = {'title':'make payment', 'form':form,'board':boarding}   
        return render(request, 'payment/make_payment.html',ctx)
    except Exception as e:
        print(e)
        messages.error(request,'Error making payment')
        return redirect('view_payments')