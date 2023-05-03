class checkout():
    # Add to cart
    books_category = "/html/body/div[4]/div[1]/div[2]/ul[1]/li[1]/a" #xpath
    fictionbook = "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[3]/div/div[2]/h2/a" #xpath
    addtocart_btn = "add-to-cart-button-45" #id
    # Shopping cart
    shoppingcart = "cart-label" #class
    
    termofservice_checkbox = "termsofservice" #id
    checkout_btn = "checkout" #id 
    notcheck_termofservice_checkbox_msg = "terms-of-service-warning-box" #id

    #Success add to cart
    product_success_addt0_shopping_cart_msg = "bar-notification" # id

    # Checkout
    # Billing address
    country = "CountryId" #id  
    country2 = "BillingNewAddress_CountryId" #id
    choosecountry = "42" #value indonesia
    address="billing-address-select" # id
    newaddress="New Address" #value
    city = "BillingNewAddress_City" #id
    address1 = "BillingNewAddress_Address1" #id
    address2 = "BillingNewAddress_Address2" #id
    zipcode = "BillingNewAddress_ZipPostalCode" #id
    phonenumber = "BillingNewAddress_PhoneNumber" #id 
    faxnumber = "BillingNewAddress_FaxNumber" #id
    continue_btn = "//input[@onclick='Billing.save()']" #xpath

    # Shipping address 
    pickpuninstore = "PickUpInStore" #id  
    shippingaddress_continue_btn = "//input[@onclick='Shipping.save()']" #xpath

    #Shipping Method
    shippingoption1 = "shippingoption_0" #id 
    shippingmethod_continue_btn = "/html[1]/body[1]/div[4]/div[1]/div[4]/div[1]/div[1]/div[2]/ol[1]/li[3]/div[2]/form[1]/div[2]/input[1]" #xpath

    # Payment Method
    payment_cod = "paymentmethod_0" #id 
    paymentmethod_continue_btn = "//input[@onclick='PaymentMethod.save()']" #xpath 

    # Payment information
    paymentinformation_cod = "section payment-info" #class
    paymentinformation_continue_btn = "//input[@onclick='PaymentInfo.save()']" #xpath

    # Confirm Order
    confirm_book_fiction ="product-name" #class
    confirm_continue_btn = "//input[@value='Confirm']" #xpath

    #Success
    success_checkout = "section order-completed" # Class

    #failed not input country
    failed_not_input_country_msg = "field-validation-error" # Class

    

    
