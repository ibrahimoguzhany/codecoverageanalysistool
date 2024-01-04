# Yazılım Şartnamesi

## 1. Giriş

### 1.1 Amaç
Bu belge, Yazılım Test Aracı Geliştirme Projesi için tasarlanan yazılımın şartnamesini detaylandırmaktadır. Yazılım, kod analizi, test kapsamı hesaplama ve görselleştirme işlevlerini içermektedir.

### 1.2 Kapsam
Yazılım, aşağıdaki modüllerden oluşmaktadır:
- **Modül-1: Statik Kod Analizi ve Cover Rate Hesaplama**
- **Modül-2: Kodun Grafiksel Temsilinin Oluşturulması ve Görselleştirilmesi**

## 2. Genel Bakış

### 2.1 Sistem Perspektifi
Yazılım, statik kod analizi yaparak ve AST (Abstract Syntax Tree) kullanarak Python kodunun grafiksel temsili üzerinde çalışmaktadır. 

### 2.2 Sistem Fonksiyonları
- **Statik Kod Analizi:** Kod üzerinde syntax hataları, stil sorunları ve diğer kalite kontrol işlemleri gerçekleştirir.
- **Cover Rate Hesaplama:** Test edilen kod satırlarının oranını hesaplar.
- **Grafiksel Görselleştirme:** Kodun AST'sini grafik olarak çizer ve test edilen/test edilmeyen bölümleri renklendirir.

### 2.3 Kullanıcı Arayüzü
- Konsol tabanlı kullanıcı arayüzü.
- Hatalar, uyarılar ve cover rate sonuçları konsolda görüntülenir.
- AST grafiği, görsel bir çıktı olarak sunulur.

## 3. Sistem Gereksinimleri

### 3.1 Fonksiyonel Gereksinimler
- Kodun syntax ve stil analizi yapabilme.
- Test kapsamı oranını hesaplayabilme.
- Kodun grafiksel temsilini oluşturabilme ve renklendirebilme.

### 3.2 Performans Gereksinimleri
- Büyük kod dosyalarını hızlı ve etkin bir şekilde işleyebilme.
- Grafiksel görselleştirmelerin anlaşılır ve net olması.

### 3.3 Güvenlik Gereksinimleri
- Kullanıcı girdilerini doğrulama ve hatalara karşı dayanıklılık.

### 3.4 Diğer Gereksinimler
- Platform bağımsız çalışabilme (Windows, Linux, MacOS).

## 4. Teslimat

### 4.1 Teslimat Maddeleri
- Kaynak kod.
- Kullanım kılavuzu.
- Sistem gereksinimleri belgesi.

### 4.2 Teslimat Tarihleri
- Proje başlangıç tarihi: [Başlangıç Tarihi]
- Proje bitiş tarihi: [Bitiş Tarihi]
