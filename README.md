# CurrencyScraping

This is an script that you can grab data from Specific Currency Website

# Usage

1) Create Object from Get_price Class ,Enter list of URl
```python
obj_test = Get_price(['https://www.tgju.org/chart/price_dollar_rl','http://www.tgju.org/chart/geram24'])
```

2) Call fetch_price() From Class 
```python
obj_test = Get_price(['https://www.tgju.org/chart/price_dollar_rl','http://www.tgju.org/chart/geram24'])
obj_test.fetch_price()
```
3) Console Print
```
unknown:['128,470', '128,550', '128,430', '120', '0.03%', '128,490', '۱۱', '128,470', '0%', '0'] 
 --------------------------------------------
unknown:['5,513,000', '5,534,600', '5,442,200', '46,200', '0.11%', '5,442,200', '۱۱', '5,448,400', '1.19%', '64,600'] 
 --------------------------------------------
```
4) The order of the above list is as follows
```
نرخ فعلی', 'بالاترین قیمت روز', 'پایین ترین قیمت روز', 'بیشترین مقدار نوسان روز', 'درصد بیشترین نوسان روز', 'نرخ بازگشایی بازار', 'زمان ثبت آخرین نرخ', 'نرخ روز گذشته', 'درصد تغییر نسبت به روز گذشته', 'میزان تغییر نسبت به روز گذشته
```
# TODO
- [x] Complete with OOP
- [ ] Set name for currency

