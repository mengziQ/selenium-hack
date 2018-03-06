# seleniumを使った自動入力  
## 実装でつまったところ  
1. body内にフレームが複数ある場合、該当のフレームまで移動しないと要素を取得できない。  
```
driver.switch_to.frame("f1")
```

2. 要素のvalue属性を書き換えることはseleniumAPIではできない。これはjavascriptをseleniumオブジェクト内で実行することによって実現できる。
```
driver.execute_script("parent.f1.document.getElementsByName('xxxx').item(0).value = 1;")
```

3. ページ遷移先ですぐに要素を取得しようとすると"NoSuchElementException: Unable to locate element"が発生する場合がある。
これは、レスポンス遅延によって要素が表示される前にアクセスしていることが原因。以下のコードで待機することで解消した。  
```
 WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.NAME, 'xxxx')))
```
