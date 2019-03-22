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
دلار:['128,940', '128,960', '128,800', '-', '-', '-', '۲۸ اسفند', '128,940', '0%', '0'] 
 --------------------------------------------
طلای ۲۴ عیار:['5,731,600', '5,731,600', '5,534,600', '-', '-', '-', '۲۸ اسفند', '5,731,600', '0%', '0']
```
4) The order of the above list is as follows
```
نرخ فعلی', 'بالاترین قیمت روز', 'پایین ترین قیمت روز', 'بیشترین مقدار نوسان روز', 'درصد بیشترین نوسان روز', 'نرخ بازگشایی بازار', 'زمان ثبت آخرین نرخ', 'نرخ روز گذشته', 'درصد تغییر نسبت به روز گذشته', 'میزان تغییر نسبت به روز گذشته
```
# TODO
- [x] Complete with OOP
- [ ] Set name for currency

