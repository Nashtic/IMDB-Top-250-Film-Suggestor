## Selahattin Ahmed Ataşoğlu - 190401090

# Bilimsel Hesaplama Bütünleme Ödevi

İçerisine asal sayı değerleri satır satır olacak biçimde yazılmış asallar.txt dosyasında bulunan
asal sayı değerlerini 3. dereceden polinoma yakınlaştıran ve istenilen a değerine
(okul numarasının son iki hanesi) göre polinomlu ve polinomsuz olmak üzere
iki farklı şekilde türevlerini bulan programın yazılması beklenmektedir.

## Kullanılan Kütüphaneler

sympy kütüphanesi import edilerek projede kullanılır.

	import sympy as sym


## Projenin Çalışma Prensibi

Yazmış olduğumuz kod içerisinde 8 farklı fonksiyon kullanılmıştır. Yazmış olduğum kodun kullanılış
şeklini, kullanmış olduğum aşağıdaki fonksiyonları ve kullanılış amaçlarını anlatarak şöyle açıklayabiliriz:

### readfile():

Bu fonksiyonumuzda asallar.txt dosyası içerisinde bulunan asal sayı değerleri tek tek çekilir,
çekilen değerler asalDiziDegerler adlı diziye int tipinde olacak şekilde aktarılır.

### matrixWithGauss(Z):

Bu fonksiyonumuzda ise Gauss yöntemiyle matrisler kullanılarak hesaplamalar yapılır.
Gauss yöntemi sayesinde findValues() fonksiyonu içerisinde hesaplamasını yapmış
olduğumuz katsayıların değerleri bulunmuş olur.

### findValues(row, rowValues):

Bu fonksiyonumuzda bizden ödevde istendiği üzere 3. dereceden polinoma yaklaştırma yapılır.
4'e 4'lük bir matris oluşturulur. x'in üssü artacak şekilde diğer denklem değerleri
(y*x, y*x^2, y*x^3 ...) bulunur. Fonksiyonun devamında bulduğumuz bu sonuçlar matrisin
en son sütünlarını atılır. writeDerivativesWithPolynom fonksiyonumuzu kullanarak kullanıcıya
ekranda gösterilecek değerlerden polinomsuz türev sonucu hariç hepsi ekrana bastırılır.

### writeDerivativesWithPolynom(row, rowValues):

Bu fonksiyonda ise yine bir matris oluşturuyoruz. 3. dereceden polinom yaklaştırması yaptığımız
için 3. dereceden yapılan polinom yaklaştırması katsayılarını ekrana yazdırıyoruz.
Bu katsayılar ile polinom denklemimizi günlük hayatta kullandığımız şekilde ekrana yazdırıyoruz. 

#### Not: Yapmış olduğum katsayı hesaplamaları sonucunda ortaya çıkan polinom denklemini göstermek istedim ve bundan dolayı ekrana yazdırdım.


    print("Polinom Denklemi Sonucumuz: \n")                #Polinomların denklem sonuçları yazdırılır.
    equation = coefficients[3] * x ** 3 + coefficients[2] * x ** 2 + coefficients[1] * x + coefficients[0]

    sym.pprint(equation)


Sonrasında tanımladığımız function(x) fonksiyonunu kullanarak polinomlu türev sonucumuzu buluyoruz.
a olarak aldığımız değer okul numaramın sonu 90 ile bittiği için 90 olarak alıyorum.
h değerimiz, polinom kullandığımız için 0.01 gibi dar bir aralıkta alabiliyoruz.

### derivativeWithOutPolynom():

Bu fonksiyonda ise polinomsuz bir şekilde türev hesaplaması yaparak ekrana yazdırıyoruz.
Polinomlu halinden farklı olarak h değerini polinomsuz olduğu için en iyi şart olarak 1 alabiliyoruz.
Hesaplama yapılırken direkt olarak asal sayı değerlerimizi atmış olduğumuz asalDiziDegerler dizisinden
verilerimizi çekerek gerekli hesaplamaları yapıyoruz. Ayrıca dizimiz index[0]'dan başladığından, 
istenen değeri bulabilmemiz için a değerinin bir eksiğini almamız gerekir.

### kodYorumlari():

Polinomlu ve polinomsuz türev hesaplamalarının arasındaki bu farkın neden olduğu yorum satırlarıyla
kısaca açıklanmıştır. Yorumlar yorum.txt adlı bir dosya açılarak içerisine yazılmıştır.

## Kodun Çalıştırıldığı Yer

	readFile()                             # Değerlerin bulunduğu asallar.txt dosyasından veriler satır satır çekilir.
	findValues(0, len(asalDiziDegerler))   # Katsayılar, polinomlu türev ve polinom denklemi değerlerini ekrana yazdırır.
	derivativeWithOutPolynom()             # Polinomsuz türev değerini ekrana yazdırır.
	kodYorumlari()                         # Yorumlar, yorum.txt dosyasına yazılır.

readFile() fonksiyonumuz ile verileri asallar.txt dosyamızdan okuyoruz ve diziye aktarıyoruz.

findValues fonksiyonumuz ile 3. dereceden yaklaştırmamız yapılır ve değerler bulunur. 
Katsayı değerleri matrixWithGauss fonksiyonumuz ile bulunarak coefficient değerine atanır.
Son olarak ise, polinomlu türev değerimizi, katsayıların ve polinom denkleminin değerlerini writeDerivativesWithPolynom ile ekrana yazdırıyoruz.
writeDerivativesWithPolynom'da ise önce bir matris oluşturuyoruz. Katsayı değerlerini yine matrixWithGauss
fonksiyonumuz ile buluyoruz ve bu değerleri coefficients dizimize aktarıyoruz.
Daha sonra katsayılar ve polinom denklemi sonucu yazdırılır. Akabinde gelen function fonksiyonumuz ile
üçüncü dereceden polinomumuz oluşturulur. Polinomlu türev değeri, function fonksiyonundan sonra
hesaplanarak ekrana yazdırılır. Bu hesaplama sırasında a = 90 ve h = 0.01 alınır.

derivativeWithOutPolynom fonksiyonu ile polinomsuz türev hesabı yapılarak ekrana yazdırılır.

kodYorumları() fonksiyonu çalıştırılarak yorum.txt dosyası oluşturularak içine bu yorumlar yazılır.

Başarıyla programdan çıkış yapılır.

## Kodun Çalıştırılabilmesi İçin Gereksinimler

phyton3 versiyonu ile derlenmelidir. sympy kütüphanesi kullanıldığı için bu kütüphanenin
konsol üzerinden gerekli indirmelerinin ya da herhangi bir phyton derleyicisi kullanılıyor ise 
bu kütüphanenin eklenmesi gerekmektedir. 
