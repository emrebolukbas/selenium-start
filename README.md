#pyTest Decorator
----
Bu ReadMe dosyası, PyTest'te dekoratörlerin nasıl kullanılacağına 
dair kapsamlı bir rehber sunar. Dekoratörler, test kodunuzu daha okunabilir, 
organize ve bakımı kolay hale getirmenin güçlü bir yoludur. Bu rehberde, aşağıdakileri de içeren çeşitli dekoratörleri keşfedeceksiniz:

Temel Dekoratörler:
-----
@pytest.fixture: Test fonksiyonları için bağımlılıklar oluşturmak için kullanılır.

@pytest.mark.parametrize: Farklı parametrelerle bir test fonksiyonunu tekrar tekrar çalıştırmak için kullanılır.

@pytest.mark.skip: Belirli bir test fonksiyonunu veya sınıfını atlamak için kullanılır.

@pytest.mark.xfail: Bir test fonksiyonunun beklendiği gibi başarısız olmasını beklemek için kullanılır.

Gelişmiş Dekoratörler:
----
@pytest.hookimpl: PyTest'in kendi kancalarını özelleştirmek için kullanılır.

@pytest.fixture_scope: Bir fikstürün kapsamını (fonksiyon, modül, oturum vb.) ayarlamak için kullanılır.

@pytest.autouse: Her test fonksiyonu çalıştırılmadan önce otomatik olarak yürütülen bir fonksiyon tanımlamak için kullanılır.
