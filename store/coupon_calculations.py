def calculate_price(price, cash_coupon, percent_coupon):
    after_cash_coupon = price - cash_coupon
    after_percent_coupon  = after_cash_coupon - (after_cash_coupon * percent_coupon / 100)
    taxed_price =(after_percent_coupon * 1.06)
    if after_percent_coupon <=10:
        shipping=after_percent_coupon+5.95
    if  after_percent_coupon >10 and after_percent_coupon<=30:
        shipping=after_percent_coupon+7.95
    if after_percent_coupon > 30 and after_percent_coupon<=50:
        shipping=after_percent_coupon +11.95
    if after_percent_coupon >50:
        shipping=0
    finalPrice = (taxed_price + shipping)

    print(f'The original price was, {price} , the price after cash coupon was {after_cash_coupon}, the price after percent coupon {after_percent_coupon},  the price after tax was {taxed_price}, shipping cost was {shipping} and the final price was {finalPrice}.')




if __name__ == '__main__':
    print (calculate_price(9,5,10))


