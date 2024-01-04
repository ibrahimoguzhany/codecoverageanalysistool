# Test Caseleri

## Modül-1: Statik Kod Analizi ve Cover Rate Hesaplama

### Test Case 1: Syntax Hatalarının Tespiti
- **Amaç:** Kodda syntax hatalarının doğru bir şekilde tespit edilmesi.
- **Giriş:** Syntax hatası içeren bir kod parçası.
- **Beklenen Çıktı:** Hata mesajlarının doğru bir şekilde döndürülmesi.

### Test Case 2: Stil İhlallerinin Tespiti
- **Amaç:** Kodda stil ihlallerinin tespit edilmesi.
- **Giriş:** Stil kılavuzuna uymayan bir kod parçası.
- **Beklenen Çıktı:** Stil ihlallerine dair uyarıların döndürülmesi.

### Test Case 3: Cover Rate Hesaplama
- **Amaç:** Test edilen kod satırlarının doğru bir şekilde hesaplanması.
- **Giriş:** Belli fonksiyonları içeren bir kod parçası ve bu fonksiyonların test edilip edilmediği.
- **Beklenen Çıktı:** Doğru cover rate yüzdesinin hesaplanması.

## Modül-2: Kodun Grafiksel Temsilinin Oluşturulması ve Görselleştirilmesi

### Test Case 1: AST Grafiğinin Oluşturulması
- **Amaç:** Kodun AST'sinin doğru bir şekilde oluşturulması.
- **Giriş:** Geçerli bir Python kodu.
- **Beklenen Çıktı:** Kodun AST'sini temsil eden bir grafın oluşturulması.

### Test Case 2: Renklendirme
- **Amaç:** Test edilen ve edilmeyen kod satırlarının grafikte doğru bir şekilde renklendirilmesi.
- **Giriş:** Kodun AST grafiği ve test edilen satırların listesi.
- **Beklenen Çıktı:** Test edilen düğümlerin yeşil, edilmeyenlerin kırmızı olarak renklendirilmesi.

### Test Case 3: Grafiksel Görselleştirme
- **Amaç:** AST grafiğinin görsel olarak açık ve anlaşılır bir şekilde çizilmesi.
- **Giriş:** Renklendirilmiş AST grafiği.
- **Beklenen Çıktı:** Grafiksel çıktının doğru bir şekilde gösterilmesi ve düğümlerin etiketlerinin okunabilir olması.
