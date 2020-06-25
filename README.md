# Bilimsel Hesaplama Bütünleme Ödevi

## Kullanılan Kütüphaneler

sympy ve math kütüphaneleri import edilerek projede kullanılır.

'''bash
import sympy as sym
import math
'''

## Projenin Çalışma Prensibi

Yazmış olduğumuz kod içerisinde 8 farklı fonksiyon kullanılmıştır.
Bu fonksiyonları şöyle sıralayabiliriz:

### readfile():

Bu fonksiyonumuzda asallar.txt dosyası içerisinde bulunan asal sayı değerleri tek tek çekilir,
çekilen değerler asalDiziDegerler adlı diziye int tipinde olacak şekilde aktarılır.

### matrixWithGauss(Z):

Bu fonksiyonumuzda ise Gauss yöntemiyle matrisler kullanılarak hesaplamalar yapılır.

### correlation(myLastResults):

Bu fonksiyonumuzda, polinoma yaklaştırma methodunda olduğu üzere, korelasyon katsayısı
hesaplaması formülündeki işlemler burada yapılır. Burada r değeri bulunur. 
(r^2 = (St - Sr) / St)

### findValues(row, rowValues):

Bu fonksiyonumuzda bizden ödevde istendiği üzere 3. dereceden polinoma yaklaştırma yapılır.
4'e 4'lük bir matris oluşturulur. x'in üssü artacak şekilde diğer denklem değerleri
(y*x, y*x^2, y*x^3 ...) bulunur. Fonksiyonun devamında bulduğumuz bu sonuçlar matrisin
en son sütünlarını atılır. writeDerivativesWithPolynom fonksiyonumuzu kullanarak kullanıcıya
ekranda gösterilecek değerlerden polinomsuz türev sonucu hariç hepsi ekrana bastırılır.

### writeDerivativesWithPolynom():

Bu fonksiyonda ise yine bir matris oluturuyoruz. 3. dereceden polinom yaklaştırması yaptığımız
için 3. dereceden yapılan polinom yaklaştırması katsayılarını ekrana yazdırıyoruz.
Bu katsayılar ile polinom denklemimizi günlük hayatta kullandığımız şekilde ekrana yazdırıyoruz.

'''bash
print("Polinom Denklemi Sonucumuz: \n")                #Polinomların denklem sonuçları yazdırılır.
    equation = coefficients[3] * x ** 3 + coefficients[2] * x ** 2 + coefficients[1] * x + coefficients[0]

    sym.pprint(equation)
'''

Sonrasında tanımladığımız function(x) fonksiyonunu kullanarak polinomlu türev sonucumuzu buluyoruz.
x0 olarak aldığımız değer okul numaramın sonu 90 ile bittiği için 90 olarak alıyorum.
h değerimiz, polinom kullandığımız için 0.01 gibi dar bir aralıkta alabiliyoruz.

### derivativeWithOutPolynom():

Bu fonksiyonda ise polinomsuz bir şekilde türev hesaplaması yaparak ekrana yazdırıyoruz.
Polinomlu halinden farklı olarak h değerini polinomsuz olduğu için en iyi şart olarak 1 alabiliyoruz.
Hesaplama yapılırken direkt olarak asal sayı değerlerimizi atmış olduğumuz asalDiziDegerler dizisinden
çekerek gerekli hesaplamaları yapıyoruz.

### kodYorumlari():

Polinomlu ve polinomsuz türev hesaplamalarının arasındaki bu farkın neden olduğu yorum satırlarıyla
kısaca açıklanmıştır.

## Kodun Çalıştırıldığı Yer

readFile() fonksiyonumuz ile verileri txt dosyamızdan okuyoruz.
findValues fonksiyonumuz ile polinomlu türev değerimizi, katsayılarını ve polinom denklemini ekrana
yazdırıyoruz.
derivativeWithOutPolynom fonksiyonu ile polinomsuz türev hesabı yapılarak ekrana yazdırılır.
kodYorumları() fonksiyonu çalıştırılarak yorum.txt dosyası oluşturularak içine bu yorumlar yazılır.
Başarıyla programdan çıkış yapılır.
