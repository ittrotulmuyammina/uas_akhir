function submitPayment() {
    // Dapatkan nilai dari formulir pembayaran
    var cardNumber = document.getElementById('cardNumber').value;
    var expiryDate = document.getElementById('expiryDate').value;
    var cvv = document.getElementById('cvv').value;

    // Validasi sederhana (Anda perlu validasi yang lebih kuat dalam produksi)
    if (cardNumber && expiryDate && cvv) {
        // Kirim data pembayaran ke server (simulasi)
        // Di sini Anda dapat menggunakan AJAX atau mengirim data ke backend
        var paymentResult = "Pembayaran berhasil!"; // Hasil dari server

        // Tampilkan hasil pembayaran
        document.getElementById('paymentResult').innerHTML = paymentResult;
    } else {
        alert("Silakan lengkapi semua field pembayaran.");
    }
}
