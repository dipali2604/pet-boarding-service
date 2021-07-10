console.log('loaded main js')




fetch('/config/')
.then((result) =>{
    return result.json();
})
.then((data)=>{
    const stripe = Stripe(data.publicKey)
    var payment_method = document.querySelector('#id_payment_method');
    var cbtn = document.querySelector('#complete')
    var id = document.querySelector('#boarding_id')
    sessionStorage.setItem("bid", id);
    cbtn.disabled =true;
    var out = document.querySelector('#out');
    payment_method.addEventListener('change', function (e) {
        var payment_method = e.target.value
        if (payment_method == 'Cash On Delivery') {
            cbtn.disabled = false;
            out.innerHTML = 'Payment Method: Cash On Delivery<br>Click to complete';
            out.className ="alert alert-success text-center"
            
            
        } else if(payment_method == 'payment gateway') {
            out.innerHTML = ' <button type="button" class="btn btn-danger btn-block " id="purchasebtn">Use Payment gateway</button>';
            out.className ="alert-danger text-center"
            var price = parseFloat(document.querySelector('#price').innerHTML);
            document.querySelector('#purchasebtn').addEventListener('click',()=>{
                
                fetch('/create-checkout-session/?price='+price)
                .then((result)=>{return result.json();})
                .then((data)=>{
                    console.log(data);
                    return stripe.redirectToCheckout({sessionId:data.sessionId,})
                }).
                then((res)=>{
                    console.log(res)
                })
            });
        }
    });
    
});